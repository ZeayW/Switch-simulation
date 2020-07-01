from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from SendWindow import Ui_SendWindow
class SendWin(QWidget):
    def __init__(self,e):
        super().__init__()
        self.ui=Ui_SendWindow()
        self.ui.setupUi(self)
        self.ui.selectBtn.clicked.connect(self.select)
        self.ui.sendBtn.clicked.connect(lambda: e.send(self.ui.macEdit.text(),self.txt))
    def select(self):
        filename = QFileDialog.getOpenFileName(self, 'open file', '')
        print(filename[0])
        with open(filename[0],'rb') as f:
            self.txt=f.read()


class MachineNode:
    def __init__(self,x,y,len,wd,direc,mac,btn):
        self.link=(-1,-1)
        self.mac=mac
        self.width=wd
        self.len=len
        self.setpos(x,y,direc)

        self.btn=btn
        self.btn.setGeometry(self.x,self.y,100,50)

        # 设置按钮格式：
        font = QFont()
        font.setBold(True)
        font.setPointSize(8)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.goto)

        self.sendWin=SendWin(self)

    def goto(self):
        self.sendWin.show()
    def send(self,dest,text):
        print("send from "+self.mac+" to "+dest+":")
        print(text)

    #def setLink(self,sw,port):
        #self.link=(sw,port)

    def show(self):
        self.btn.show()

    def setpos(self,x,y,direc):
        if direc==1:
            self.x,self.y=x-self.len/2,y-self.width
        if direc==2:
            self.x,self.y=x-self.len,y-self.width/2
        if direc==3:
            self.x,self.y=x-self.len/2,y
        if direc==4:
            self.x,self.y=x,y-self.width/2

