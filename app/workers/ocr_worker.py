from PyQt5.QtCore import QThread, pyqtSignal
from PIL import Image
import pytesseract


class OCRWorker(QThread):
    """Worker thread for performing OCR operations."""
    
    progress_updated = pyqtSignal(int)
    finished = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

    def run(self):
        """Perform OCR processing."""
        try:
            self.progress_updated.emit(10)
            image = Image.open(self.image_path).convert("L")
            self.progress_updated.emit(30)
            
            for i in range(30, 90, 10):
                self.progress_updated.emit(i)
                self.msleep(100)
            
            text = pytesseract.image_to_string(image)
            self.progress_updated.emit(100)
            self.finished.emit(text)
        except Exception as e:
            self.error_occurred.emit(str(e))