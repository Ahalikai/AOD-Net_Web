import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Results_dialog(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(596, 420)
     #   self.ui = results.Ui_Form()  # 子窗口的实例化
     #   self.ui.setupUi(self)
        self.setWindowTitle("实验方案结果")
        self.init()
        self.setAction()

    def init(self):
        self.widget=QWidget()
        self.table= QTableWidget(self.widget)
        self.setCentralWidget(self.widget)
        windowLayout=QHBoxLayout()
        windowLayout.addWidget(self.table)
        self.widget.setLayout(windowLayout)

    def create_Evolution_table(self,row=4,col=10):
       # self.ui.label.setText("优化设计方案")
      #  self.table=self.ui.tableWidget
        self.table.setRowCount(row)
        self.table.setColumnCount(col)

      #题  for i in range(row):
    #       #  for i in range(col):
    #      #   self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标3', '标题4']
    #      fp)
        for i in range(row):
            for j in range(col):
                item=QTableWidgetItem("%s %s" % (i,j))
                self.table.setItem(i,j,item)
                # 设置每个位置的文本值




    def setAction(self):
        pass