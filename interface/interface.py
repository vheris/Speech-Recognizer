import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt


def load_stylesheet(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speech Recognizer")
        self.resize(400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setSpacing(30)  # Отступ между элементами

        self.label = QLabel("Выберете формат транскрибации:", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем текст

        self.audio_button = QPushButton("Аудио", self)
        self.audio_button.setObjectName("primaryButton")
        
        self.video_button = QPushButton("Видео", self)
        self.video_button.setObjectName("primaryButton")
        
        self.realTime_button = QPushButton("Запись и преобразование в реальном времени", self)
        self.realTime_button.setObjectName("primaryButton")

        layout.addWidget(self.label)
        layout.addWidget(self.audio_button)
        layout.addWidget(self.video_button)
        layout.addWidget(self.realTime_button)
        layout.setAlignment(self.label, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(self.audio_button, Qt.AlignmentFlag.AlignHCenter)
        layout.setAlignment(self.video_button, Qt.AlignmentFlag.AlignHCenter)
        layout.setAlignment(self.realTime_button, Qt.AlignmentFlag.AlignHCenter)
        

        central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    stylesheet = load_stylesheet("styles.qss")
    app.setStyleSheet(stylesheet)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())