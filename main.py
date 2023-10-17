import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox
from PyQt5.QtGui import QPixmap

memes = [
    {"name": "Meme1", "category": "Category1", "image_path": "memes/img.jpg"},
    {"name": "Meme2", "category": "Category1", "image_path": "memes/img.png"},
    {"name": "Meme3", "category": "Category2", "image_path": "memes/даун 1000%.png"},
    {"name": "Meme4", "category": "Category2", "image_path": "memes/img2.jfif"},
]

class RandomMemeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Випадкові Меми")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.meme_name_label = QLabel(self)
        self.meme_category_label = QLabel(self)
        self.meme_image_label = QLabel(self)

        self.random_meme_button = QPushButton("Випадковий мем")
        self.random_meme_button.clicked.connect(self.show_random_meme)

        self.category_combobox = QComboBox(self)
        self.category_combobox.addItem("Всі категорії")  # Добавляем опцию для отображения всех мемов
        self.category_combobox.addItems(set(meme["category"] for meme in memes))
        self.category_combobox.currentIndexChanged.connect(self.filter_memes_by_category)

        self.layout.addWidget(self.meme_name_label)
        self.layout.addWidget(self.meme_category_label)
        self.layout.addWidget(self.meme_image_label)
        self.layout.addWidget(self.random_meme_button)
        self.layout.addWidget(self.category_combobox)

        self.selected_category = None
        self.show_random_meme()

    def show_random_meme(self):
        if self.selected_category is not None:
            if self.selected_category == "Всі категорії":
                filtered_memes = memes
            else:
                filtered_memes = [meme for meme in memes if meme["category"] == self.selected_category]
        else:
            random_meme = random.choice(memes)
            self.meme_name_label.setText(random_meme["name"])
            self.meme_category_label.setText(random_meme["category"])
            pixmap = QPixmap(random_meme["image_path"])
            self.meme_image_label.setPixmap(pixmap)
            return

        if filtered_memes:
            random_meme = random.choice(filtered_memes)
            self.meme_name_label.setText(random_meme["name"])
            self.meme_category_label.setText(random_meme["category"])
            pixmap = QPixmap(random_meme["image_path"])
            self.meme_image_label.setPixmap(pixmap)
        else:
            self.meme_name_label.setText("Мемів з даною категорією не знайдено")

    def filter_memes_by_category(self):
        self.selected_category = self.category_combobox.currentText()
        self.show_random_meme()

app = QApplication(sys.argv)
window = RandomMemeApp()
window.show()
sys.exit(app.exec_())
