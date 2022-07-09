from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
import sys
from PyQt5.QtGui import QPixmap, QFont
import tensorflow as tf
from keras import models, layers
from keras.models import load_model
from keras.utils.generic_utils import get_custom_objects
from keras import backend as K
from PIL import ImageQt
import uuid
import cv2
import numpy as np
import git

def center_normalize(x):
    return (x - K.mean(x)) / K.std(x)

def root_mean_squared_error(y_true, y_pred):
    y_pred = tf.cast(y_pred, tf.float32)
    y_true = tf.cast(y_true, tf.float32)
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1))

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

        self.btnUpload = QPushButton("Upload signature to verify")
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
        self.lblForge.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(self.lblForge)

        self.lblReal = QLabel("REAL")
        self.lblReal.setFont(lblFont)
        self.lblReal.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(self.lblReal)

        self.show()


    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.jpg *.png *.jpeg)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        pixmap_scaled = pixmap.scaled(512, 512, QtCore.Qt.KeepAspectRatio)
        self.lblImage.setPixmap(QPixmap(pixmap_scaled))
        self.lblImage.setStyleSheet('border: 2px solid black; border-radius: 3px;')
        self.lblReal.setStyleSheet('color: black;')
        self.lblForge.setStyleSheet('color: black;')
        self.resize(pixmap_scaled.width(), pixmap_scaled.height())

    def process(self):
        # read and save image
        image = ImageQt.fromqpixmap(self.lblImage.pixmap())
        imageUUID = str(uuid.uuid1()) + '.png'
        image.save('image_t/'+ imageUUID )

        adam = tf.keras.optimizers.Adam(learning_rate=0.0001)
        model = load_model('model.h5', custom_objects={'center_normalize': layers.Activation(center_normalize),'root_mean_squared_error': root_mean_squared_error})
        model.compile(optimizer=adam, loss=root_mean_squared_error, metrics=['accuracy'])

        image_path = repo.working_tree_dir + "\\image_t\\" + imageUUID

        img = cv2.imread(image_path)

        # PREPROCESSING
        #to check for its aspect ratio 
        height, width, channel = img.shape
        if width > height : #landscape
            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # #resize image to 256 x 512
        img = cv2.resize(img,(512, 256))
        img = np.reshape(img,[1,512,256,3])

        predictions = model.predict(img)
        res = (predictions[0][0] + predictions[0][1])/2
        print(res)

        if res > 0.5 :
            result = 1
        else :
            result = 0
        if(result == 1):
            self.lblReal.setStyleSheet('color: black;')
            self.lblForge.setStyleSheet('color: #E83A14;')
        elif(result == 0):
            self.lblForge.setStyleSheet('color: black;')
            self.lblReal.setStyleSheet('color: #5FD068;')

repo = git.Repo('.', search_parent_directories=True)
App = QApplication(sys.argv)
App.setStyleSheet("QLabel{font-size: 18pt; font-weight:800;} QPushButton{font-size: 12pt; font-weight:500; border: 2px solid #6D8B74; border-radius: 5px; background-color: #BDE6F1!important;}")
window = Window()
sys.exit(App.exec())