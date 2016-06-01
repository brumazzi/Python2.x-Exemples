#!/usr/bin/python
# -*- coding: utf-8 -*-

# simple.py

import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
#wid.resize(250, 150)
wid.setGeometry(10,800,800,600)
wid.setWindowTitle('Simple')
wid.show()

sys.exit(app.exec_())

