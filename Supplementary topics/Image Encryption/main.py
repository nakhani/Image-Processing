import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog
from PySide6.QtGui import QPixmap
from encryptor import encrypt_image
from decryptor import decrypt_image

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Encryption and Decryption")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.input_label = QLabel("Input Image:")
        self.layout.addWidget(self.input_label)

        self.input_image_label = QLabel()
        self.layout.addWidget(self.input_image_label)

        self.encrypt_button = QPushButton("Encrypt Image")
        self.encrypt_button.clicked.connect(self.encrypt_image)
        self.layout.addWidget(self.encrypt_button)

        self.encrypted_image_label = QLabel("Encrypted Image:")
        self.layout.addWidget(self.encrypted_image_label)

        self.encrypted_image_view = QLabel()
        self.layout.addWidget(self.encrypted_image_view)

        self.decrypt_button = QPushButton("Decrypt Image")
        self.decrypt_button.clicked.connect(self.decrypt_image)
        self.layout.addWidget(self.decrypt_button)

        self.decrypted_image_label = QLabel("Decrypted Image:")
        self.layout.addWidget(self.decrypted_image_label)

        self.decrypted_image_view = QLabel()
        self.layout.addWidget(self.decrypted_image_view)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def select_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.input_image_label.setPixmap(QPixmap(file_name).scaled(300, 300))
            return file_name
        return None

    def encrypt_image(self):
        image_path = self.select_image()
        if image_path:
            encrypt_image(image_path, 'encrypted_image.bmp', 'secret_key.npy')
            self.encrypted_image_view.setPixmap(QPixmap('encrypted_image.bmp').scaled(300, 300))

    def decrypt_image(self):
        decrypt_image('encrypted_image.bmp', 'secret_key.npy', 'decrypted_image.jpg')
        self.decrypted_image_view.setPixmap(QPixmap('decrypted_image.jpg').scaled(300, 300))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
