# coding:utf-8
import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from UI import Uniform_ui, MainWindow
from Action import MainWindow_dialog

class Uniform_dialog(QDialog):
    def __init__(self):
        #self.ui = MainWindow_dialog.MainWindow.MainUi()
        self.setAction()


    def setAction(self):
        self.ui.right_widget21.setVisible(False)
        self.ui.right_widget22.setVisible(False)
        self.ui.right_widget23.setVisible(False)
        self.ui.right_widget24.setVisible(False)
        self.ui.right_widget25.setVisible(False)
