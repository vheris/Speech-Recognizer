import sys
from PyQt6.QtWidgets import QApplication
from interface.interface import MainWindow, load_stylesheet

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    stylesheet = load_stylesheet("interface/styles.qss")
    if stylesheet:
        app.setStyleSheet(stylesheet)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())