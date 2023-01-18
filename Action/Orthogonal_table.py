from PyQt5.QtWidgets import *
from PyQt5.QtCore  import  *
from PyQt5.QtGui  import  *
from Algorithm.Orthogonal_alg import *
import json
import requests
from functools import partial
from nose.tools import *
from UI import orthogonal_dialog_ui
from Action import  Orthogonal_table
class Orthogonal_dialog(QDialog):
    def __init__(self,MainWindow):
        self.MainWindow=MainWindow
        QDialog.__init__(self)
        self.ui = orthogonal_dialog_ui.Ui_Dialog()  # 子窗口的实例化
        self.ui.setupUi(self)
        self.setWindowTitle("正交设计")
        self.setAction()
        self.createTable()

    def createTable(self):
        self.table = self.ui.tableWidget
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setRowCount(1)
        self.table.setColumnCount(2)
        item = QTableWidgetItem("3")
        self.table.setItem(0, 0, item)
        self.table.item(0, 0).setTextAlignment(Qt.AlignCenter)
        item = QTableWidgetItem("2")
        self.table.setItem(0, 1, item)
        self.table.item(0, 1).setTextAlignment(Qt.AlignCenter)

    def setAction(self):
        self.ui.pushButton.clicked.connect(self.open_table)
        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.pushButton_3.clicked.connect(self.Add)
        self.ui.pushButton_2.clicked.connect(self.Delete)

    def Add(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        item = QTableWidgetItem("1")
        self.table.setItem(row, 0, item)
        self.table.item(row, 0).setTextAlignment(Qt.AlignCenter)
        item = QTableWidgetItem("2")
        self.table.setItem(row, 1, item)
        self.table.item(row, 1).setTextAlignment(Qt.AlignCenter)

    def Delete(self):
        row = self.table.currentRow()
        self.table.removeRow(row)

    def open_table(self):
        Orthogonal_table.Orthogonal_table(self).exec_()

    def accepted(self):
        data=[]
        for i in range(self.table.rowCount()):
            data.append((int(self.table.item(i,1).text()),int(self.table.item(i,0).text())))

        oat=OAT()
        self.results=oat.genSets2(data)
        self.result_table(self.results)

    def result_table(self, res):
        self.MainWindow.setLayout1()
        #self.MainWindow.btn1.clicked.connect(self.re_design)
        self.MainWindow.label.setText("正交设计方案")
        self.MainWindow.btn.clicked.connect(self.MainWindow.Visualize_2D)
        #self.MainWindow.btn1.setVisible(False)
        ft = QFont()
        ft.setPointSize(11)
        self.MainWindow.label.setFont(ft)
        row = res.shape[0]
        col = res.shape[1]
        self.MainWindow.table.setRowCount(row)
        self.MainWindow.table.setColumnCount(col)

        for i in range(row):
            for j in range(col):
                item = QTableWidgetItem("%s " % res[i, j])
                self.MainWindow.table.setItem(i, j, item)
        self.MainWindow.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        qe = QEventLoop()
        qe.exec_()

      #  item = QTableWidgetItem( self.ui.lineEdit.text())
      #  self.table.setItem(0, 0, item)