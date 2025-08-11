import sys
import os

from PyQt6.QtWidgets import (QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
QWidget, QStackedWidget, QButtonGroup, QRadioButton, QSizePolicy, QFileDialog)
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
        self.current_file_path = None
        
        self.back_button = self.create_back_button()
        self.label = self.create_audio_label()
        self.format_buttons = self.create_format_buttons()
        
        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.setAlignment(self.back_button, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.label)
        layout.setAlignment(self.label, Qt.AlignmentFlag.AlignHCenter)
        
        layout.addStretch()
        
        radio_layout = QHBoxLayout()
        radio_layout.addStretch() 
        
        for btn in self.format_buttons:
            radio_layout.addWidget(btn)
        
        radio_layout.addStretch()
        
        layout.addLayout(radio_layout)
        
        # Кнопка загрузки файла
        upload_button = QPushButton("Загрузить аудиофайл")
        upload_button.setObjectName("uploadButton")
        upload_button.clicked.connect(self.upload_file)
        
        layout.addWidget(upload_button)
        layout.setAlignment(upload_button, Qt.AlignmentFlag.AlignHCenter)
        
        # Лейбл для отображения названия файла
        self.file_label = QLabel("Файл не выбран")
        self.file_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.file_label.setObjectName("fileLabel")
        layout.addWidget(self.file_label)
        
        layout.addStretch()
        
        self.setLayout(layout)
    
    def create_back_button(self):
        button = QPushButton()
        try:
            button.setIcon(QIcon("interface/images/backArr.svg"))
        except:
            button.setText("← Назад")
        button.setObjectName("backButton")
        button.clicked.connect(lambda: self.main_window.show_page(0))
        return button
    
    def create_audio_label(self):
        label = QLabel("Интерфейс для работы с аудио")
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        return label
    
    def create_format_buttons(self):
        variables = ["Таймкоды", "Без таймкодов", "Субтитры"]
        buttons = []
        
        self.button_group = QButtonGroup()
        
        for i, fmt in enumerate(variables):
            btn = QRadioButton(fmt)
            if i == 0:
                btn.setChecked(True)
            self.button_group.addButton(btn, i)
            buttons.append(btn)
        
        return buttons
    
    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите аудиофайл",
            "",
            "Audio Files (*.mp3 *.wav *.flac *.aac *.ogg *.m4a *.wma *.aiff);;All Files (*)",
            options = QFileDialog.Option(0)
        )
        if file_path:
            if not os.access(file_path, os.R_OK) and not (os.path.exists(file_path)):
                self.file_label.setText("Ошибка доступа!")
                return
            audio_formats = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.aiff')
            if not file_path.lower().endswith(audio_formats):
                self.file_label.setText("Неверный формат файла!")
                return
            self.current_file_path = file_path
            file_name = os.path.basename(file_path)
            self.file_label.setText(f"Выбран: {file_name}") 


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
