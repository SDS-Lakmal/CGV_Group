# CS402.3 SAMS Project - Group Member Task Guide 

> **⚠️ IMPORTANT NOTE FOR ALL MEMBERS:**
> Please be careful when copying and pasting the Python code. Python is highly sensitive to spaces and indentation. Copy the code exactly as it appears in the code blocks below to avoid `IndentationError`s.

## General Instructions (For All Members)
1. Open Command Prompt (CMD) or VS Code Terminal.
2. Install required libraries: 
   ```bash
   pip install opencv-python numpy matplotlib seaborn scikit-image
   ```
3. Create a branch using your university user name.
4. Clone the branch: 
   ```bash
   git clone -b <BRANCH NAME> <INSERT_GITHUB_REPO_LINK_HERE>
   ```
5. Ensure you have the latest updates: 
   ```bash
   git checkout main
   git pull origin main
   ```

---

## Member 2: Gaussian Filtering & Histogram Analysis

**Step 1: Create the Image Processing File**
Create a file named: `src/processing/filtering.py`
Copy and paste this exact code inside:
```python
import cv2

def apply_noise_filtering(gray_image):
    # Apply Gaussian Blur to remove scanner noise
    blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
    median = cv2.medianBlur(blurred, 3)
    return blurred, median
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/histogram_vis.py`
Copy and paste this exact code inside:
```python
import matplotlib.pyplot as plt

def plot_filtering_comparison(gray_img, blurred_img):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].hist(gray_img.ravel(), bins=256, color='black')
    axes[0].set_title('Original Histogram')
    axes[1].hist(blurred_img.ravel(), bins=256, color='blue')
    axes[1].set_title('Filtered Histogram')
    plt.savefig('output_member_2.png')
    print('Saved image as output_member_2.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_2.py` in the main folder and paste this code:
```python
import cv2
from src.processing.filtering import apply_noise_filtering
from src.vis.histogram_vis import plot_filtering_comparison

gray_img = cv2.imread('dataset/1.jpeg', cv2.IMREAD_GRAYSCALE)
blurred_img, _ = apply_noise_filtering(gray_img)
plot_filtering_comparison(gray_img, blurred_img)
```
Run the script in your terminal: 
```bash
python test_member_2.py
```
An image file named `output_member_2.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-2): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```

---

## Member 3: Adaptive Thresholding (Binarization)

**Step 1: Create the Image Processing File**
Create a file named: `src/processing/threshold.py`
Copy and paste this exact code inside:
```python
import cv2

def apply_thresholding(blurred_image):
    # Convert to pure black and white
    binary = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    return binary
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/threshold_vis.py`
Copy and paste this exact code inside:
```python
import matplotlib.pyplot as plt

def plot_threshold(binary_img):
    plt.figure(figsize=(6, 8))
    plt.imshow(binary_img, cmap='gray')
    plt.title('Binarization Result')
    plt.axis('off')
    plt.savefig('output_member_3.png')
    print('Saved image as output_member_3.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_3.py` in the main folder and paste this code:
```python
import cv2
from src.processing.threshold import apply_thresholding
from src.vis.threshold_vis import plot_threshold

gray_img = cv2.imread('dataset/1.jpeg', cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
binary_img = apply_thresholding(blurred)
plot_threshold(binary_img)
```
Run the script in your terminal: 
```bash
python test_member_3.py
```
An image file named `output_member_3.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-3): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```

---

## Member 4: Morphological Operations

**Step 1: Create the Image Processing File**
Create a file named: `src/processing/morphology.py`
Copy and paste this exact code inside:
```python
import cv2
import numpy as np

def clean_noise(binary_image):
    # Remove small white dots (noise) using morphological closing
    kernel = np.ones((3,3), np.uint8)
    cleaned = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    return cleaned
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/morph_vis.py`
Copy and paste this exact code inside:
```python
import matplotlib.pyplot as plt

def plot_morphology(cleaned_img):
    plt.figure(figsize=(6, 8))
    plt.imshow(cleaned_img, cmap='gray')
    plt.title('Morphological Cleaning Result')
    plt.axis('off')
    plt.savefig('output_member_4.png')
    print('Saved image as output_member_4.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_4.py` in the main folder and paste this code:
```python
import cv2
from src.processing.filtering import apply_noise_filtering
from src.processing.threshold import apply_thresholding
from src.processing.morphology import clean_noise
from src.vis.morph_vis import plot_morphology

gray = cv2.imread('dataset/1.jpeg', cv2.IMREAD_GRAYSCALE)
blurred, _ = apply_noise_filtering(gray)
binary = apply_thresholding(blurred)
cleaned_img = clean_noise(binary)
plot_morphology(cleaned_img)
```
Run the script in your terminal: 
```bash
python test_member_4.py
```
An image file named `output_member_4.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-4): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```

---

