#-*- coding: cp1252 -*-

'''
    Tela de Avaliação qualitativa
'''

import os
import tela_nivel
from PyQt4 import uic, QtCore, QtGui

class TelaAvalQualitativa(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(TelaAvalQualitativa, self).__init__()
        uic.loadUi(os.sep.join(["templates","tela_avl_qualitativa.ui"]), self)

        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

        self.salvarButton.clicked.connect(self.abre_tela_nivel)

    def abre_tela_nivel(self, e):
        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()

'''      
root = QtGui.QApplication([])
app = TelaAvalQualitativa()
app.show()
root.exec_()
'''
