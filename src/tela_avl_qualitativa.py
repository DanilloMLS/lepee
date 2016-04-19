#-*- coding: cp1252 -*-

'''
    Tela de Avalia��o qualitativa
'''

import os
import tela_nivel
import avaliacao
from PyQt4 import uic, QtCore, QtGui

class TelaAvalQualitativa(QtGui.QMainWindow):
    def __init__(self,nivel,numAcertos,parent=None):
        super(TelaAvalQualitativa, self).__init__()
        uic.loadUi(os.sep.join(["templates","tela_avl_qualitativa.ui"]), self)
        #print nivel
        #print numAcertos
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
        profe = str(self.profText.text().toUtf8()).decode('utf8')
        aluno = str(self.alunoText.text().toUtf8()).decode('utf8')
        aval = str(self.avalText.toPlainText())

        arquivo = open("avaliacoes/avaliacao.txt","r")
        conteudo = arquivo.readlines()
        arquivo = open("avaliacoes/avaliacao.txt","w")
        conteudo.append("\n===============================")
        conteudo.append("\nN�vel: "+self.nivel)
        conteudo.append("\n")
        conteudo.append("N�mero de Acertos: "+self.numAcertos)
        conteudo.append("\n")
        conteudo.append("Professor: "+profe)
        conteudo.append("\n")
        conteudo.append("Aluno: "+aluno)
        conteudo.append("\n")
        conteudo.append("Avalia��o: "+aval)
        arquivo.writelines(conteudo)
        '''
        arquivo=open("avaliacoes/avaliacao.txt","w")
        arquivo.write("N�vel: "+self.nivel)
        arquivo.write("\n")
        arquivo.write("N�mero de Acertos: "+self.numAcertos)
        arquivo.write("\n")
        arquivo.write("Professor: "+profe)
        arquivo.write("\n")
        arquivo.write("Aluno: "+aluno)
        arquivo.write("\n")
        arquivo.write("Avalia��o: "+aval)
        '''
        arquivo.close()
        self.close()
    
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
