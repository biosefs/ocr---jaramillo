from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QTimer
from PyQt5.QtGui import QPixmap
from ..services.ImageHandler import ImageHandler
from ..workers.ocr_worker import OCRWorker

class OCRController(QObject):
    progress_updated = pyqtSignal(int)
    ocr_completed = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.model = ImageHandler()
        self.worker = None

    def load_image(self, file_path):
        try:
            self.model.load_image(file_path) 
            pixmap = QPixmap(file_path)
            self.view.update_image_display(pixmap)
            self.view.text_edit.clear()
        except Exception as e:
            self.error_occurred.emit(f"Failed to load image: {str(e)}")

    def process_ocr(self):
        if not self.model.image_path:
            self.error_occurred.emit("Please upload or drop an image first.")
            return
        
        self.view.submit_btn.setEnabled(False)
        
        self.worker = OCRWorker(self.model.image_path)
        self.worker.progress_updated.connect(self.progress_updated)
        self.worker.finished.connect(self.handle_ocr_result)
        self.worker.error_occurred.connect(self.error_occurred)
        self.worker.start()

    @pyqtSlot(str)
    def handle_ocr_result(self, text):
        self.ocr_completed.emit(text)
        self.cleanup_worker()

    def cleanup_worker(self):
        if self.worker:
            self.worker.quit()
            self.worker.wait()
            self.worker = None

    def clear_fields(self):
        self.model.clear()
        self.view.text_edit.clear()
        self.view.image_label.setPixmap(QPixmap()) 
        self.view.image_label.setText("Drop Image Here\n\n—or—\n\nClick to Upload")
        self.view.image_label.setProperty("has_image", "false")
        self.view.image_label.style().polish(self.view.image_label)
        self.view.progress_bar.setVisible(False)
        self.view.progress_bar.setValue(0)
        self.view.submit_btn.setEnabled(True)

    def copy_to_clipboard(self):
        from PyQt5.QtWidgets import QApplication
        
        text = self.view.text_edit.toPlainText()
        if text.strip():
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            
            self.view.copy_btn.setText("✓ Copied!")
            QTimer.singleShot(2000, lambda: self.view.copy_btn.setText("Copy to Clipboard"))
            return True
        
        self.error_occurred.emit("No text to copy")
        return False