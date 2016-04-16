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

class TelaAvaliacao(QtGui.QMainWindow):
    def __init__(self, nivel, Parent = None):
        super(TelaAvaliacao, self).__init__()

        uic.loadUi(os.sep.join(["templates","tela_avaliacao.ui"]), self)
        self.__player1 = Player(self.perguntaWidget)
        self.__player2 = Player(self.alternativaWidget)
        
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

        #criação da avaliação
        s = ''
        if nivel == "niveis\\nivel 1\\conts\\":
            s = "nivel1"
        elif nivel == "niveis\\nivel 2\\conts\\":
            s = "nivel2"
        elif nivel == "niveis\\nivel 3\\conts\\":
            s = "nivel3"
        elif nivel == "niveis\\nivel 4\\conts\\":
            s = "nivel4"
        else:
            s = "nivel5"

        self.n = s
        self.aval = Avaliacao(s)
        self.q = []
        self.q = avaliacao.gerarQuestionario(s)
        
        self.__player1.carregar(self.q[0].getPerg()+"\\apresentação1.avi")
        self.alter1.clicked.connect(self.carregaAlternativa1)
        self.alter2.clicked.connect(self.carregaAlternativa2)
        self.alter3.clicked.connect(self.carregaAlternativa3)
        self.alter4.clicked.connect(self.carregaAlternativa4)
        self.alter5.clicked.connect(self.carregaAlternativa5)
        self.proxPergButton.clicked.connect(self.proxPerg)

        
    #carrega vídeos das alternativas
    def carregaAlternativa1(self, e):
        if len(self.q) > 0:
            self.__player2.carregar(self.q[0].getAlter1()+"\\apresentação1.avi")

    def carregaAlternativa2(self, e):
        if len(self.q) > 0:
            self.__player2.carregar(self.q[0].getAlter2()+"\\apresentação1.avi")

    def carregaAlternativa3(self, e):
        if len(self.q) > 0:
            self.__player2.carregar(self.q[0].getAlter3()+"\\apresentação1.avi")

    def carregaAlternativa4(self, e):
        if len(self.q) > 0:
            self.__player2.carregar(self.q[0].getAlter4()+"\\apresentação1.avi")

    def carregaAlternativa5(self, e):
        if len(self.q) > 0:
            self.__player2.carregar(self.q[0].getAlter5()+"\\apresentação1.avi")


    
    def proxPerg(self, e):
        if self.radioButton_1.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked() or self.radioButton_4.isChecked() or self.radioButton_5.isChecked():
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
            elif self.radioButton_5.isChecked():
                if self.q[0].getResp() == self.q[0].getAlter5():
                    self.aval.acertou()
                        
            print self.aval.getNumAcertos()
            print self.q[0].getPerg()
            if len(self.q) > 1:
                self.q.pop(0)                
                self.__player1.carregar(self.q[0].getPerg()+"\\apresentação1.avi")
            else:
                #self.q.pop(0)
                self.__conecta_event_btn(self.proxPergButton, self.n, self.aval.getNumAcertos())
    
    def __conecta_event_btn(self, btn, nivel, acertos):
        btn.clicked.connect(lambda: self.__envia_nivel_selec(nivel, acertos))
        
    def __envia_nivel_selec(self, nivel, acertos):
        self.tela = tela_avl_qualitativa.TelaAvalQualitativa(nivel,acertos)
        self.tela.show()
        self.close()
        
'''
root = QtGui.QApplication([])
app = TelaAvaliacao()
app.show()
root.exec_()
'''
