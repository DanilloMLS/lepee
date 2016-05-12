#-*- coding: cp1252 -*-

'''
    Tela de Avaliação quantitativa
'''

import os
import tela_avl_qualitativa
import avaliacao
from avaliacao import Avaliacao
from player import Player
from PyQt4 import uic, QtCore, QtGui
from PyQt4 import *
from animated_move_button import AnimatedMoveButton

class TelaAvaliacao(QtGui.QMainWindow):
    def __init__(self, nivel="niveis\\nivel 1\\conts\\", Parent = None, palette=None):
        super(TelaAvaliacao, self).__init__()

        uic.loadUi(os.sep.join(["templates","tela_avaliacao.ui"]), self)
        self.__player1 = Player(self.perguntaWidget)

        self.setMouseTracking(True)

        self.setAutoFillBackground(True)
        img = QtGui.QPixmap(palette.button().texture())
        img = img.scaled(QtCore.QSize(self.width(), self.height()))
        palette.setBrush(palette.Background, QtGui.QBrush(img))
        self.setPalette(palette)

        cursor = QtGui.QCursor(QtGui.QPixmap('icons\\pointingHand.png'))

        #criação da avaliação
        self.n = ''
        if nivel == "niveis\\nivel 1\\conts\\":
            self.n = "nivel1"
        elif nivel == "niveis\\nivel 2\\conts\\":
            self.n = "nivel2"
        elif nivel == "niveis\\nivel 3\\conts\\":
            self.n = "nivel3"
        elif nivel == "niveis\\nivel 4\\conts\\":
            self.n = "nivel4"
        else:
            self.n = "nivel5"
        self.aval = Avaliacao(self.n)
        self.q = []
        self.q = avaliacao.gerarQuestionario(self.n)

        #botões das alternativas
        self.alter1Button = AnimatedMoveButton(self, self.q[0].getAlter1()+"\\apresentação1.gif")
        self.alter2Button = AnimatedMoveButton(self, self.q[0].getAlter2()+"\\apresentação1.gif")
        self.alter3Button = AnimatedMoveButton(self, self.q[0].getAlter3()+"\\apresentação1.gif")
        self.alter4Button = AnimatedMoveButton(self, self.q[0].getAlter4()+"\\apresentação1.gif")
        self.alter1Button.setGeometry(70,410,191,171)
        self.alter2Button.setGeometry(320,410,191,171)
        self.alter3Button.setGeometry(570,410,191,171)
        self.alter4Button.setGeometry(820,410,191,171)
        self.alter1Button.show()
        self.alter2Button.show()
        self.alter3Button.show()
        self.alter4Button.show()
        self.alter1Button.setCursor(cursor)
        self.alter2Button.setCursor(cursor)
        self.alter3Button.setCursor(cursor)
        self.alter4Button.setCursor(cursor)

        #radio buttons
        self.group = QtGui.QButtonGroup()
        self.group.addButton(self.radioButton_1)
        self.group.addButton(self.radioButton_2)
        self.group.addButton(self.radioButton_3)
        self.group.addButton(self.radioButton_4)

        #tamanho da janela
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

        self.proxPergButton.setIcon(QtGui.QIcon('icons\\avançar2.jpg'))
        self.proxPergButton.setIconSize(QtCore.QSize(70, 70))
        self.proxPergButton.setCursor(cursor)
        
        self.__player1.carregar(self.q[0].getPerg()+"\\apresentação1.avi")
        
        self.alter1Button.clicked.connect(self.carregaAlternativa1)
        self.alter2Button.clicked.connect(self.carregaAlternativa2)
        self.alter3Button.clicked.connect(self.carregaAlternativa3)
        self.alter4Button.clicked.connect(self.carregaAlternativa4)
        self.proxPergButton.clicked.connect(self.proxPerg)

        
    #carrega vídeos das alternativas
    def carregaAlternativa1(self, e):
        self.radioButton_1.setChecked(True)

    def carregaAlternativa2(self, e):
        self.radioButton_2.setChecked(True)

    def carregaAlternativa3(self, e):
        self.radioButton_3.setChecked(True)

    def carregaAlternativa4(self, e):
        self.radioButton_4.setChecked(True)
    
    def proxPerg(self, e):
        if self.radioButton_1.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked() or self.radioButton_4.isChecked():
            #verifica se o radio button marcado é da resposta certa
            if self.radioButton_1.isChecked():
                if self.q[0].getResp() == self.q[0].getAlter1():
                    self.aval.acertou()
            elif self.radioButton_2.isChecked():
                if self.q[0].getResp() == self.q[0].getAlter2():
                    self.aval.acertou()
            elif self.radioButton_3.isChecked():
                if self.q[0].getResp() == self.q[0].getAlter3():
                    self.aval.acertou()
            elif self.radioButton_4.isChecked():
                if self.q[0].getResp() == self.q[0].getAlter4():
                    self.aval.acertou()
            self.group.setExclusive(False)
            self.radioButton_1.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            self.group.setExclusive(True)
            print self.aval.getNumAcertos()
            print self.q[0].getPerg()
            if len(self.q) > 1:
                self.q.pop(0)
                self.__player1.carregar(self.q[0].getPerg()+"\\apresentação1.avi")
                self.alter1Button.setGif(self.q[0].getAlter1()+"\\apresentação1.gif")
                self.alter2Button.setGif(self.q[0].getAlter2()+"\\apresentação1.gif")
                self.alter3Button.setGif(self.q[0].getAlter3()+"\\apresentação1.gif")
                self.alter4Button.setGif(self.q[0].getAlter4()+"\\apresentação1.gif")

            else:
                #self.q.pop(0)
                print "aval"
                self.__conecta_event_btn(self.proxPergButton, self.n, self.aval.getNumAcertos())
    
    def __conecta_event_btn(self, btn, nivel, acertos):
        print "aval"
        #btn.clicked.connect(lambda: self.__envia_nivel_selec(nivel, acertos))
        
        self.tela = tela_avl_qualitativa.TelaAvalQualitativa(nivel,acertos, palette=self.palette())
        self.tela.show()
        self.close()
        
        
    def __envia_nivel_selec(self, nivel, acertos):
        print "aval"
        self.tela = tela_avl_qualitativa.TelaAvalQualitativa(nivel,acertos)
        self.tela.show()
        self.close()
        

if __name__ == "__main__": 
    root = QtGui.QApplication([])
    app = TelaAvaliacao()
    app.show()
    root.exec_()

