#-*- coding: cp1252 -*-

'''
    Tela de Avalia��o
'''

from player import Player
from PyQt4 import uic, QtCore, QtGui

class TelaAvaliacao(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(TelaAvaliacao, self).__init__()
        print "Entrou na Tela de Avalia��o"

        uic.loadUi(os.sep.join(["templates","tela_ensino.ui"]), self)
        self.__player = Player(self.perguntaWidget)
        
        
