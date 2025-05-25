import sys
from PyQt5.QtWidgets import QApplication
from app.views.main_window import OCRMainWindow

def main():
    app = QApplication(sys.argv)
    window = OCRMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()