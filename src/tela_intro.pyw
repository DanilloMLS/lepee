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

class TelaIntro(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(TelaIntro,self).__init__()
        uic.loadUi("templates\\intro.ui",self)

        self.__alunoButton = animated_button.AnimatedButton(self.alunoWidget,'icons\\voltar.gif')
        self.__alunoButton.show()

        self.__profButton = animated_button.AnimatedButton(self.profWidget,'icons\\voltar.gif')
        self.__profButton.show()
        
        #self.alunoButton.setText('Meu Texto')
        #self.profButton.setText('123456')
        #profButton = animated_button.AnimatedButton(self,'icons\\voltar.gif')    
        #alunoButton = animated_button.AnimatedButton(self,'icons\\voltar.gif')
        #self.__alunoButton.show()

        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

root = QtGui.QApplication([])
app = TelaIntro()
app.show()
root.exec_()
