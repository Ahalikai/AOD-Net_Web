# coding:utf-8

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import *
import sys
import qtawesome
from UI import MainWindow
from Action import MainWindow_dialog
from Algorithm import dehaze

def main():
    #app = QtWidgets.QApplication(sys.argv)
    #gui = MainWindow.MainUi()
    #gui.show()
    MainWindow_dialog.MainWindow_dialog().exec_()
    #sys.exit(app.exec_())

if __name__ == '__main__':
    main()