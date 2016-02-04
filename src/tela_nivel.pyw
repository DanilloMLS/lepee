# -*- coding: cp1252 -*-

'''
    Autor: "Fagner Barros"
    Versão: "1.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Criação: 07/11/2015
    Data da última modificação: 07/11/2015
    Versão Python: 2.7
    Versão do PyQt: 4.8
'''

import os
from PyQt4 import QtGui, QtCore, uic
import tela_ensino

class TelaNivel(QtGui.QWidget):
    def __init__(self):
        super(TelaNivel, self).__init__()
        uic.loadUi("templates" + os.sep + "tela_nivel.ui", self)

        i =  1
        x = 37
        y = 30
        for nivel in os.listdir("niveis"):
            btn = QtGui.QPushButton(self)
            btn.setGeometry(x, y, 151, 111)
            self.__conecta_event_btn(btn, nivel)
            btn.show()
            x += 151
            i+=1
            if i % 5 == 0:
                y+= 111
                x= 37

    def __conecta_event_btn(self, btn, nivel):
        #Relaciona um botão e um conteúdo a um evento 
        btn.clicked.connect(lambda: self.__envia_nivel_selec(nivel))
        
    def __envia_nivel_selec(self, nivel):
        self.tela = tela_ensino.TelaEnsino(None, "niveis" + os.sep +
                                           nivel + os.sep + "conts" + os.sep)
        self.tela.show()
        self.close()

    def closeEvent(self, e):
        self.deleteLater()
'''        
root = QtGui.QApplication([])
app = Nivel()
app.show()
root.exec_()
'''
