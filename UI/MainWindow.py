# coding:utf-8

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import *
import sys
import qtawesome
from Action import MainWindow_dialog


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)

        self.ui = self.init_ui()  # 窗口的实例化
        #self.ui.setupUi(self)
        #self.init_ui()

    def mousePressEvent(self, event):
        self.pressX = event.x()  # 记录鼠标按下的时候的坐标
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()  # 获取移动后的坐标
        moveX = x - self.pressX
        moveY = y - self.pressY  # 计算移动了多少
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY  # 计算移动后主窗口在桌面的位置
        self.move(positionX, positionY)  # 移动主窗口


    def init_ui(self):
        self.setFixedSize(1200, 720)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.main_layout.setSpacing(0)

        self.top_widget = QtWidgets.QWidget()  # 创建头部部件
        self.top_widget.setObjectName('top_widget')
        self.top_layout = QtWidgets.QGridLayout()  # 创建头部部件的网格布局层
        self.top_widget.setLayout(self.top_layout)  # 设置头部部件布局为网格
        self.top_layout.setSpacing(0)

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.left_widget1 = QtWidgets.QWidget()  # 创建左上侧部件
        self.left_widget1.setObjectName('left_widget1')
        self.left_layout1 = QtWidgets.QGridLayout()  # 创建左上侧部件的网格布局层
        self.left_widget1.setLayout(self.left_layout1)  # 设置左上侧部件布局为网格

        self.left_widget2 = QtWidgets.QWidget()  # 创建左中侧部件
        self.left_widget2.setObjectName('left_widget2')
        self.left_layout2 = QtWidgets.QGridLayout()  # 创建左中侧部件的网格布局层
        self.left_widget2.setLayout(self.left_layout2)  # 设置左中侧部件布局为网格

        self.left_widget3 = QtWidgets.QWidget()  # 创建左下侧部件-占位
        self.left_widget3.setObjectName('left_widget3')
        self.left_layout3 = QtWidgets.QGridLayout()  # 创建左下侧部件的网格布局层-占位
        self.left_widget3.setLayout(self.left_layout3)  # 设置左下侧部件布局为网格-占位

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.right_widget1 = QtWidgets.QWidget()  # 创建右一侧部件-标题
        self.right_widget1.setObjectName('right_widget1')
        self.right_layout1 = QtWidgets.QGridLayout()  # 创建右一侧部件的网格布局层
        self.right_widget1.setLayout(self.right_layout1)  # 设置右一侧部件布局为网格

        self.right_widget2 = QtWidgets.QWidget()  # 创建右二侧部件-图文
        self.right_widget2.setObjectName('right_widget2')
        self.right_layout2 = QtWidgets.QGridLayout()  # 创建右二侧部件的网格布局层
        self.right_widget2.setLayout(self.right_layout2)  # 设置右二侧部件布局为网格

        self.right_widget3 = QtWidgets.QWidget()  # 创建右三侧部件-标题
        self.right_widget3.setObjectName('right_widget3')
        self.right_layout3 = QtWidgets.QGridLayout()  # 创建右三侧部件的网格布局层
        self.right_widget3.setLayout(self.right_layout3)  # 设置右三侧部件布局为网格

        self.right_widget4 = QtWidgets.QWidget()  # 创建右四侧部件-图文
        self.right_widget4.setObjectName('right_widget4')
        self.right_layout4 = QtWidgets.QGridLayout()  # 创建右四侧部件的网格布局层
        self.right_widget4.setLayout(self.right_layout4)  # 设置右四侧部件布局为网格

        self.right_widget5 = QtWidgets.QWidget()  # 创建右四侧部件-图文
        self.right_widget5.setObjectName('right_widget5')
        self.right_layout5 = QtWidgets.QGridLayout()  # 创建右四侧部件的网格布局层
        self.right_widget5.setLayout(self.right_layout5)  # 设置右四侧部件布局为网格

        self.right_widget22 = QtWidgets.QWidget()  # 创建右二侧部件-图文1
        self.right_widget22.setObjectName('right_widget22')
        self.right_layout22 = QtWidgets.QGridLayout()  # 创建右二侧部件的网格布局层
        self.right_widget22.setLayout(self.right_layout22)  # 设置右二侧部件布局为网格

        self.right_widget21 = QtWidgets.QWidget()  # 创建右二侧部件-图文1
        self.right_widget21.setObjectName('right_widget21')
        self.right_layout21 = QtWidgets.QGridLayout()  # 创建右二侧部件的网格布局层
        self.right_widget21.setLayout(self.right_layout21)  # 设置右二侧部件布局为网格

        self.right_widget23 = QtWidgets.QWidget()  # 创建右二侧部件-图文1
        self.right_widget23.setObjectName('right_widget23')
        self.right_layout23 = QtWidgets.QGridLayout()  # 创建右二侧部件的网格布局层
        self.right_widget23.setLayout(self.right_layout23)  # 设置右二侧部件布局为网格

        self.right_widget24 = QtWidgets.QWidget()  # 创建右二侧部件-图文1
        self.right_widget24.setObjectName('right_widget24')
        self.right_layout24 = QtWidgets.QGridLayout()  # 创建右二侧部件的网格布局层
        self.right_widget24.setLayout(self.right_layout24)  # 设置右二侧部件布局为网格

        self.right_widget25 = QtWidgets.QWidget()  # 创建右二侧部件-图文1
        self.right_widget25.setObjectName('right_widget25')
        self.right_layout25 = QtWidgets.QGridLayout()  # 创建右二侧部件的网格布局层
        self.right_widget25.setLayout(self.right_layout25)  # 设置右二侧部件布局为网格

        self.left_layout.addWidget(self.left_widget1, 0, 0, 3, 3)  # 左侧部件在第0行第0列，占3行3列
        self.left_layout.addWidget(self.left_widget2, 3, 0, 6, 3)  # 左侧部件在第3行第0列，占6行3列
        self.left_layout.addWidget(self.left_widget3, 9, 0, 2, 3)  # 左侧部件在第9行第0列，占2行3列

        self.right_layout2.addWidget(self.right_widget21, 0, 0, 2, 2)  # 左侧部件在第2行第0列，占2行9列
        self.right_layout2.addWidget(self.right_widget22, 0, 2, 2, 2)  # 左侧部件在第2行第0列，占2行9列
        # self.right_layout2.addWidget(self.right_widget23,0,4,2,2) # 左侧部件在第2行第0列，占2行9列
        # self.right_layout2.addWidget(self.right_widget24,0,6,2,2) # 左侧部件在第2行第0列，占2行9列
        self.right_layout2.setContentsMargins(30, 0, 0, 0);

        self.right_layout4.setContentsMargins(30, 0, 0, 0);

        self.right_layout.addWidget(self.right_widget1, 0, 0, 2, 9)  # 左侧部件在第0行第0列，占2行9列
        self.right_layout.addWidget(self.right_widget2, 2, 0, 2, 9)  # 左侧部件在第2行第0列，占2行9列
        self.right_layout.addWidget(self.right_widget3, 4, 0, 2, 9)  # 左侧部件在第4行第0列，占2行9列
        self.right_layout.addWidget(self.right_widget4, 6, 0, 2, 9)  # 左侧部件在第4行第0列，占2行9列
        self.right_layout.addWidget(self.right_widget5, 8, 0, 4, 9)  # 左侧部件在第4行第0列，占2行9列

        self.main_layout.addWidget(self.left_widget, 1, 0, 12, 3)  # 左侧部件在第1行第0列，占12行3列
        self.main_layout.addWidget(self.right_widget, 1, 3, 12, 9)  # 右侧部件在第1行第3列，占12行9列

        self.main_layout.addWidget(self.top_widget, 0, 0, 1, 13)  # 右侧部件在第0行第0列，占1行13列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # self.left_widget.setMargin(0);
        self.left_layout.setVerticalSpacing(0);
        self.left_layout.setSpacing(0)
        self.left_layout2.setSpacing(0)
        self.left_layout3.setSpacing(0)

        self.left_out = QtWidgets.QPushButton(qtawesome.icon('fa.sign-out', color='#808080'), "退出登录")
        self.left_out.setObjectName('left_out')
        self.left_out.clicked.connect(self.close)  # 点击按钮之后关闭窗口

        self.left_username = QtWidgets.QLabel("         基于深度学习的城市交通道路图像处理平台")
        self.left_username.setObjectName('username')

        self.left_close = QtWidgets.QPushButton("")  # 占位
        self.left_visit = QtWidgets.QPushButton("")  # 占位
        self.left_mini = QtWidgets.QPushButton("")  # 占位
        self.zw = QtWidgets.QLabel("")  # 占位
        self.zw2 = QtWidgets.QLabel("")  # 占位

        self.left_label_1 = QtWidgets.QLabel("Admin")
        self.left_label_1.setObjectName('left_label')

        self.left_img_1 = QtWidgets.QLabel("图")
        self.left_img_1.setObjectName('left_img')

        # 按钮
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='#2c3a45'), "首页")
        self.left_button_1.setObjectName('left_button1')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.user', color='#2c3a45'), "城市内涝")
        self.left_button_2.setObjectName('left_button2')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.bars', color='#2c3a45'), "道路能见度")
        self.left_button_3.setObjectName('left_button3')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.file-text', color='#2c3a45'), "环卫评价")
        self.left_button_4.setObjectName('left_button4')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.search', color='#2c3a45'), "帮助/反馈")
        self.left_button_5.setObjectName('left_button5')

        self.right_button_1 = QtWidgets.QPushButton()
        self.right_button_1.setObjectName('right_button1')
        self.right_button_2 = QtWidgets.QPushButton()
        self.right_button_2.setObjectName('right_button2')
        self.right_button_3 = QtWidgets.QPushButton()
        self.right_button_3.setObjectName('right_button3')
        self.right_button_4 = QtWidgets.QPushButton()
        self.right_button_4.setObjectName('right_button4')
        self.right_button_5 = QtWidgets.QPushButton()
        self.right_button_5.setObjectName('right_button5')

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("Ahalk")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('pic\\Ahalk.jpg'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_button_21 = QtWidgets.QLabel("    一维函数优化算例\n")  #
        self.right_button_21.setObjectName('right_button_21')
        self.right_button_22 = QtWidgets.QLabel("")
        # self.right_button_22.setScaledContents (True) # 让图片自适应label大小
        # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.right_button_22.setPixmap(QtGui.QPixmap("pic\\100001\\q.png"))
        self.right_button_22.setGeometry(400, 400, 400, 400)
        self.right_button_22.setObjectName('right_button_22')
        self.right_button_22.setScaledContents(True)
        self.right_button_23 = QtWidgets.QLabel("\n 一维函数、无约束、单目标优化问题")  #
        self.right_button_23.setObjectName('right_button_23')

        self.right_button_221 = QtWidgets.QLabel("  二维Rosenbrock函数\n")  #
        self.right_button_221.setObjectName('right_button_221')
        self.right_button_222 = QtWidgets.QLabel("")
        # self.right_button_22.setScaledContents (True) # 让图片自适应label大小
        # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.right_button_222.setPixmap(QtGui.QPixmap("pic\\100003\\q.png"))
        self.right_button_222.setGeometry(400, 400, 400, 400)
        self.right_button_222.setObjectName('right_button_222')
        self.right_button_222.setScaledContents(True)
        self.right_button_223 = QtWidgets.QLabel("\n    二维(nv=2)Rosenbrock函数无约\n束、单目标优化")  #
        self.right_button_223.setObjectName('right_button_223')

        self.right_button_321 = QtWidgets.QLabel("")  #
        self.right_button_321.setObjectName('right_button_321')
        self.right_button_322 = QtWidgets.QLabel("")
        # self.right_button_22.setScaledContents (True) # 让图片自适应label大小
        # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.right_button_322.setPixmap(QtGui.QPixmap("").scaled(60, 60))
        self.right_button_322.setGeometry(400, 400, 400, 400)
        self.right_button_322.setObjectName('right_button_322')
        self.right_button_323 = QtWidgets.QLabel("")  #
        self.right_button_323.setObjectName('right_button_323')

        self.right_button_421 = QtWidgets.QLabel("")  #
        self.right_button_421.setObjectName('right_button_421')
        self.right_button_422 = QtWidgets.QLabel("")
        # self.right_button_22.setScaledContents (True) # 让图片自适应label大小
        # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.right_button_422.setPixmap(QtGui.QPixmap("").scaled(60, 60))
        self.right_button_422.setGeometry(400, 400, 400, 400)
        self.right_button_422.setObjectName('right_button_422')
        self.right_button_423 = QtWidgets.QLabel("")  #
        self.right_button_423.setObjectName('right_button_423')

        self.right_button_521 = QtWidgets.QLabel("")  #
        self.right_button_521.setObjectName('right_button_521')
        self.right_button_522 = QtWidgets.QLabel("")
        # self.right_button_22.setScaledContents (True) # 让图片自适应label大小
        # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.right_button_522.setPixmap(QtGui.QPixmap("").scaled(60, 60))
        self.right_button_522.setGeometry(400, 400, 400, 400)
        self.right_button_522.setObjectName('right_button_522')
        self.right_button_523 = QtWidgets.QLabel("")  #
        self.right_button_523.setObjectName('right_button_523')

        # self.top_layout.addWidget(self.left_out)

        self.left_button_1.setStyleSheet(
            '''
            *{background-color:#e6e6e6;}
            ''')

        # 按钮布局位置
        # self.left_layout1.addWidget(self.left_img_1,0,0,1,3)
        # self.left_layout1.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout1.addWidget(self.recommend_button_1, 0, 0, 1, 1)

        self.left_layout2.addWidget(self.left_button_1, 0, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_2, 1, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_3, 2, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_4, 3, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_5, 4, 0, 1, 3)

        self.top_layout.addWidget(self.left_username, 0, 0, 1, 15)
        self.top_layout.addWidget(self.left_out, 0, 16, 1, 1)

        # 右边布局
        self.right_label_1 = QtWidgets.QLabel("问题选择")
        self.right_label_1.setObjectName('right_label')
        self.right_label_2 = QtWidgets.QLabel("")
        self.right_label_2.setObjectName('right_labe2')

        self.right_layout1.addWidget(self.right_label_1, 1, 0, 2, 9)

        self.right_layout3.addWidget(self.right_label_2, 2, 0, 2, 9)

        # self.right_layout21.addWidget(self.zw,0,0,1,1)
        self.right_layout21.addWidget(self.right_button_21, 1, 0, 1, 1)
        self.right_layout21.addWidget(self.right_button_22, 2, 0, 1, 1)
        self.right_layout21.addWidget(self.right_button_23, 4, 0, 8, 4)

        self.right_layout21.addWidget(self.right_button_1, 0, 0, 8, 8)
        # self.right_layout21.addWidget(self.zw2,12,0,1,1)
        self.right_layout21.setContentsMargins(0, 20, 0, 20);

        self.right_button_1.setStyleSheet(
            '''
            QPushButton{height:50px;border:none}
            ''')

        self.right_layout22.addWidget(self.right_button_221, 1, 0, 1, 1)
        self.right_layout22.addWidget(self.right_button_222, 2, 0, 1, 1)
        self.right_layout22.addWidget(self.right_button_223, 4, 0, 8, 4)

        self.right_layout22.addWidget(self.right_button_2, 0, 0, 8, 8)
        self.right_layout22.setContentsMargins(0, 20, 0, 20);

        self.right_button_2.setStyleSheet(
            '''
            QPushButton{height:50px;border:none}
            ''')

        self.right_layout23.addWidget(self.right_button_321, 1, 0, 1, 1)
        self.right_layout23.addWidget(self.right_button_322, 2, 0, 1, 1)
        self.right_layout23.addWidget(self.right_button_323, 4, 0, 8, 4)

        self.right_layout23.addWidget(self.right_button_3, 0, 0, 8, 8)
        self.right_layout23.setContentsMargins(0, 20, 0, 20);

        self.right_button_3.setStyleSheet(
            '''
            QPushButton{height:50px;border:none}
            ''')

        self.right_layout24.addWidget(self.right_button_421, 1, 0, 1, 1)
        self.right_layout24.addWidget(self.right_button_422, 2, 0, 1, 1)
        self.right_layout24.addWidget(self.right_button_423, 4, 0, 8, 4)

        self.right_layout24.addWidget(self.right_button_4, 0, 0, 8, 8)
        self.right_layout24.setContentsMargins(0, 20, 0, 20);

        self.right_button_4.setStyleSheet(
            '''
            QPushButton{height:50px;border:none}
            ''')

        self.right_layout25.addWidget(self.right_button_521, 1, 0, 1, 1)
        self.right_layout25.addWidget(self.right_button_522, 2, 0, 1, 1)
        self.right_layout25.addWidget(self.right_button_523, 4, 0, 8, 4)

        self.right_layout25.addWidget(self.right_button_5, 0, 0, 8, 8)
        self.right_layout25.setContentsMargins(0, 20, 0, 20);

        self.right_button_5.setStyleSheet(
            '''
            QPushButton{height:50px;border:none}
            ''')

        self.main_layout.setContentsMargins(0, 0, 0, 0);
        self.left_layout.setContentsMargins(0, 0, 0, 0);
        self.left_layout1.setContentsMargins(0, 0, 0, 0);
        self.left_layout2.setContentsMargins(0, 0, 0, 0);
        self.left_layout3.setContentsMargins(0, 0, 0, 0);
        self.right_layout.setContentsMargins(0, 0, 0, 0);
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.right_widget21.setStyleSheet(
            '''
            QWidget#right_widget21{
            border:none;
            border-radius：100px;
            font-size:15px;
            background-color:#fafafa;
            padding: 30px;
             }
            QWidget#right_button_21{margin: 0 auto;color:#909399;font-size:20px;font-weight:500;}
            QWidget#right_button_22{margin: 0 auto;}
            QWidget#right_button_23{margin: 0 auto;color:#2c3a45;font-size:15px;font-weight:500;}
            ''')
        self.right_widget22.setStyleSheet(
            '''
            QWidget#right_widget22{
            border:none;
            border-radius：100px;
            font-size:15px;
            background-color:#fafafa;
            padding: 30px;
             }
            QWidget#right_button_221{margin: 0 auto;color:#909399;font-size:20px;font-weight:500;}
            QWidget#right_button_222{margin: 0 auto;}
            QWidget#right_button_223{margin: 0 auto;color:#2c3a45;font-size:15px;font-weight:500;}
            ''')

        self.right_widget23.setStyleSheet(
            '''
            QWidget#right_widget23{
            border:none;
            border-radius：100px;
            font-size:15px;
            background-color:#fafafa;
            padding: 30px;
             }
            QWidget#right_button_321{margin: 0 auto;color:#909399;font-size:20px;font-weight:500;}
            QWidget#right_button_322{margin: 0 auto;}
            QWidget#right_button_323{margin: 0 auto;color:#2c3a45;font-size:15px;font-weight:500;}
            ''')

        self.right_widget24.setStyleSheet(
            '''
            QWidget#right_widget24{
            border:none;
            border-radius：100px;
            font-size:15px;
            background-color:#fafafa;
            padding: 30px;
             }
            QWidget#right_button_421{margin: 0 auto;color:#909399;font-size:20px;font-weight:500;}
            QWidget#right_button_422{margin: 0 auto;}
            QWidget#right_button_423{margin: 0 auto;color:#2c3a45;font-size:15px;font-weight:500;}
            ''')

        self.right_widget25.setStyleSheet(
            '''
            QWidget#right_widget25{
            border:none;
            border-radius：100px;
            font-size:15px;
            background-color:#fafafa;
            padding: 30px;
             }
            QWidget#right_button_521{margin: 0 auto;color:#909399;font-size:20px;font-weight:500;}
            QWidget#right_button_522{margin: 0 auto;}
            QWidget#right_button_523{margin: 0 auto;color:#2c3a45;font-size:15px;font-weight:500;}
            ''')


        self.right_widget.setStyleSheet(
            '''
            QLabel{
            border:none;
            font-size:23px;
            font-weight:500;
            color:#2c3a45;
            font-family:'微软雅黑';
            padding-left:30px;
             }
            ''')
        self.left_widget1.setStyleSheet(
            '''
            *{color:#2c3a45;}
    
            QToolButton{
            border:none;
            font-weight:600;
            font-size:14px;
            font-family:'微软雅黑';
            }
            ''')
        self.left_widget2.setStyleSheet(
            '''
            QPushButton:hover{background:#e6e6e6;}
            ''')
        self.top_widget.setStyleSheet(
            '''
            *{background-color:#303030;}
            QLabel{
            color:#ffffff;
            border:none;
            font-weight:600;
            font-size:16px;
            font-family:'微软雅黑';
             }
            QPushButton{
            color:#ffffff;
            border:none;
            font-weight:600;
            font-size:16px;
            font-family:'微软雅黑';
             }
            ''')
        self.left_widget.setStyleSheet(
            '''
            *{background-color:#fafafa;}
            QPushButton{
            border:none;
            font-size:15px;
            text-align:left;
            padding-left:30px;
            height:70px;
            font-family:'微软雅黑';
             }
            QPushButton:hover{background:red;}
            ''')
        self.left_out.setStyleSheet(
            '''
            QPushButton{ text-align:right;padding-right:30px;color:#808080;font-size:14px;}
            ''')
        self.left_username.setStyleSheet(
            '''
            QPushButton{ text-align:left;padding-left:30px;color:#ffffff;font-size:16px;}
            ''')

        self.left_label_1.setStyleSheet(
            '''
            QLabel{background-color:#eeeeee;}
            ''')
        self.right_widget.setStyleSheet(
            '''
            *{background-color:#f2f2f2;}
            ''')

