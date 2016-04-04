#-*- coding: cp1252 -*-

'''
    Tela de Avaliação quantitativa
'''

import os
import tela_avl_qualitativa
from player import Player
from PyQt4 import uic, QtCore, QtGui

class TelaAvaliacao(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(TelaAvaliacao, self).__init__()

        uic.loadUi(os.sep.join(["templates","tela_avaliacao.ui"]), self)
        self.__player1 = Player(self.perguntaWidget)
        self.__player2 = Player(self.alternativaWidget)

        
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

        self.proxPerg.clicked.connect(self.abre_tela_avlQualitativa)

    def abre_tela_avlQualitativa(self, e):
        self.a = tela_avl_qualitativa.TelaAvalQualitativa()
        self.a.show()

        self.close()

'''
root = QtGui.QApplication([])
app = TelaAvaliacao()
app.show()
root.exec_()
'''
