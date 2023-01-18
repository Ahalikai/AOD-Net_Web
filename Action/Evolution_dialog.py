from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QEventLoop
from UI import evolution_dialog_ui
from  Action import  Results_dialog

class Evolution_dialog(QDialog):
    def __init__(self,MainWindow):
        self.MainWindow=MainWindow
        QDialog.__init__(self)
        self.ui = evolution_dialog_ui.Ui_Dialog()  # 子窗口的实例化
        self.ui.setupUi(self)
        self.setWindowTitle("优化实验设计")
        self.setAction()

    def setAction(self):
        self.box_problem=self.ui.comboBox
        self.box_problem.currentIndexChanged.connect(self.Problemchange)
        self.box_algorithm=self.ui.comboBox_2
        self.box_algorithm.currentIndexChanged.connect(self.Algorithmchange)
        self.ui.buttonBox.accepted.connect(self.buttonBox_accepted)
       # self.ui.buttonBox.rejected.connect(self.buttonBox_rejected)



    def buttonBox_accepted(self):

        self.widget = QWidget()
        self.table = QTableWidget(self.widget)
        self.MainWindow.setCentralWidget(self.widget)
        windowLayout = QVBoxLayout()

        label = QLabel()
        label.setText("优化设计方案")
        ft=QFont()
        ft.setPointSize(11)
        label.setFont(ft)

        windowLayout.addWidget(label)
        windowLayout.addWidget(self.table)

        self.widget.setLayout(windowLayout)
        row = 3
        col = 10
        self.table.setRowCount(row)
        self.table.setColumnCount(col)
        for i in range(row):
            for j in range(col):
                item = QTableWidgetItem("%s %s" % (i, j))
                self.table.setItem(i, j, item)

       # res=Results_dialog.Results_dialog()
       # res.create_Evolution_table()
       # res.show()
       # qe = QEventLoop()
       # qe.exec_()




    def Problemchange(self):
        pro = self.box_problem.itemText(self.box_problem.currentIndex())
        if(pro=="问题1"):
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append("1")
        if (pro == "问题2"):
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append("2")
        if (pro == "问题3"):
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append("3")
        if (pro == "问题4"):
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append("4")

    def Algorithmchange(self):
        alg=self.box_algorithm.itemText(self.box_algorithm.currentIndex())
        if(alg=='PSO'):
            self.ui.gridWidget_3.setVisible(True)
            self.ui.label_7.setText("W")
            self.ui.label_8.setText("C1")
            self.ui.label_9.setText("C2")
        if (alg == 'GA'):
            self.ui.label_7.setText("交叉概率")
            self.ui.label_8.setText("变异概率")

            self.ui.gridWidget_3.setVisible(False)
        if (alg == 'DE'):
            self.ui.label_7.setText("交叉概率")
            self.ui.label_8.setText("缩放因子")
            self.ui.gridWidget_3.setVisible(False)
