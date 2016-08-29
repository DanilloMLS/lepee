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
import ajudaTutoriais
from PyQt4 import QtGui, QtCore, uic
import tela_ensino

class TelaNivel(QtGui.QWidget):
    def __init__(self):
        super(TelaNivel, self).__init__()
        uic.loadUi(os.sep.join(["templates", "tela_nivel.ui"]), self)
        self.tela = None
        
        palette	= QtGui.QPalette()
        cursor = QtGui.QCursor(QtGui.QPixmap('icons\\pointingHand.png'))

        
        self.setAutoFillBackground(True)
        palette.setBrush(self.backgroundRole(),
                         QtGui.QBrush(QtGui.QPixmap("background\\cinza.png").scaled(self.width(), self.height())))
        self.setPalette(palette)

        self.nivel1Button.setCursor(cursor)
        self.nivel2Button.setCursor(cursor)
        self.nivel3Button.setCursor(cursor)
        self.nivel4Button.setCursor(cursor)
        self.nivel5Button.setCursor(cursor)
        self.ajudaBt.setCursor(cursor)

        h = self.nivel1Button.height()
        w = self.nivel1Button.width()
    
        self.nivel1Button.setFlat(True)
        self.nivel1Button.setAutoFillBackground(True)
        palette.setBrush(self.nivel1Button.backgroundRole(),
                         QtGui.QBrush(QtGui.QPixmap("background\\violeta.png").scaled(w, h)))
        self.nivel1Button.setPalette(palette)
        
        self.nivel2Button.setFlat(True)
        self.nivel2Button.setAutoFillBackground(True)
        palette.setBrush(self.nivel2Button.backgroundRole(),
                         QtGui.QBrush(QtGui.QPixmap("background\\verde.png").scaled(w, h)))
        self.nivel2Button.setPalette(palette)

        self.nivel3Button.setFlat(True)
        self.nivel3Button.setAutoFillBackground(True)
        palette.setBrush(self.nivel3Button.backgroundRole(),
                         QtGui.QBrush(QtGui.QPixmap("background\\azul.png").scaled(w, h)))
        self.nivel3Button.setPalette(palette)

        self.nivel4Button.setFlat(True)
        self.nivel4Button.setAutoFillBackground(True)
        palette.setBrush(self.nivel4Button.backgroundRole(),
                         QtGui.QBrush(QtGui.QPixmap("background\\laranja.png").scaled(w, h)))
        self.nivel4Button.setPalette(palette)

        self.nivel5Button.setFlat(True)
        self.nivel5Button.setAutoFillBackground(True)
        palette.setBrush(self.nivel5Button.backgroundRole(),
                         QtGui.QBrush(QtGui.QPixmap("background\\marrom.png").scaled(w, h)))
        self.nivel5Button.setPalette(palette)
        
        self.__conecta_event_btn(self.nivel1Button, "nivel 1")
        self.__conecta_event_btn(self.nivel2Button, "nivel 2")
        self.__conecta_event_btn(self.nivel3Button, "nivel 3")
        self.__conecta_event_btn(self.nivel4Button, "nivel 4")
        self.__conecta_event_btn(self.nivel5Button, "nivel 5")
        self.ajudaBt.clicked.connect(self.ajuda)

    def ajuda(self,e):
        self.a = ajudaTutoriais.TelaAjudaTutoriais()
        self.a.show()
        
    def __conecta_event_btn(self, btn, nivel):
        #Relaciona um botão e um conteúdo a um evento 
        btn.clicked.connect(lambda: self.__envia_nivel_selec(nivel, btn))
        
    def __envia_nivel_selec(self, nivel, btn):
        print os.sep.join(["niveis", nivel,"conts", ""]) # Para debug
        self.tela = tela_ensino.TelaEnsino(cam_cont_nivel=
                                          os.sep.join(["niveis", nivel,
                                                      "conts", ""]), palette=btn.palette())
        self.tela.show()
        self.close()
        

    def closeEvent(self, e):
        self.deleteLater()
        
if __name__ == "__main__":       
    root = QtGui.QApplication([])
    app = TelaNivel()
    app.show()
    root.exec_()

