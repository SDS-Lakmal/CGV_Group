# 🎓 Student Attendance Management System (SAMS)

A robust, modular Computer Vision and Digital Image Processing pipeline built with Python and OpenCV. SAMS automates the extraction, processing, classification, and database logging of student attendance records from physical signing sheet photographs.

---

## 📌 Project Overview
Manual attendance tracking is prone to human error and time inefficiency. **SAMS** solves this by:
1. Parsing student metadata from an XML database file (`info.xml`).
2. Processing signing sheet snapshots through sequential image-enhancement algorithms.
3. Isolating tabular grid regions and extracting individual student signature boxes.
4. Evaluating pixel density to classify attendance status (**Present / Absent**).
5. Storing results in an SQLite database and rendering visual analytics.

---

## 📁 Repository & File Architecture

```text
attendance-system/
├── dataset/
│   ├── 1.jpeg ... 5.jpeg         # Physical attendance signing sheet images
│   └── info.xml                 # XML file containing student metadata
├── src/
│   ├── investigation/           # Feature Extraction & Analysis
│   │   └── feature_extractor.py # ORB Keypoint descriptor extraction
│   ├── processing/              # Core DIP Processing Modules
│   │   ├── grayscale.py         # BGR to Grayscale conversion
│   │   ├── filtering.py         # Gaussian noise reduction
│   │   ├── threshold.py         # Adaptive thresholding / binarization
│   │   ├── morphology.py        # Morphological closing operations
│   │   ├── grid_extraction.py   # Table grid contour & bounding box detection
│   │   ├── cropper.py           # Signature ROI array slicing
│   │   ├── presence_analyzer.py # Pixel density calculation & presence classification
│   │   └── db_handler.py        # SQLite database mapping
│   └── vis/                     # Data Visualization Utilities
│       ├── preprocessing_plots.py
│       ├── histogram_vis.py
│       ├── morph_vis.py
│       ├── grid_vis.py
│       ├── crop_vis.py
│       ├── feature_vis.py
│       ├── pie_chart_vis.py
│       ├── bar_chart_vis.py
│       └── ssim_vis.py
├── sams.py                      # Main Command-Line Pipeline Controller
├── requirements.txt             # Project Dependencies
└── README.md                    # System Documentation
