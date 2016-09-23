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
from PyQt4 import QtGui, QtCore
import tela_ensino

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class TelaNivel(QtGui.QWidget):
    def __init__(self):
        super(TelaNivel, self).__init__()

        #############################################################
        self.setObjectName(_fromUtf8("self"))
        self.resize(419, 212)
        self.setMinimumSize(QtCore.QSize(419, 212))
        self.setMaximumSize(QtCore.QSize(419, 212))
        

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons\\logo lepe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setWindowIcon(icon)
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 201))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.nivel3Button = QtGui.QPushButton(self.widget)
        self.nivel3Button.setGeometry(QtCore.QRect(280, 10, 101, 81))
        self.nivel3Button.setStyleSheet(_fromUtf8("font: 48pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);"))
        self.nivel3Button.setObjectName(_fromUtf8("nivel3Button"))

        self.nivel4Button = QtGui.QPushButton(self.widget)
        self.nivel4Button.setGeometry(QtCore.QRect(20, 110, 101, 81))
        self.nivel4Button.setStyleSheet(_fromUtf8("font: 48pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);"))
        self.nivel4Button.setObjectName(_fromUtf8("nivel4Button"))

        self.nivel5Button = QtGui.QPushButton(self.widget)
        self.nivel5Button.setGeometry(QtCore.QRect(150, 110, 101, 81))
        self.nivel5Button.setStyleSheet(_fromUtf8("font: 48pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);"))
        self.nivel5Button.setObjectName(_fromUtf8("nivel5Button"))

        self.nivel2Button = QtGui.QPushButton(self.widget)
        self.nivel2Button.setGeometry(QtCore.QRect(150, 10, 101, 81))
        self.nivel2Button.setStyleSheet(_fromUtf8("font: 48pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);"))
        self.nivel2Button.setObjectName(_fromUtf8("nivel2Button"))

        self.nivel1Button = QtGui.QPushButton(self.widget)
        self.nivel1Button.setGeometry(QtCore.QRect(20, 10, 101, 81))
        self.nivel1Button.setMinimumSize(QtCore.QSize(101, 81))
        self.nivel1Button.setMaximumSize(QtCore.QSize(101, 16777215))
        self.nivel1Button.setStyleSheet(_fromUtf8("font: 48pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);"))
        self.nivel1Button.setObjectName(_fromUtf8("nivel1Button"))

        self.ajudaBt = QtGui.QPushButton(self.widget)
        self.ajudaBt.setGeometry(QtCore.QRect(340, 160, 41, 31))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.ajudaBt.setFont(font)
        self.ajudaBt.setObjectName(_fromUtf8("ajudaBt"))
        
        self.nivel3Button.setText("3")
        self.nivel4Button.setText("4")
        self.nivel5Button.setText("5")
        self.nivel2Button.setText("2")
        self.nivel1Button.setText("1")

        '''self.nivel3Button.setToolTip("Nível de Liguagem Compreensiva 3")
        self.nivel4Button.setToolTip("Nível de Liguagem Compreensiva 4")
        self.nivel5Button.setToolTip("Nível de Liguagem Compreensiva 5")
        self.nivel2Button.setToolTip("Nível de Liguagem Compreensiva 2")
        self.nivel1Button.setToolTip("NFagner")'''

        self.setWindowTitle("Tela de Seleção de Nível LEPÊ")
        self.ajudaBt.setText("?")
        self.ajudaBt.setToolTip("Ajuda")

        #############################################################

        #uic.loadUi(os.sep.join(["templates", "tela_nivel.ui"]), self)
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