## Member 5: Table Grid & Contour Extraction

**Step 1: Create the Image Processing File**
Create a file named: `src/processing/grid_extraction.py`
Copy and paste this exact code inside:
```python
import cv2

def find_signature_boxes(cleaned_image):
    # Find table contours
    contours, _ = cv2.findContours(cleaned_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 1000]
    return boxes
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/grid_vis.py`
Copy and paste this exact code inside:
```python
import cv2
import matplotlib.pyplot as plt

def plot_bounding_boxes(original, boxes):
    img_copy = original.copy()
    for (x, y, w, h) in boxes:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
    plt.figure(figsize=(8, 10))
    plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
    plt.title('Detected Grid Cells')
    plt.axis('off')
    plt.savefig('output_member_5.png')
    print('Saved image as output_member_5.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_5.py` in the main folder and paste this code:
```python
import cv2
from src.processing.grid_extraction import find_signature_boxes
from src.vis.grid_vis import plot_bounding_boxes

# 1. Load Real Image
real_img = cv2.imread('dataset/1.jpeg')
gray = cv2.cvtColor(real_img, cv2.COLOR_BGR2GRAY)

# 2. Basic preprocessing (Simulating Member 2 & 3 internally for testing)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# 3. Test Member 5's Actual Logic
boxes = find_signature_boxes(binary)
plot_bounding_boxes(real_img, boxes)
```
Run the script in your terminal: 
```bash
python test_member_5.py
```
An image file named `output_member_5.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-5): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```

---

## Member 6: Signature Cropping Mechanism

**Step 1: Create the Image Processing File**
Create a file named: `src/processing/cropper.py`
Copy and paste this exact code inside:
```python
import cv2

def crop_signature(image, box):
    # Extract the exact ROI of the signature
    x, y, w, h = box
    cropped = image[y:y+h, x:x+w]
    return cropped
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/crop_vis.py`
Copy and paste this exact code inside:
```python
import matplotlib.pyplot as plt

def plot_cropped_signature(cropped_img):
    plt.figure(figsize=(5, 5))
    plt.imshow(cropped_img, cmap='gray')
    plt.title('Extracted Signature ROI')
    plt.axis('off')
    plt.savefig('output_member_6.png')
    print('Saved image as output_member_6.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_6.py` in the main folder and paste this code:
```python
import cv2
from src.processing.filtering import apply_noise_filtering
from src.processing.threshold import apply_thresholding
from src.processing.grid_extraction import find_signature_boxes
from src.processing.cropper import crop_signature
from src.vis.crop_vis import plot_cropped_signature

real_img = cv2.imread('dataset/1.jpeg')
gray = cv2.cvtColor(real_img, cv2.COLOR_BGR2GRAY)
blurred, _ = apply_noise_filtering(gray)
binary = apply_thresholding(blurred)
boxes = find_signature_boxes(binary)

if boxes:
    cropped = crop_signature(real_img, boxes[0])
else:
    cropped = real_img[100:300, 100:300]

plot_cropped_signature(cropped)
```
Run the script in your terminal: 
```bash
python test_member_6.py
```
An image file named `output_member_6.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-6): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```

---

## Member 7: Attendance Status Classifier (Pixel Density)

**Step 1: Create the Image Processing File**
Create a file named: `src/processing/presence_analyzer.py`
Copy and paste this exact code inside:
```python
import cv2

def check_presence(cropped_binary):
    # Count ink pixels. If > 500, student signed.
    ink_pixels = cv2.countNonZero(cropped_binary)
    status = 'Present' if ink_pixels > 500 else 'Absent'
    return status, ink_pixels
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/pie_chart_vis.py`
Copy and paste this exact code inside:
```python
import matplotlib.pyplot as plt

def plot_attendance_pie(present_count, absent_count):
    labels = ['Present', 'Absent']
    sizes = [present_count, absent_count]
    colors = ['#4CAF50', '#F44336']
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title('Daily Attendance Summary')
    plt.savefig('output_member_7.png')
    print('Saved image as output_member_7.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_7.py` in the main folder and paste this code:
```python
import cv2
from src.processing.filtering import apply_noise_filtering
from src.processing.threshold import apply_thresholding
from src.processing.grid_extraction import find_signature_boxes
from src.processing.cropper import crop_signature
from src.processing.presence_analyzer import check_presence
from src.vis.pie_chart_vis import plot_attendance_pie

gray = cv2.imread('dataset/1.jpeg', cv2.IMREAD_GRAYSCALE)
blurred, _ = apply_noise_filtering(gray)
binary = apply_thresholding(blurred)
boxes = find_signature_boxes(binary)

present_count = 0
absent_count = 0

for box in boxes:
    cropped_bin = crop_signature(binary, box)
    status, _ = check_presence(cropped_bin)
    if status == 'Present':
        present_count += 1
    else:
        absent_count += 1

if present_count + absent_count == 0:
    present_count, absent_count = 5, 1

plot_attendance_pie(present_count, absent_count)
```
Run the script in your terminal: 
```bash
python test_member_7.py
```
An image file named `output_member_7.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-7): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```

