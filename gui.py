import sys
import os
import json
import matplotlib
#import keyboard

from PyQt5.QtCore import QCoreApplication, Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QStyleFactory
from PyQt5.QtWidgets import QAction, QMessageBox, QCheckBox, QProgressBar, QLabel, QComboBox
from PyQt5.QtWidgets import QFileDialog, QLineEdit
from PyQt5.QtCore import pyqtSlot

import cv2
import json
import requests
import numpy as np
import os, sys, time
from shutil import copyfile

from scipy.integrate import odeint
import matplotlib.pyplot as plt


import threading
from threading import Thread

class Window(QMainWindow):
    resized = pyqtSignal()
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 900, 500)
        self.setWindowTitle('Population Simulator 1.0')
        self.init_ui()

    def init_ui(self):
        boldFont = QFont()
        boldFont.setBold(True)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.pop_img = QLabel(self)
        self.update_pop_img()
        self.pop_img.move(20,10)

        self.tbx1 = QLineEdit(self)
        self.tbx1.resize(100,30)
        self.tbx1.move(750, 400)
        self.tbx1.setText("5")

        self.x_label = QLabel('LABEL', self)
        self.x_label.setFont(boldFont)
        self.x_label.resize(150, 10)
        self.x_label.move(700, 400)

        self.start_button = QPushButton('START', self)
        self.start_button.move(650, 450)
        self.start_button.clicked.connect(self.start)

        self.reset_button = QPushButton('STOP', self)
        self.reset_button.move(775, 450)
        self.reset_button.clicked.connect(self.reset)

        self.show()


    def start(self, event):
        try:
            y0 = float(self.tbx1.text())
        except:
            y0 = 1


        t = np.linspace(0,40)
        y = odeint(model,y0,t)

        plt.plot(t,y)
        plt.xlabel('time')
        plt.ylabel('y(t)')

        plt.savefig('out.png')
        update_image(self)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)

    def reset(self, event):
        plt.clf()
        self.update_pop_img()

    def update_pop_img(self):
        image_filepath = 'out_img.png'
        self.pixmap = QPixmap(image_filepath)
        self.pop_img.setPixmap(self.pixmap)
        self.pop_img.resize(600,500)

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


def update_image(self):
    image_filepath = 'out.png'
    self.pixmap = QPixmap(image_filepath)
    #self.pixmap = self.pixmap.scaled(450, 450)
    self.pop_img.setPixmap(self.pixmap)
    # self.pop_img.scaledToWidth(200)

# function that returns dy/dt
def model(y,t):
    k = 1
    dydt = k * (1-(y/1000)) * y
    return dydt

if __name__ == '__main__':
    run()
