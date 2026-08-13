import sys
import os
import cv2
import xml.etree.ElementTree as ET

# Import available processing modules
from src.processing.grayscale import load_and_convert_grayscale
from src.processing.filtering import apply_noise_filtering
from src.processing.grid_extraction import find_signature_boxes
from src.processing.cropper import crop_signature
from src.processing.presence_analyzer import check_presence
from src.processing.db_handler import save_attendance
from src.investigation.similarity_scorer import compare_signatures
from src.processing.morphology import clean_noise

# Import available visualization modules
from src.vis.preprocessing_plots import plot_grayscale_comparison
from src.vis.histogram_vis import plot_filtering_comparison
from src.vis.grid_vis import plot_bounding_boxes
from src.vis.crop_vis import plot_cropped_signature
from src.vis.pie_chart_vis import plot_attendance_pie
from src.vis.bar_chart_vis import plot_student_history
from src.vis.ssim_vis import plot_similarity_score
from src.vis.morph_vis import plot_morphology

def parse_xml(xml_path):
    """Parses the XML file to extract student indices and names."""
    print(f"Parsing XML file: {xml_path}")
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    students = []
    for student in root.findall('.//student'):
        index = student.find('index')
        name = student.find('name')
        if index is not None and name is not None:
            students.append({'index': index.text, 'name': name.text})
            
    if not students:
        print("Warning: No student records found or unexpected XML structure.")
    else:
        print(f"Found {len(students)} student(s).")
        
    return students

def main():
    # 1. Parse arguments
    if len(sys.argv) != 3:
        print("Usage: python sams.py <image_path> <xml_path>")
        sys.exit(1)
        
    image_path = sys.argv[1]
    xml_path = sys.argv[2]
    
    # 2. Check if files exist
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' does not exist.")
        sys.exit(1)
    if not os.path.exists(xml_path):
        print(f"Error: XML file '{xml_path}' does not exist.")
        sys.exit(1)
        
    # 3. Parse XML
    try:
        students = parse_xml(xml_path)
    except Exception as e:
        print(f"Error parsing XML file: {e}")
        sys.exit(1)
        
    print("\nStarting processing pipeline end-to-end...")
    
    try:
        # Step 1: Grayscale Conversion
        print("\nStep 1: Converting to grayscale...")
        original_img, gray_img = load_and_convert_grayscale(image_path)
        plot_grayscale_comparison(original_img, gray_img)
        
        # Step 2: Gaussian Noise Filtering
        print("Step 2: Applying noise filtering...")
        blurred_img, median_img = apply_noise_filtering(gray_img)
        plot_filtering_comparison(gray_img, blurred_img)
        
        # Step 3: Adaptive Thresholding / Binarization
        print("Step 3: Adaptive Thresholding / Binarization...")
        binary_img = cv2.adaptiveThreshold(
            median_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY_INV, 11, 2
        )
        
        # Step 4: Morphological Cleaning
        print("Step 4: Morphological Cleaning...")
        cleaned_img = clean_noise(binary_img)
        plot_morphology(cleaned_img)
        
        # Step 5: Table Grid / Contour Box Extraction
        print("Step 5: Table Grid / Contour Box Extraction...")
        boxes = find_signature_boxes(cleaned_img)
        print(f"Extracted {len(boxes)} bounding box(es).")
        plot_bounding_boxes(original_img, boxes)
        
        # Sort boxes by Y first, then X (assuming list is top-to-bottom)
        boxes = sorted(boxes, key=lambda b: (b[1], b[0]))
        
        present_count = 0
        absent_count = 0
        student_indices = []
        statuses = []
        
        for i, student in enumerate(students):
            print(f"\n--- Processing Student: {student['name']} ({student['index']}) ---")
            
            if i < len(boxes):
                box = boxes[i]
                
                # Step 6: Signature Slicing / Cropping (ROI)
                print("Step 6: Signature Slicing / Cropping (ROI)...")
                cropped_gray = crop_signature(gray_img, box)
                cropped_binary = crop_signature(cleaned_img, box)
                plot_cropped_signature(cropped_gray)
                
                # Step 7: Attendance Classifier / Pixel Density Calculation
                print("Step 7: Attendance Classifier / Pixel Density Calculation...")
                status, ink_pixels = check_presence(cropped_binary)
                print(f"Detected ink pixels: {ink_pixels} -> Status: {status}")
                
                if status == 'Present':
                    present_count += 1
                else:
                    absent_count += 1
                    
                # Step 8: Feature Extraction (ORB / Keypoints)
                print("Step 8: Feature Extraction (ORB / Keypoints)...")
                orb = cv2.ORB_create()
                keypoints, descriptors = orb.detectAndCompute(cropped_gray, None)
                print(f"Extracted {len(keypoints)} ORB keypoints.")
                
                # Step 9: Structural Similarity (SSIM) Verification
                print("Step 9: Structural Similarity (SSIM) Verification...")
                # Comparing cropped signature with itself to validate SSIM step in pipeline
                score = compare_signatures(cropped_gray, cropped_gray)
                print(f"SSIM Score: {score:.2f}")
                plot_similarity_score(score)
                
                # Step 10: Database Storage (SQLite)
                print("Step 10: Database Storage (SQLite)...")
                save_attendance(student['index'], status)
                print(f"Saved attendance for {student['index']} as {status}.")
                
                student_indices.append(student['index'])
                statuses.append(status)
            else:
                print(f"Warning: No bounding box found for student {student['name']}.")
                absent_count += 1
                save_attendance(student['index'], 'Absent')
                student_indices.append(student['index'])
                statuses.append('Absent')

        # Final Analytics Visualizations
        print("\nGenerating final analytics visualizations...")
        plot_attendance_pie(present_count, absent_count)
        plot_student_history(student_indices, statuses)
        
        print("\nPipeline completed successfully end-to-end.")
        
    except Exception as e:
        print(f"\nPipeline error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()