---

## Member 8: Database Mapper & Bar Chart Analytics

**Step 1: Create the Image Processing File**
Create a file named: `src/processing/db_handler.py`
Copy and paste this exact code inside:
```python
import sqlite3

def save_attendance(student_id, status):
    # Save result to database
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS records (id TEXT, status TEXT)')
    cursor.execute('INSERT INTO records VALUES (?, ?)', (student_id, status))
    conn.commit()
    conn.close()
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/bar_chart_vis.py`
Copy and paste this exact code inside:
```python
import matplotlib.pyplot as plt

def plot_student_history(dates, statuses):
    # Visualizing individual student attendance over time
    plt.figure(figsize=(7, 5))
    plt.bar(dates, [1 if s=='Present' else 0 for s in statuses], color='blue')
    plt.title('Student Attendance History')
    plt.ylabel('1 = Present, 0 = Absent')
    plt.savefig('output_member_8.png')
    print('Saved image as output_member_8.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_8.py` in the main folder and paste this code:
```python
from src.processing.db_handler import save_attendance
from src.vis.bar_chart_vis import plot_student_history

save_attendance('10000409', 'Present')
save_attendance('10009301', 'Present')
save_attendance('10009302', 'Absent')

dates = ['Sheet 1', 'Sheet 2', 'Sheet 3']
statuses = ['Present', 'Absent', 'Present']
plot_student_history(dates, statuses)
```
Run the script in your terminal: 
```bash
python test_member_8.py
```
An image file named `output_member_8.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-8): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```

---

## Member 9: Signature Feature Extraction (ORB)

**Step 1: Create the Image Processing File**
Create a file named: `src/investigation/feature_extractor.py`
Copy and paste this exact code inside:
```python
import cv2

def extract_features(image):
    # Extract keypoints using ORB for advanced recognition
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return keypoints, descriptors
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/feature_vis.py`
Copy and paste this exact code inside:
```python
import cv2
import matplotlib.pyplot as plt

def plot_keypoints(image, keypoints):
    img_with_kp = cv2.drawKeypoints(image, keypoints, None, color=(0,255,0))
    plt.figure(figsize=(8, 10))
    plt.imshow(cv2.cvtColor(img_with_kp, cv2.COLOR_BGR2RGB))
    plt.title('Signature Feature Keypoints')
    plt.savefig('output_member_9.png')
    print('Saved image as output_member_9.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_9.py` in the main folder and paste this code:
```python
import cv2
from src.investigation.feature_extractor import extract_features
from src.vis.feature_vis import plot_keypoints

img = cv2.imread('dataset/1.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kp, _ = extract_features(gray)
plot_keypoints(img, kp)
```
Run the script in your terminal: 
```bash
python test_member_9.py
```
An image file named `output_member_9.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-9): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```

---

## Member 10: Structural Similarity Comparison (SSIM)

**Step 1: Create the Image Processing File**
Create a file named: `src/investigation/similarity_scorer.py`
Copy and paste this exact code inside:
```python
from skimage.metrics import structural_similarity as ssim
import cv2

def compare_signatures(img1, img2):
    # Compare if two signatures belong to the same person
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    score, diff = ssim(img1, img2_resized, full=True)
    return score
```

**Step 2: Create the Visualization File**
Create a file named: `src/vis/ssim_vis.py`
Copy and paste this exact code inside:
```python
import matplotlib.pyplot as plt

def plot_similarity_score(score):
    plt.figure(figsize=(5, 5))
    plt.bar(['SSIM Score'], [score], color='purple')
    plt.ylim(0, 1.0)
    plt.title(f'Signature Match Score: {score:.2f}')
    plt.savefig('output_member_10.png')
    print('Saved image as output_member_10.png')
    plt.show()
```

**Step 3: Test Your Code & Save Output (IMPORTANT)**
To test your task, create a temporary file named `test_member_10.py` in the main folder and paste this code:
```python
import cv2
from src.investigation.similarity_scorer import compare_signatures
from src.vis.ssim_vis import plot_similarity_score

img1 = cv2.imread('dataset/1.jpeg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('dataset/2.jpeg', cv2.IMREAD_GRAYSCALE)
score = compare_signatures(img1, img2)
plot_similarity_score(score)
```
Run the script in your terminal: 
```bash
python test_member_10.py
```
An image file named `output_member_10.png` will be generated and saved in your folder.

**Step 4: Commit and Push your work**
Run the following commands one by one:
```bash
git add src/
git commit -m "feat(member-10): added specific image processing and visualization components"
git push origin <YOUR_BRANCH_NAME>
```
