from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
import sys
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Open File"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()


        self.btn = QPushButton("Upload Signature Sign")
        self.btn.clicked.connect(self.getImage)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        self.show()
    
        self.label = QLabel("Your Image will be displayed here.")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        vbox.addWidget(self.label)
        
        self.btn1 = QPushButton("Process")

        self.btn1.clicked.connect(self.process)
        vbox.addWidget(self.btn1)

        vbox.addLayout(hbox)

        self.label2 = QLabel("REAL")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(self.label2)

        self.label3 = QLabel("FORGE")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(self.label3)


    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.jpg *.png *.jpeg)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        pixmap2 = pixmap.scaled(512, 512, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(QPixmap(pixmap2))
        self.resize(pixmap2.width(), pixmap2.height())

    def process():
        return



App = QApplication(sys.argv)
App.setStyleSheet("QLabel{font-size: 18pt; font-weight:800;} QPushButton{font-size: 12pt; font-weight:500;}")
window = Window()
sys.exit(App.exec())