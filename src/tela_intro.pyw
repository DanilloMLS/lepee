# -*- coding: cp1252 -*-

'''
    Autor: "Danillo Moraes"
    Vers�o: "2.0.0"
    Email: "moraesdanillo10@gmail.com
    Data de Cria��o: 28/10/2015
    Data da �ltima modifica��o: 28/10/2015
    Vers�o Python: 2.7
    Vers�o do PyQt: 4.8
'''

from PyQt4 import QtGui, QtCore, uic
import animated_button
import tela_ensino

class TelaIntro(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(TelaIntro,self).__init__()
        uic.loadUi("templates\\intro.ui",self)

        self.__alunoButton = animated_button.AnimatedButton(self.alunoWidget,'icons\\voltar.gif')
        self.__alunoButton.setGeometry(self.__alunoButton.x(),self.__alunoButton.y(), 251,200)
        self.__alunoButton.show()
        
        self.__profButton = animated_button.AnimatedButton(self.profWidget,'icons\\voltar.gif')
        self.__profButton.setGeometry(self.__profButton.x(),self.__profButton.y(), 251,200)
        self.__profButton.show()

        self.__introGif = animated_button.AnimatedButton(self.introGif,'icons\\voltar.gif')
        self.__introGif.setGeometry(self.__introGif.x(),self.__introGif.y(), 211,121)
        self.__introGif.show()
        
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

        self.__alunoButton.clicked.connect(self.abre_tela_nivelEvent)


    def abre_tela_nivelEvent(self, e):
        self.a = tela_ensino.TelaEnsino()
        self.a.show()

        self.close()


    def closeEvent(self, e):
        '''
            Destr�i os objetos na janela principal quando est� for fechada
        '''
        self.deleteLater()

        
root = QtGui.QApplication([])
app = TelaIntro()
app.show()
root.exec_()
