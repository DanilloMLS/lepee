# -*- coding: cp1252 -*-

'''
    Autor: "Danillo Moraes"
    Versão: "2.0.0"
    Email: "moraesdanillo10@gmail.com
    Data de Criação: 28/10/2015
    Data da última modificação: 12/02/2016
    Autor da úlitma mod: Danillo Moraes
    Versão Python: 2.7
    Versão do PyQt: 4.8
'''
import os
import time
from PyQt4 import QtGui, QtCore, uic
from animated import animated_widget
import tela_nivel
import tela_login

class TelaIntro(QtGui.QMainWindow):
    def __init__(self,parent=None):

        super(TelaIntro,self).__init__()
        uic.loadUi("templates" + os.sep + "tela_intro.ui", self)
        dir_icons = "icons" + os.sep
        
        cursor = QtGui.QCursor(QtGui.QPixmap(dir_icons + 'pointingHand.png'))

        '''animated_widget(self.alunoButton, dir_icons + 'parar.gif')
        self.alunoButton.setGeometry(self.alunoButton.x(), self.alunoButton.y(), 251, 200)
        self.alunoButton.setCursor(cursor)
        self.alunoButton.show()'''

        palette = QtGui.QPalette()
        self.setAutoFillBackground(True)
        img = QtGui.QPixmap("background\\introducao.jpg")
        img = img.scaled(QtCore.QSize(self.width(), self.height()))
        palette.setBrush(palette.Background, QtGui.QBrush(img))
        self.setPalette(palette)

        self.profButton.setIcon(QtGui.QIcon('icons\\Viviane.jpg'))
        self.profButton.setIconSize(QtCore.QSize(160,200))
        #animated_widget(self.profButton, dir_icons + 'parar.gif')
        #self.profButton.setGeometry(self.profButton.x(), self.profButton.y(), 251, 200)
        self.profButton.setCursor(cursor)
        self.profButton.show()
    
        animated_widget(self.introLabel, dir_icons + 'apres.gif')
        self.introLabel.setGeometry(self.introLabel.x(), self.introLabel.y(),
                                    self.introLabel.width(), self.introLabel.height())
        self.introLabel.show()
        
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

        #self.alunoButton.clicked.connect(self.abre_tela_nivelEvent)
        self.profButton.clicked.connect(self.abre_tela_login)
        
    def abre_tela_nivelEvent(self, e):
        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()
    
    def abre_tela_login(self, e):
        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()
    
    def closeEvent(self, e):
        '''
            Destrói os objetos na janela principal quando está for fechada
        '''
        self.deleteLater()


if __name__ == "__main__":        
    root = QtGui.QApplication([])
    
    splash_pix = QtGui.QPixmap("background\\abertura.png")
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    
    splash.setMask(splash_pix.mask())
    splash.show()
    root.processEvents()

    time.sleep(4)
    
    app = TelaIntro()
    splash.finish(app)
    app.show()
    
    root.exec_()

        
