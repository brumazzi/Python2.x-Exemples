#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import PySide
from PySide.QtGui import *

class MainFrame(QWidget):

    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        #self.setGeometry(0,0,640,480)
        #self.setWindowTitle("Main Frame")
        print "sdasd"

app = QApplication(sys.argv)

f = MainFrame()#QMainWindow()
#f.setGeometry(0,0,640,480)
f.show()

sys.exit(app.exec_())
