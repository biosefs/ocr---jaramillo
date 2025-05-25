DARK_STYLESHEET = """
/* Main application styles */
QWidget {
    background-color: #333446;
    color: #EAEFEF;
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
}

/* Title label */
#titleLabel {
    font-size: 20px; 
    font-weight: bold; 
    color: #EAEFEF;
}

/* Subtitle label */
#subtitleLabel {
    color: #EAEFEF; 
    font-size: 12px; 
    margin-bottom: 10px;
}

/* Image label */
ClickableLabel {
    border: 2px dashed #7F8CAA;
    color: #7F8CAA;
    font-size: 14px;
    padding: 30px;
    background-color: #333446;
    border-radius: 10px;
}

ClickableLabel[has_image="true"] {
    border: 1px solid #7F8CAA;
    background-color: #333446;
}


/* Buttons */
ActionButton {
    padding: 10px;
    border: none;
    border-radius: 8px;
    background-color: #7F8CAA;
    color: #333446;
    font-weight: bold;
}

ActionButton:hover {
    background-color: #B8CFCE;
    color: #333446;
}

/* Text edit */
OCRTextEdit {
    background-color: #333446;
    color: #EAEFEF;
    border-radius: 6px;
    border: 1px solid #7F8CAA;
}

/* Progress bar */
OCRProgressBar {
    background-color: #2E2E3A;
    border: 1px solid #7F8CAA;
    border-radius: 6px;
    text-align: center;
    color: #EAEFEF;
}

OCRProgressBar::chunk {
    background-color: #7F8CAA;
}

/* Message boxes */
QMessageBox {
    background-color: #333446;
    color: #EAEFEF;
}

QMessageBox QLabel {
    color: #EAEFEF;
}
"""