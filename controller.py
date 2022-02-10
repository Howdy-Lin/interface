from PyQt5 import QtWidgets, QtGui, QtCore

from qtt import Ui_MainWindow


import random


class MainWindow_controller(QtWidgets.QMainWindow):
    

    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.a = random.randint(1, 99)
        self.l = 1
        self.h = 99
    def setup_control(self):
        self.ui.pushButton.clicked.connect(self.buttonClicked)
        
    
    def buttonClicked(self):
                       
        b = self.ui.lineEdit.text()
        try:
            b = int(b)
            
        except:            
            self.lineEdit.clear()
            b=''
        if b:
            if self.a==b:
                self.ui.lineEdit_2.setText('猜對了')              
                
            elif self.a>b:
                if b>self.l:
                    self.l=b
                self.ui.lineEdit_2.setText('数值的范围:{}-{}     太小了'.format(self.l, self.h))
                
            elif self.a<b:
                if b<self.h:
                    self.h=b
                self.ui.lineEdit_2.setText('数值的范围:{}-{}     太大了'.format(self.l, self.h))
                
            #b = self.ui.lineEdit.text()
        #elif b > a:
            #self.ui.lineEdit_2.setText('�摮云憭批���岫銝�甈∪')
        '''
        while a != b:  # 雿輻 while 餈游����� a 銝� b嚗停銝蝜潛��
            if b < a:
                self.ui.lineEdit_2.setText('�摮云撠���岫銝�甈∪')
                b = self.ui.lineEdit.text()
            elif b > a:
                self.ui.lineEdit_2.setText('�摮云憭批���岫銝�甈∪')
                b = self.ui.lineEdit.text()
        '''