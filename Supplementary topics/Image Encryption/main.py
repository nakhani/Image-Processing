import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QPalette, QColor, QFont
from PySide6.QtCore import Qt
from encryptor import encrypt_image
from decryptor import decrypt_image

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Encryption and Decryption")
        self.setGeometry(100, 100, 800, 400)

       
        self.enable_dark_mode()

        self.layout = QVBoxLayout()

       
        self.image_layout = QHBoxLayout()
        self.layout.addLayout(self.image_layout)

        
        self.input_layout = QVBoxLayout()
        self.input_label = QLabel("Input Image:")
        self.input_layout.addWidget(self.input_label)
        self.input_image_label = QLabel()
        self.input_layout.addWidget(self.input_image_label)
        self.image_layout.addLayout(self.input_layout)

       
        self.encrypted_layout = QVBoxLayout()
        self.encrypted_image_label = QLabel("Cipher image:")
        self.encrypted_layout.addWidget(self.encrypted_image_label)
        self.encrypted_image_view = QLabel()
        self.encrypted_layout.addWidget(self.encrypted_image_view)
        self.image_layout.addLayout(self.encrypted_layout)

        
        self.decrypted_layout = QVBoxLayout()
        self.decrypted_image_label = QLabel("Decrypted Image:")
        self.decrypted_layout.addWidget(self.decrypted_image_label)
        self.decrypted_image_view = QLabel()
        self.decrypted_layout.addWidget(self.decrypted_image_view)
        self.image_layout.addLayout(self.decrypted_layout)

        self.get_image_button = QPushButton("Select and Process Image")
        self.get_image_button.setStyleSheet("color: black;")  
        self.get_image_button.setFont(QFont("Arial", 10, QFont.Bold))  
        self.get_image_button.clicked.connect(self.select_and_process_image)
        self.layout.addWidget(self.get_image_button)
       

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def enable_dark_mode(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

    def select_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.input_image_label.setPixmap(QPixmap(file_name).scaled(300, 300))
            return file_name
        return None

    def select_and_process_image(self):
        image_path = self.select_image()
        if image_path:
            encrypt_image(image_path)
            self.encrypted_image_view.setPixmap(QPixmap('encrypted_image.bmp').scaled(300, 300))
            decrypt_image('encrypted_image.bmp', 'secret_key.npy')
            self.decrypted_image_view.setPixmap(QPixmap('decrypted_image.jpg').scaled(300, 300))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
