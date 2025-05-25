from PyQt5.QtWidgets import (
    QLabel, QPushButton, QTextEdit, QProgressBar, QSizePolicy
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QDragEnterEvent, QDropEvent


class ClickableLabel(QLabel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent().on_image_label_clicked()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            file_path = urls[0].toLocalFile()
            self.parent().on_image_dropped(file_path)


class OCRTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setFont(QFont("Courier", 10))
        self.setPlaceholderText("Output...")


class OCRProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setValue(0)
        self.setVisible(False)


class ActionButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(40)
        self.setCursor(Qt.PointingHandCursor)