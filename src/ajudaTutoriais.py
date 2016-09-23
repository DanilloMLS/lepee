# -*- coding: cp1252 -*-

import sys
import os
from player import Player
from PyQt4 import QtGui, QtCore, Qt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class TelaAjudaTutoriais(QtGui.QMainWindow):
    def __init__(self):
        super(TelaAjudaTutoriais, self).__init__()
        cursor = QtGui.QCursor(QtGui.QPixmap('icons\\pointingHand.png'))
        ###########################################################

        self.setObjectName(_fromUtf8("self"))
        self.resize(633, 611)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons\\logo lepe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet(_fromUtf8("background-image: url(:ajuda.jpg);\n"
""))
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.voltarBt = QtGui.QPushButton(self.centralwidget)
        self.voltarBt.setGeometry(QtCore.QRect(520, 560, 75, 23))
        self.voltarBt.setObjectName(_fromUtf8("voltarBt"))
        self.voltarBt.setCursor(cursor)

        self.tutorialWidget = QtGui.QWidget(self.centralwidget)
        self.tutorialWidget.setGeometry(QtCore.QRect(40, 30, 553, 376))
        self.tutorialWidget.setStyleSheet(_fromUtf8("background-color: rgb(63, 63, 63);"))
        
        self.tutorialWidget.setObjectName(_fromUtf8("tutorialWidget"))

        self.tutorial1Bt = QtGui.QPushButton(self.centralwidget)
        self.tutorial1Bt.setGeometry(QtCore.QRect(40, 440, 181, 71))
        self.tutorial1Bt.setCursor(cursor)

        font = QtGui.QFont()
        font.setPointSize(14)

        self.tutorial1Bt.setFont(font)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons\\arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tutorial1Bt.setIcon(icon1)
        self.tutorial1Bt.setObjectName(_fromUtf8("tutorial1Bt"))
        self.tutorial2Bt = QtGui.QPushButton(self.centralwidget)
        self.tutorial2Bt.setGeometry(QtCore.QRect(420, 440, 181, 71))
        self.tutorial2Bt.setCursor(cursor)

        font = QtGui.QFont()
        font.setPointSize(14)

        self.tutorial2Bt.setFont(font)
        self.tutorial2Bt.setIcon(icon1)
        self.tutorial2Bt.setObjectName(_fromUtf8("tutorial2Bt"))
        self.tutorial3Bt = QtGui.QPushButton(self.centralwidget)
        self.tutorial3Bt.setGeometry(QtCore.QRect(230, 440, 181, 71))
        self.tutorial3Bt.setCursor(cursor)
        
        font = QtGui.QFont()
        font.setPointSize(14)

        self.tutorial3Bt.setFont(font)
        self.tutorial3Bt.setIcon(icon1)
        self.tutorial3Bt.setObjectName(_fromUtf8("tutorial3Bt"))
        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.setWindowTitle("Ajuda - Tutoriais")
        self.voltarBt.setText("Voltar")
        self.tutorial1Bt.setText("Escolhendo\num nível")
        self.tutorial2Bt.setText("Avaliação\nQuantitativa")
        self.tutorial3Bt.setText("Avaliação\nQualitativa")

        
        ###########################################################
        
        self.__player1 = Player(self.tutorialWidget)

        palette	= QtGui.QPalette()
        self.setAutoFillBackground(True)
        img = QtGui.QPixmap("background\\ajuda.jpg")
        img = img.scaled(QtCore.QSize(self.width(), self.height()))
        palette.setBrush(palette.Background, QtGui.QBrush(img))
        self.setPalette(palette)

        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())
        self.show()

        self.__player1.carregar("niveis\\nivel 1\\conts\\Cores\\video\\1- CORES ok.avi")
        self.tutorial1Bt.clicked.connect(self.mostrarTutorial1)
        self.tutorial2Bt.clicked.connect(self.mostrarTutorial2)
        self.tutorial3Bt.clicked.connect(self.mostrarTutorial3)
        
        self.voltarBt.clicked.connect(self.voltar)

    def mostrarTutorial1(self):
        self.__player1.carregar("ajuda\\tutorial1.avi")

    def mostrarTutorial2(self):
        self.__player1.carregar("ajuda\\tutorial2.avi") 

    def mostrarTutorial3(self):
        self.__player1.carregar("ajuda\\tutorial3.avi") 
    
    def voltar(self,e):
        #self.a = ajudaMenuInicial.TelaAjuda()
        #self.a.show()
        self.close()

    
def main():
    app = QtGui.QApplication(sys.argv)
    window = TelaAjudaTutoriais()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())
