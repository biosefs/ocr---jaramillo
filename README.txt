OCR - Jaramillo

A desktop application for Optical Character Recognition (OCR) built with Python and PyQt5. This project allows users to upload or drag-and-drop images, extract text using Tesseract OCR, and copy the recognized text to the clipboard.

Features
- Modern dark-themed GUI
- Drag-and-drop or click to upload images
- Real-time progress bar during OCR processing
- Copy recognized text to clipboard
- Clear/reset interface easily

Requirements
- Python 3.7+
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Pillow](https://pypi.org/project/Pillow/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (must be installed and in your system PATH)

Installation
1. Clone this repository:
   ```
   git clone https://github.com/biosefs/ocr---jaramillo.git
   cd ocr---jaramillo
   ```

2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - [Download and install Tesseract](https://github.com/tesseract-ocr/tesseract)
   - Make sure `tesseract` is in your system PATH.


Usage

Run the application with:
```
python main.py
```

- Click or drag-and-drop an image to upload.
- Click the Submit buttpon to start OCR.
- Copy the recognized text using the Copy to Clipboard button.
- Use Clear button to reset the interface.


Credits
- Developed by Jayson Jaramillo (BSCS 3B)
- Final Project for CSA 105 - Machine Learning

License
This project is for educational purposes.
