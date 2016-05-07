#-*- coding: cp1252 -*-

'''
    Tela de Avaliação qualitativa
'''

import os
import tela_nivel
import avaliacao
from PyQt4 import uic, QtCore, QtGui

class TelaAvalQualitativa(QtGui.QMainWindow):
    def __init__(self,nivel="1",numAcertos="1",parent=None, palette=None):
        super(TelaAvalQualitativa, self).__init__()
        uic.loadUi(os.sep.join(["templates","tela_avl_qualitativa.ui"]), self)
        #print nivel
        #print numAcertos


        self.setAutoFillBackground(True)
        img = QtGui.QPixmap(palette.button().texture())
        img = img.scaled(QtCore.QSize(self.width(), self.height()))
        palette.setBrush(palette.Background, QtGui.QBrush(img))
        self.setPalette(palette)

        self.profText.setStyleSheet("QLineEdit {font-size: 10pt; font-family: Arial; color: black}")
        self.alunoText.setStyleSheet("QLineEdit {font-size: 10pt; font-family: Arial; color: black}")
        self.avalText.setStyleSheet("QTextEdit {font-size: 10pt; font-family: Arial; color: black}")
        self.salvarButton.setStyleSheet("QPushButton {font-size: 10pt; font-family: Arial; color: black}")
        #self.profText.setStyleSheet("QLineEdit {color: blue}")

        self.nivelLabel.setText(nivel)
        self.acertoLabel.setText(str(numAcertos))
        self.nivel = nivel
        self.numAcertos = str(numAcertos)
        
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

        self.salvarButton.clicked.connect(self.salvar_avaliacao)

    def salvar_avaliacao(self, e):
        profe = self.profText.text()
        aluno = self.alunoText.text()
        aval = self.avalText.toPlainText()

        arquivo = open("avaliacoes/avaliacao.txt","r")
        conteudo = arquivo.readlines()
        arquivo = open("avaliacoes/avaliacao.txt","w")
        conteudo.append("\n===============================")
        conteudo.append("\nNível: "+self.nivel)
        conteudo.append("\n")
        conteudo.append("Número de Acertos: "+self.numAcertos)
        conteudo.append("\n")
        conteudo.append("Professor: "+profe)
        conteudo.append("\n")
        conteudo.append("Aluno: "+aluno)
        conteudo.append("\n")
        conteudo.append("Avaliação: "+aval)
        arquivo.writelines(conteudo)
        '''
        arquivo=open("avaliacoes/avaliacao.txt","w")
        arquivo.write("Nível: "+self.nivel)
        arquivo.write("\n")
        arquivo.write("Número de Acertos: "+self.numAcertos)
        arquivo.write("\n")
        arquivo.write("Professor: "+profe)
        arquivo.write("\n")
        arquivo.write("Aluno: "+aluno)
        arquivo.write("\n")
        arquivo.write("Avaliação: "+aval)
        '''
        arquivo.close()
        self.close()

        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()

    
    def abre_tela_nivel(self, e):
        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()


if __name__ == "__main__": 
    root = QtGui.QApplication([])
    app = TelaAvalQualitativa()
    app.show()
    root.exec_()

