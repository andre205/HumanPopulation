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

import lotkavolterramodel as lvm

class Window(QMainWindow):
    resized = pyqtSignal()
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(800, 300, 900, 500)
        self.setWindowTitle('Population Simulator 1.0')
        self.init_ui()

    def init_ui(self):
        boldFont = QFont()
        boldFont.setBold(True)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.pop_img = QLabel(self)
        self.update_pop_img()
        self.pop_img.move(20,10)

        self.top_label = QLabel('EQUATION', self)
        self.top_label.setFont(boldFont)
        self.top_label.resize(150, 10)
        self.top_label.move(700, 50)

        self.eq_label = QLabel('dx/dt = ax - pxy', self)
        self.eq_label.setFont(boldFont)
        self.eq_label.resize(200, 30)
        self.eq_label.move(700, 70)

        self.eq_label2 = QLabel('dy/dt = -by + qxy', self)
        self.eq_label2.setFont(boldFont)
        self.eq_label2.resize(200, 30)
        self.eq_label2.move(700, 90)

        self.tbx_a = QLineEdit(self)
        self.tbx_a.resize(100,30)
        self.tbx_a.move(750, 120)
        self.tbx_a.setText("15")

        self.tbx_p = QLineEdit(self)
        self.tbx_p.resize(100,30)
        self.tbx_p.move(750, 160)
        self.tbx_p.setText(".2")

        self.tbx_b = QLineEdit(self)
        self.tbx_b.resize(100,30)
        self.tbx_b.move(750, 200)
        self.tbx_b.setText("10")

        self.tbx_q = QLineEdit(self)
        self.tbx_q.resize(100,30)
        self.tbx_q.move(750, 240)
        self.tbx_q.setText(".5")

        self.tbx_x = QLineEdit(self)
        self.tbx_x.resize(100,30)
        self.tbx_x.move(750, 300)
        self.tbx_x.setText("25")

        self.tbx_y = QLineEdit(self)
        self.tbx_y.resize(100,30)
        self.tbx_y.move(750, 340)
        self.tbx_y.setText("35")

        self.tbx_t = QLineEdit(self)
        self.tbx_t.resize(100,30)
        self.tbx_t.move(750, 380)
        self.tbx_t.setText("5")

        self.label_a = QLabel('a:', self)
        self.label_a.setFont(boldFont)
        self.label_a.resize(200, 30)
        self.label_a.move(700, 120)

        self.label_p = QLabel('p:', self)
        self.label_p.setFont(boldFont)
        self.label_p.resize(200, 30)
        self.label_p.move(700, 160)

        self.label_b = QLabel('b:', self)
        self.label_b.setFont(boldFont)
        self.label_b.resize(200, 30)
        self.label_b.move(700, 200)

        self.label_q = QLabel('q:', self)
        self.label_q.setFont(boldFont)
        self.label_q.resize(200, 30)
        self.label_q.move(700, 240)

        self.label_x = QLabel('X0:', self)
        self.label_x.setFont(boldFont)
        self.label_x.resize(200, 30)
        self.label_x.move(700, 300)

        self.label_y = QLabel('Y0:', self)
        self.label_y.setFont(boldFont)
        self.label_y.resize(200, 30)
        self.label_y.move(700, 340)

        self.label_t = QLabel('t:', self)
        self.label_t.setFont(boldFont)
        self.label_t.resize(200, 30)
        self.label_t.move(700, 380)

        self.start_button = QPushButton('START', self)
        self.start_button.move(650, 450)
        self.start_button.clicked.connect(self.start)

        self.reset_button = QPushButton('RESET', self)
        self.reset_button.move(775, 450)
        self.reset_button.clicked.connect(self.reset)

        self.show()


    def start(self, event):
        try:
            user_x0 = float(self.tbx_x.text())
            user_y0 = float(self.tbx_y.text())
            user_a = float(self.tbx_a.text())
            user_b = float(self.tbx_b.text())
            user_p = float(self.tbx_p.text())
            user_q = float(self.tbx_q.text())
            user_t = float(self.tbx_t.text())
        except:
            user_x0 = 10
            user_y0 = 15
            user_a = 20
            user_b = 25
            user_p = .5
            user_q = .15
            user_t = 20

        # lvm.lv_plot(a,p,b,q,X,Y,t0,tf,tdi)
        lvm.lv_plot(user_a,user_p,user_b,user_q,user_x0,user_y0,0,user_t,1000)

        update_image(self)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)

    def reset(self, event):
        image_filepath = 'img/white.png'
        self.pixmap = QPixmap(image_filepath)
        self.pop_img.setPixmap(self.pixmap)
        self.pop_img.resize(600,500)
        

    def update_pop_img(self):
        image_filepath = 'img/lvimg.png'
        self.pixmap = QPixmap(image_filepath)
        self.pop_img.setPixmap(self.pixmap)
        self.pop_img.resize(600,500)

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


def update_image(self):
    image_filepath = 'img/lvimg.png'
    self.pixmap = QPixmap(image_filepath)
    #self.pixmap = self.pixmap.scaled(450, 450)
    self.pop_img.setPixmap(self.pixmap)
    # self.pop_img.scaledToWidth(200)

# # function that returns dy/dt
def model(y,t):
    k = 1
    dydt = k * (1-(y/1000)) * y
    return dydt

if __name__ == '__main__':
    run()
