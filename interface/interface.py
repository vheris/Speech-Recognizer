import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

def load_stylesheet(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: Stylesheet file {file_path} not found")
        return ""
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        return ""

class AudioWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()
        label = QLabel("Интерфейс для работы с аудио")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        
        back_button = QPushButton()
        try:
            back_button.setIcon(QIcon("interface/images/backArr.svg"))
        except:
            back_button.setText("← Назад")
        back_button.setObjectName("backButton")
        back_button.clicked.connect(lambda: main_window.show_page(0))
        
        layout.addWidget(back_button)
        layout.setAlignment(back_button, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)
        self.setLayout(layout)


class VideoWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()
        label = QLabel("Интерфейс для работы с видео")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        
        back_button = QPushButton()
        try:
            back_button.setIcon(QIcon("interface/images/backArr.svg"))
        except:
            back_button.setText("← Назад")
        back_button.setObjectName("backButton")
        back_button.clicked.connect(lambda: main_window.show_page(0))
        
        layout.addWidget(back_button)
        layout.setAlignment(back_button, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)
        self.setLayout(layout)


class RealTimeWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()
        label = QLabel("Интерфейс для записи в реальном времени")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        
        back_button = QPushButton()
        try:
            back_button.setIcon(QIcon("interface/images/backArr.svg"))
        except:
            back_button.setText("← Назад")
        back_button.setObjectName("backButton")
        back_button.clicked.connect(lambda: main_window.show_page(0))
        
        layout.addWidget(back_button)
        layout.setAlignment(back_button, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)
        self.setLayout(layout)


class MenuWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()
        layout.setSpacing(30)

        label = QLabel("Выберите формат транскрибации:")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15)

        audio_button = QPushButton("Аудио")
        audio_button.setObjectName("primaryButton")
        
        video_button = QPushButton("Видео")
        video_button.setObjectName("primaryButton")
        
        realtime_button = QPushButton("Реальное время")
        realtime_button.setObjectName("primaryButton")

        buttons_layout.addWidget(audio_button)
        buttons_layout.addWidget(realtime_button)
        buttons_layout.addWidget(video_button)
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(label)
        layout.setAlignment(label, Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
        
        audio_button.clicked.connect(lambda: main_window.show_page(1))
        video_button.clicked.connect(lambda: main_window.show_page(2))
        realtime_button.clicked.connect(lambda: main_window.show_page(3))



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speech Recognizer")
        self.resize(500, 300)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Страницы интерфейса
        self.stacked_widget.addWidget(MenuWidget(self)) #0
        self.stacked_widget.addWidget(AudioWidget(self)) #1
        self.stacked_widget.addWidget(VideoWidget(self)) #2
        self.stacked_widget.addWidget(RealTimeWidget(self)) #3
    
    def show_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
