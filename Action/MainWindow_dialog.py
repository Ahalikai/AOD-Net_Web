# coding:utf-8
import sys
import  numpy as np
import  pyperclip
import qtawesome
import os
from PIL import Image
import cv2
from Algorithm import dehaze, PicSimilar

from PyQt5 import QtCore,QtGui,QtWidgets
#from UI import MainWindow, Uniform_ui, orthogonal_dialog_ui, evolution_dialog_ui
from UI import MainWindow
#from Action import Uniform_dialog, Orthogonal_dialog, Evolution_dialog

from PyQt5.QtGui import  *
from PyQt5.QtCore import  *
from PyQt5.QtWidgets import *

class MainWindow_dialog(QDialog):

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        QDialog.__init__(self)
        self.ui = MainWindow.MainUi()
        self.ui.show()
        self.setAction()
        sys.exit(app.exec_())

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "้ๅๆไปถ", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        print(fileName)
        #print(fileType)
        return fileName


    def setAction(self):
        self.ui.left_button_1.clicked.connect(self.button_1_Change)
        self.ui.left_button_2.clicked.connect(self.button_2_Change)
        self.ui.left_button_3.clicked.connect(self.button_3_Change)
        self.ui.left_button_4.clicked.connect(self.button_4_Change)
        self.ui.left_button_5.clicked.connect(self.button_5_Change)

        #self.ui.right_button_1.clicked.connect(self.button_5_Change)
        self.ui.right_button_2.clicked.connect(self.button_5_Change)
        self.ui.right_button_3.clicked.connect(self.button_5_Change)
        self.ui.right_button_4.clicked.connect(self.button_5_Change)
        self.ui.right_button_5.clicked.connect(self.button_5_Change)

        #pass
    def button_1_Orthogonal(self):
        self.open_file()
        #pass
        #Orthogonal_dialog.Orthogonal_dialog(self).exec_()


    def button_1_openfile(self):
        image_path1 = self.open_file()
        image_path2 = dehaze.dehaze.dehaze_image(image_path1)
        print("hello")
        self.ui.right_button_22.setPixmap(QtGui.QPixmap(image_path1))
        self.ui.right_button_222.setPixmap(QtGui.QPixmap(image_path2))
        similar = PicSimilar.similar(image_path1, image_path2)
        print('%.2f%%' % (similar * 100) )

        result_z = " "
        if(similar > 0.1):
            result_z = result_z + "ๆต้พ"
        elif(similar > 0.02):
            result_z = result_z + "่ฝป้พ"
        else:
            result_z = result_z + "ๆ?้พ"

        #result_z = result_z + ' (็ธไผผๅบฆ๏ผ' + similar + ')\n'
        result_z = result_z + "(STD๏ผ" + (str)( '%.2f%%' % (similar * 100) ) + ")\n"
        print(result_z)
        self.ui.right_button_221.setText(result_z)
        self.setAction()



    def button_2_Uniform(self):
        pass
        #Uniform_dialog.Uniform_dialog().exec_()

    def button_1_Change(self):
        self.buttonChange(1)
        self.setAction()

    def button_2_Change(self):
        self.buttonChange(2)

        self.ui.right_label_1.setText("ๅบ็ก่ฎพ่ฎก")
        self.ui.right_label_2.setText("ๅๅบ้ข่ฎพ่ฎก")

        # self.right_button_22.setScaledContents (True) # ่ฎฉๅพ็่ช้ๅบlabelๅคงๅฐ
        # ่ฐ็จQtGui.QPixmapๆนๆณ๏ผๆๅผไธไธชๅพ็๏ผๅญๆพๅจๅ้pngไธญ
        # ๅจl1้้ข๏ผ่ฐ็จsetPixmapๅฝไปค๏ผๅปบ็ซไธไธชๅพๅๅญๆพๆก๏ผๅนถๅฐไนๅ็ๅพๅpngๅญๆพๅจ่ฟไธชๆกๆก้ใ
        self.ui.right_button_21.setText("ๆญฃไบค่ฎพ่ฎก")
        self.ui.right_button_22.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_23.setText("Orthogonal experimental")

        self.ui.right_button_221.setText("ๅๅ่ฎพ่ฎก")
        self.ui.right_button_222.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_223.setText("Uniform experimental") #

        self.ui.right_button_321.setText("ๆไธๆน่ฎพ่ฎก")
        self.ui.right_button_322.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_323.setText("Latin square design")  #
        self.ui.right_layout2.addWidget(self.ui.right_widget23, 2, 0, 2, 2)  # ๅทฆไพง้จไปถๅจ็ฌฌ2่ก็ฌฌ0ๅ๏ผๅ?2่ก9ๅ

        self.ui.right_button_421.setText("ไธญๅฟๅคๅ่ฎพ่ฎก")
        self.ui.right_button_422.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_423.setText("Center composite design")  #
        self.ui.right_layout4.addWidget(self.ui.right_widget24, 0, 0, 2, 2)


        self.ui.right_button_521.setText("Box-Benhnken่ฎพ่ฎก")
        self.ui.right_button_522.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_523.setText("Box-Behnken Design")  #
        self.ui.right_layout4.addWidget(self.ui.right_widget25, 0, 2, 2, 2)

        self.ui.right_button_1.clicked.connect(self.button_1_Orthogonal)
        self.ui.right_button_2.clicked.connect(self.button_2_Uniform)

        self.setAction()

    def button_3_Change(self):
        self.buttonChange(3)
        #self.ui.right_widget21.setVisible(False)
        #self.ui.right_widget22.setVisible(False)
        self.ui.right_widget23.setVisible(False)
        self.ui.right_widget24.setVisible(False)
        self.ui.right_widget25.setVisible(False)

        self.ui.right_label_1.setText("ๅบไบAOD-Net็ไบค้้่ทฏๅพๅๅคงๆฐ่ฝ่งๅบฆๆฃๆตๆนๆณ็?็ฉถ")
        self.ui.right_label_2.setText("")


        self.ui.right_button_21.setText("้ๅๅพๅ\n")
        self.ui.right_button_22.setPixmap(QtGui.QPixmap("pic\\CNN\\demo_test.jpg"))
        self.ui.right_button_23.setText("\nๅๅงๅพๅ")

        self.ui.right_button_221.setText("่ฝป้พ (STD๏ผ5.02%)\n")
        self.ui.right_button_222.setPixmap(QtGui.QPixmap("pic\\CNN\\demo_result.png"))
        self.ui.right_button_223.setText("\nๅฏนๆฏๅพๅ")  #

        self.ui.right_button_1.clicked.connect(self.button_1_openfile)
        #Evolution_dialog.Evolution_dialog().exec_()
        self.setAction()

    def button_4_Change(self):
        self.buttonChange(4)
        self.ui.right_label_1.setText("ๅบ็ก่ฎพ่ฎก")
        self.ui.right_label_2.setText("็ธๅณไธๅๅฝ")

        self.ui.right_button_21.setText("ๆญฃไบคๅฎ้ชๆนๅทฎๅๆ")
        self.ui.right_button_22.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_23.setText("Orthogonal analysis of variance")

        self.ui.right_button_221.setText("้ๅๆฐ็ป่ฎก")
        self.ui.right_button_222.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_223.setText("Nonparametric statistics")  #
        self.ui.right_widget23.setVisible(False)
        self.ui.right_button_421.setText("็ธๅณๅๆ")
        self.ui.right_button_422.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_423.setText("Correlation analysis")  #
        self.ui.right_layout4.addWidget(self.ui.right_widget24, 0, 0, 2, 2)

        self.ui.right_button_521.setText("ไธๅ็บฟๆงๅๅฝ")
        self.ui.right_button_522.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_523.setText("Unary linear regression")  #
        self.ui.right_layout4.addWidget(self.ui.right_widget25, 0, 2, 2, 2)
        self.setAction()

    def button_5_Change(self):
        self.buttonChange(5)
        self.ui.right_widget21.setVisible(False)
        self.ui.right_widget22.setVisible(False)
        self.ui.right_widget23.setVisible(False)
        self.ui.right_widget24.setVisible(False)
        self.ui.right_widget25.setVisible(False)
        self.ui.right_label_1.setText(" ")
        self.ui.right_label_2.setText("ๅฆ้ๅธฎๅฉ/ๅ้ฆ๏ผ่ฏท่็ณปAha15380251715@gmail.comใ")

        self.setAction()

    def buttonChange(self,i):
        self.ui.right_widget21.setVisible(False)
        self.ui.right_widget22.setVisible(False)
        self.ui.right_widget23.setVisible(False)
        self.ui.right_widget24.setVisible(False)
        self.ui.right_widget25.setVisible(False)
        self.ui.init_ui()

        self.ui.left_button_1.setStyleSheet(
            '''
            QPushButton:hover{background:#f2f2f2;}
            ''')
        self.ui.left_button_2.setStyleSheet(
            '''
            QPushButton:hover{background:#f2f2f2;}
            ''')
        self.ui.left_button_3.setStyleSheet(
            '''
            QPushButton:hover{background:#f2f2f2;}
            ''')
        self.ui.left_button_4.setStyleSheet(
            '''
            QPushButton:hover{background:#f2f2f2;}
            ''')
        self.ui.left_button_5.setStyleSheet(
            '''
            QPushButton:hover{background:#f2f2f2;}
            ''')
        if(i == 1):
            self.ui.left_button_1.setStyleSheet(
            '''
            *{background-color:#e6e6e6;}
            ''')
        elif(i == 2):
            self.ui.left_button_2.setStyleSheet(
            '''
            *{background-color:#e6e6e6;}
            ''')
        elif (i == 3):
            self.ui.left_button_3.setStyleSheet(
            '''
            *{background-color:#e6e6e6;}
            ''')
        elif (i == 4):
            self.ui.left_button_4.setStyleSheet(
            '''
            *{background-color:#e6e6e6;}
            ''')
        elif (i == 5):
            self.ui.left_button_5.setStyleSheet(
            '''
            *{background-color:#e6e6e6;}
            ''')
