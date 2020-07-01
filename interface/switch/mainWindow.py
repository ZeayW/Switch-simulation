from PyQt5.QtWidgets import QWidget

from window import Ui_Mainwindow
from Widget import Ui_Widget1
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtGui import QPen,QPainter,QPixmap
import sys
import os
import os.path

class Switch:
    def __init__(self):
        self.a=1;
# 主界面
class main_window(QWidget):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Widget1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.addSwitch)
        self.qpen=QPen()


    def addSwitch(self):
        #创建一个新按钮
        self.ui.btn=QtWidgets.QPushButton(self)
        #设置按钮属性
        #self.ui.btn.setObjectName(text)
        self.ui.btn.setGeometry(10,10,100,30)
        _translate = QtCore.QCoreApplication.translate
        self.ui.btn.setText(_translate("MainWindow", "aa"))

        #设置按钮格式：
        font=QtGui.QFont()
        font.setUnderline(True)
        font.setBold(True)
        font.setPointSize(10)
        self.ui.btn.setFont(font)
        self.ui.btn.setStyleSheet("border:none;")
        self.ui.btn.show()
        #self.ui.paintEvent()

    def paintEvent(self):
     painter = QPainter(self)
     print("aa")
     pixmap = QPixmap("myPic.png")
     painter.drawPixmap(self.rect(), pixmap)
     print("aa")
     pen = QPen(Qt.black, 3)
     pen.setWidth(2)
     painter.setPen(pen)
     painter.drawLine(10, 100, 30, 50)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())
