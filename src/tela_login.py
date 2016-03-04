# -*- coding: cp1252 -*-
'''
    Autor: "Danillo Moraes"
    Vers�o: "2.0.0"
    Email: "moraesdanillo10@gmail.com
    Data de Cria��o: 12/02/2016
    Data da �ltima modifica��o: 12/02/2016
    Autor da �litma mod: Danillo Moraes
    Vers�o Python: 2.7
    Vers�o do PyQt: 4.8
'''
import os
from PyQt4 import QtGui, QtCore, uic
import tela_nivel
import tela_cadastro

class TelaLogin(QtGui.QMainWindow):
    def __init__(self):

        super(TelaLogin,self).__init__()
        uic.loadUi("templates" + os.sep + "tela_login.ui", self)
        dir_icons = "icons" + os.sep
        
        cursor = QtGui.QCursor(QtGui.QPixmap(dir_icons + 'pointingHand.png'))

        self.logarButton.setCursor(cursor)
        self.cadButton.setCursor(cursor)
        
        self.setMaximumHeight(200)
        self.setMaximumWidth(400)
        self.setMinimumHeight(200)
        self.setMinimumWidth(400)

        self.logarButton.clicked.connect(self.abre_tela_nivelEvent)
        self.cadButton.clicked.connect(self.abre_tela_cadastro)
        
    def abre_tela_nivelEvent(self, e):
        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()

    def abre_tela_cadastro(self, e):
        self.a = tela_cadastro.TelaCadastro()
        self.a.show()

        self.close()

    def closeEvent(self, e):
        '''
            Destr�i os objetos na janela principal quando est� for fechada
        '''
        self.deleteLater()

