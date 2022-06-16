from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
import sys
from PyQt5.QtGui import QPixmap, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Signature Verification - Tim Hore"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300


        self.InitWindow()


    def InitWindow(self):
        btnFont = QFont("Georgia")
        lblFont = QFont("Constantia")
        self.setWindowIcon(QtGui.QIcon("assets/icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.btnUpload = QPushButton("Upload Signature Sign")
        self.btnUpload.setFont(btnFont)
        self.btnUpload.clicked.connect(self.getImage)

        vbox.addWidget(self.btnUpload)

        self.setLayout(vbox)
    
        self.lblImage = QLabel("Your Image will be displayed here.")
        self.lblImage.setFont(lblFont)
        self.lblImage.setAlignment(QtCore.Qt.AlignCenter)
        vbox.addWidget(self.lblImage)
        
        self.btnProcess = QPushButton("Process")
        self.btnProcess.setFont(btnFont)
        self.btnProcess.clicked.connect(self.process)
        vbox.addWidget(self.btnProcess)

        vbox.addLayout(hbox)

        self.lblForge = QLabel("FORGE")
        self.lblForge.setFont(lblFont)
        # self.lblForge.setStyleSheet('color: #E83A14;')
        self.lblForge.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(self.lblForge)

        self.lblReal = QLabel("REAL")
        self.lblReal.setFont(lblFont)
        # self.lblReal.setStyleSheet('color: #5FD068;')
        self.lblReal.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(self.lblReal)

        self.show()


    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.jpg *.png *.jpeg)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        pixmap2 = pixmap.scaled(512, 512, QtCore.Qt.KeepAspectRatio)
        self.lblImage.setPixmap(QPixmap(pixmap2))
        self.lblImage.setStyleSheet('border: 2px solid black; border-radius: 3px;')
        self.resize(pixmap2.width(), pixmap2.height())

    def process():
        return



App = QApplication(sys.argv)
App.setStyleSheet("QLabel{font-size: 18pt; font-weight:800;} QPushButton{font-size: 12pt; font-weight:500; border: 2px solid #6D8B74; border-radius: 5px; background-color: #BDE6F1!important;}")
window = Window()
sys.exit(App.exec())