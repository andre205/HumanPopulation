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

import threading
from threading import Thread

class Window(QMainWindow):
    resized = pyqtSignal()
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 620, 500)
        self.setWindowTitle('Population Simulator 1.0')
        self.init_ui()

    def init_ui(self):
        boldFont = QFont()
        boldFont.setBold(True)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.pop_img = QLabel(self)
        self.update_pop_img()
        self.pop_img.move(100,20)

        self.tbx1 = QLineEdit(self)
        self.tbx1.move(100, 300)
        self.tbx1.resize(100,30)
        self.tbx1.setText("test")

        self.x_label = QLabel('LABEL', self)
        self.x_label.setFont(boldFont)
        self.x_label.resize(150, 10)
        self.x_label.move(20, 310)

        self.start_button = QPushButton('START', self)
        self.start_button.move(100, 450)
        self.start_button.clicked.connect(self.start)

        self.reset_button = QPushButton('STOP', self)
        self.reset_button.move(250, 450)
        self.reset_button.clicked.connect(self.reset)

        self.show()


    def start(self, event):
        x=1
        # tbx1 = self.tbx1.text()
        # tby1 = self.tby1.text()
        # tbx2 = self.tbx2.text()
        # tby2 = self.tby2.text()
        #
        # tbr = self.rgb_r.text()
        # tbg = self.rgb_g.text()
        # tbb = self.rgb_b.text()
        #
        # tbpx = self.px_ct.text()
        #
        # REGION = (int(tbx1), int(tby1), int(tbx2), int(tby2))
        # RGB = [int(tbr), int(tbg), int(tbb)]
        #
        # th = Thread(target = monitor(REGION, RGB, int(tbpx)))
        # th.start()
        # th.join()
        # #monitor(REGION, RGB)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)


    def update_pop_img(self):
        image_filepath = 'out_img.png'
        self.pixmap = QPixmap(image_filepath)
        self.pop_img.setPixmap(self.pixmap)
        self.pop_img.resize(400,200)

    def reset(self, event):
        x=1


def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


# def update_image(REGION):
#     screen =  ImageGrab.grab(bbox=REGION)
#     img_np = np.array(screen.getdata(),dtype='uint8')\
#     .reshape((screen.size[1],screen.size[0],3))
#     img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
#     cv2.imwrite('out_img.png', img_np)
#     cv2.destroyAllWindows()

if __name__ == '__main__':
    run()
