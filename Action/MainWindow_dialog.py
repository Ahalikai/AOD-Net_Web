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
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
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
            result_z = result_z + "浓雾"
        elif(similar > 0.02):
            result_z = result_z + "轻雾"
        else:
            result_z = result_z + "无雾"

        #result_z = result_z + ' (相似度：' + similar + ')\n'
        result_z = result_z + "(STD：" + (str)( '%.2f%%' % (similar * 100) ) + ")\n"
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

        self.ui.right_label_1.setText("基础设计")
        self.ui.right_label_2.setText("响应面设计")

        # self.right_button_22.setScaledContents (True) # 让图片自适应label大小
        # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.ui.right_button_21.setText("正交设计")
        self.ui.right_button_22.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_23.setText("Orthogonal experimental")

        self.ui.right_button_221.setText("均匀设计")
        self.ui.right_button_222.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_223.setText("Uniform experimental") #

        self.ui.right_button_321.setText("拉丁方设计")
        self.ui.right_button_322.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_323.setText("Latin square design")  #
        self.ui.right_layout2.addWidget(self.ui.right_widget23, 2, 0, 2, 2)  # 左侧部件在第2行第0列，占2行9列

        self.ui.right_button_421.setText("中心复合设计")
        self.ui.right_button_422.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_423.setText("Center composite design")  #
        self.ui.right_layout4.addWidget(self.ui.right_widget24, 0, 0, 2, 2)


        self.ui.right_button_521.setText("Box-Benhnken设计")
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

        self.ui.right_label_1.setText("基于AOD-Net的交通道路图像大气能见度检测方法研究")
        self.ui.right_label_2.setText("")


        self.ui.right_button_21.setText("选取图像\n")
        self.ui.right_button_22.setPixmap(QtGui.QPixmap("pic\\CNN\\demo_test.jpg"))
        self.ui.right_button_23.setText("\n原始图像")

        self.ui.right_button_221.setText("轻雾 (STD：5.02%)\n")
        self.ui.right_button_222.setPixmap(QtGui.QPixmap("pic\\CNN\\demo_result.png"))
        self.ui.right_button_223.setText("\n对比图像")  #

        self.ui.right_button_1.clicked.connect(self.button_1_openfile)
        #Evolution_dialog.Evolution_dialog().exec_()
        self.setAction()

    def button_4_Change(self):
        self.buttonChange(4)
        self.ui.right_label_1.setText("基础设计")
        self.ui.right_label_2.setText("相关与回归")

        self.ui.right_button_21.setText("正交实验方差分析")
        self.ui.right_button_22.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_23.setText("Orthogonal analysis of variance")

        self.ui.right_button_221.setText("非参数统计")
        self.ui.right_button_222.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_223.setText("Nonparametric statistics")  #
        self.ui.right_widget23.setVisible(False)
        self.ui.right_button_421.setText("相关分析")
        self.ui.right_button_422.setPixmap(QtGui.QPixmap(""))
        self.ui.right_button_423.setText("Correlation analysis")  #
        self.ui.right_layout4.addWidget(self.ui.right_widget24, 0, 0, 2, 2)

        self.ui.right_button_521.setText("一元线性回归")
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
        self.ui.right_label_2.setText("如需帮助/反馈，请联系Aha15380251715@gmail.com。")

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
