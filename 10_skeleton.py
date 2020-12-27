#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © %YEAR% %USER% <%MAIL%>
#
# Distributed under terms of the %LICENSE% license.
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Window")
        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        pass

App = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(App.exec())

