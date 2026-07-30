import sys
import os
import xml.etree.ElementTree as ET
from src.processing.grayscale import load_and_convert_grayscale
from src.vis.preprocessing_plots import plot_grayscale_comparison

def parse_student_info(xml_path):
    """
    Reads info.xml and extracts student Index and Name as a list.
    Contributed by: Member 01 (CLI & XML Handling)
    """
    if not os.path.exists(xml_path):
        print(f"Error: XML file '{xml_path}' not found.")
        return []

    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    students = []
    for student in root.findall('.//student'):
        idx = student.find('index').text if student.find('index') is not None else ''
        name = student.find('name').text if student.find('name') is not None else ''
        students.append({'index': idx, 'name': name})
        
    return students

def run_pipeline(image_path, xml_path):
    """
    Main function to execute the Attendance Processing Pipeline.
    """
    print("=" * 60)
    print("   NSBM Student Attendance Management System (SAMS)")
    print("=" * 60)

    # 1. Load Student Records from XML.
    students = parse_student_info(xml_path)
    print(f"\n[INFO] Loaded {len(students)} student records from {xml_path}:")
    for s in students:
        print(f"       -> Index: {s['index']} | Name: {s['name']}")

    # 2. Member 01: Image Preprocessing (Grayscale Conversion)
    print(f"\n[STEP 1] Loading image and converting to Grayscale ({image_path})...")
    try:
        original_img, gray_img = load_and_convert_grayscale(image_path)
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    # 3. Member 01: Visualization (Grayscale Comparison Plot)
    print("[VISUALIZATION] Displaying Member 01 Pre-processing Plot...")
    plot_grayscale_comparison(original_img, gray_img)

    print("\n[SUCCESS] Member 01 Pipeline Step completed successfully!")
    print("=" * 60)

if __name__ == '__main__':
    # Default values if terminal arguments are not provided:
    img_arg = sys.argv[1] if len(sys.argv) > 1 else 'dataset/1.jpeg'
    xml_arg = sys.argv[2] if len(sys.argv) > 2 else 'dataset/info.xml'
    
    run_pipeline(img_arg, xml_arg)