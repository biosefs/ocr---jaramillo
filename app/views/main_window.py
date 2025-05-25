from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog, QLabel
)
from PyQt5.QtCore import Qt, QTimer
from .components import (
    ClickableLabel, OCRTextEdit, 
    OCRProgressBar, ActionButton
)
from ..controllers.ocr_controller import OCRController


class OCRMainWindow(QWidget):    
    def __init__(self):
        super().__init__()
        self.controller = OCRController(self)
        self.setup_ui()
        self.connect_signals()
        self.apply_styles()

    def setup_ui(self):
        self.setWindowTitle("OCR - Jaramillo")
        self.setGeometry(100, 100, 900, 520)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        
        self.setup_header(main_layout)
        
        content_layout = QHBoxLayout()
        self.setup_image_column(content_layout)
        self.setup_output_column(content_layout)
        
        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def setup_header(self, layout):
        title = QLabel("OCR Final Project for CSA 105 - Machine Learning")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("titleLabel")
        
        subtitle = QLabel("Jayson Jaramillo  BSCS 3B")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setObjectName("subtitleLabel")
        
        layout.addWidget(title)
        layout.addWidget(subtitle)

    def setup_image_column(self, layout):
        image_column = QVBoxLayout()
        
        self.image_label = ClickableLabel(self)
        self.image_label.setText("Drop Image Here\n\n—or—\n\nClick to Upload")
        image_column.addWidget(self.image_label)
        
        self.setup_image_buttons(image_column)
        
        layout.addLayout(image_column, 1)

    def setup_image_buttons(self, layout):
        button_row = QHBoxLayout()
        
        self.clear_btn = ActionButton("Clear", self)
        self.submit_btn = ActionButton("Submit", self)
        
        button_row.addWidget(self.clear_btn)
        button_row.addWidget(self.submit_btn)
        
        layout.addLayout(button_row)

    def setup_output_column(self, layout):
        output_column = QVBoxLayout()
        
        self.text_edit = OCRTextEdit(self)
        output_column.addWidget(self.text_edit)
        
        self.progress_bar = OCRProgressBar(self)
        output_column.addWidget(self.progress_bar)
        
        self.copy_btn = ActionButton("Copy to Clipboard", self)
        output_column.addWidget(self.copy_btn)
        
        layout.addLayout(output_column, 1)

    def connect_signals(self):
        self.clear_btn.clicked.connect(self.controller.clear_fields)
        self.submit_btn.clicked.connect(self.controller.process_ocr)
        self.copy_btn.clicked.connect(self.controller.copy_to_clipboard)
        self.controller.progress_updated.connect(self.update_progress)
        self.controller.ocr_completed.connect(self.display_ocr_result)
        self.controller.error_occurred.connect(self.display_error) 

    def apply_styles(self):
        from styles.dark_theme import DARK_STYLESHEET
        self.setStyleSheet(DARK_STYLESHEET)

    def on_image_label_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff);;All Files (*)"
        )
        if file_path:
            self.controller.load_image(file_path)

    def on_image_dropped(self, file_path):
        self.controller.load_image(file_path)

    def display_ocr_result(self, text):
        self.text_edit.setPlainText(text)
        self.progress_bar.setVisible(False)
        self.submit_btn.setEnabled(True)

    def display_error(self, error_msg):
        QMessageBox.critical(self, "OCR Error", error_msg)
        self.progress_bar.setVisible(False)
        self.submit_btn.setEnabled(True)

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        if not self.progress_bar.isVisible():
            self.progress_bar.setVisible(True)

    def update_image_display(self, pixmap):
        self.image_label.setPixmap(pixmap.scaled(
            self.image_label.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        ))
        self.image_label.setProperty("has_image", True)
        self.image_label.style().polish(self.image_label)  