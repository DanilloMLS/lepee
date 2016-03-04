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
import tela_login

class TelaCadastro(QtGui.QMainWindow):
    def __init__(self):

        super(TelaCadastro,self).__init__()
        uic.loadUi("templates" + os.sep + "tela_cadastro.ui", self)
        dir_icons = "icons" + os.sep
        
        cursor = QtGui.QCursor(QtGui.QPixmap(dir_icons + 'pointingHand.png'))

        self.okButton.setCursor(cursor)
        self.cancelButton.setCursor(cursor)
        
        self.setMaximumHeight(250)
        self.setMaximumWidth(450)
        self.setMinimumHeight(250)
        self.setMinimumWidth(450)
        
        self.okButton.clicked.connect(self.abre_tela_nivelEvent)
        self.cancelButton.clicked.connect(self.abre_tela_login)
        
    def abre_tela_nivelEvent(self, e):
        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()

    def abre_tela_login(self, e):
        self.a = tela_login.TelaLogin()
        self.a.show()

        self.close()

        
    def closeEvent(self, e):
        '''
            Destr�i os objetos na janela principal quando est� for fechada
        '''
        self.deleteLater()

