from PyQt5.QtGui import QFont
class SwitchNode:
    def __init__(self,x,y,len,wd,port,btn):
        #设置各端口的连接 links[x]= (t,s,p) 表示本交换机的x号端口的连接情况
            #若t=0，表示连接到机器，s表示机器号
            #若t=1,表示连接到交换机，s表示交换机号，p表示端口号
        self.links=[(0,-1,-1),(0,-1,-1),(0,-1,-1),(0,-1,-1)]

        self.width=wd
        self.len=len
        self.setpos(x, y, port)
        self.btn=btn
        self.btn.setGeometry(self.x,self.y,100,50)
        font = QFont()
        font.setBold(True)
        font.setPointSize(9)
        self.btn.setFont(font)

    def setpos(self,x,y,direc):
        if direc==1:
            self.x,self.y=x-self.len/2,y-self.width
        elif direc==2:
            self.x,self.y=x-self.len,y-self.width/2
        elif direc==3:
            self.x,self.y=x-self.len/2,y
        elif direc==4:
            self.x,self.y=x,y-self.width/2
        else:
            self.x,self.y=x,y

    #def setLink(self,my_port,dest_sw,dest_port):
        #self.links[my_port]=(dest_sw,dest_port)

    def show(self):
        self.btn.show()
    def port1_pos(self):
        return (self.x+self.len/2,self.y,self.x+self.len/2,self.y-80)

    def port2_pos(self):
        return (self.x,self.y+self.width/2,self.x-80,self.y+self.width/2)
    def port3_pos(self):
        return (self.x+self.len/2,self.y+self.width/2,self.x+self.len/2,self.y+self.width/2+100)
    def port4_pos(self):
        return (self.x+self.len,self.y+self.width/2, self.x+self.len+80,self.y+self.width/2)

    def port_pos(self,i):
        if i==1: return self.port1_pos();
        if i==2: return self.port2_pos();
        if i == 3: return self.port3_pos();
        if i == 4: return self.port4_pos();
