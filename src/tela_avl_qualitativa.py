#-*- coding: cp1252 -*-

'''
    Tela de Avaliação qualitativa
'''

import os
import tela_nivel
import avaliacao
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class TelaAvalQualitativa(QtGui.QMainWindow):
    def __init__(self,nivel="1",numAcertos="1",parent=None, palette=None):
        super(TelaAvalQualitativa, self).__init__()
        cursor = QtGui.QCursor(QtGui.QPixmap('icons\\pointingHand.png'))
        
        #################################################################################################

        self.setObjectName(_fromUtf8("self"))
        self.resize(583, 380)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons\\logo lepe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.salvarButton = QtGui.QPushButton(self.centralwidget)
        self.salvarButton.setGeometry(QtCore.QRect(420, 280, 75, 23))
        self.salvarButton.setObjectName(_fromUtf8("salvarButton"))
        self.salvarButton.setCursor(cursor)

        self.profText = QtGui.QLineEdit(self.centralwidget)
        self.profText.setGeometry(QtCore.QRect(100, 50, 391, 20))
        self.profText.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.profText.setText(_fromUtf8(""))
        self.profText.setObjectName(_fromUtf8("profText"))

        self.alunoText = QtGui.QLineEdit(self.centralwidget)
        self.alunoText.setGeometry(QtCore.QRect(100, 80, 391, 20))
        self.alunoText.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.alunoText.setText(_fromUtf8(""))
        self.alunoText.setObjectName(_fromUtf8("alunoText"))

        self.avalText = QtGui.QTextEdit(self.centralwidget)
        self.avalText.setGeometry(QtCore.QRect(100, 180, 391, 71))
        self.avalText.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.avalText.setObjectName(_fromUtf8("avalText"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 58, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 50, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 155, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 18, 120, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.acertoLabel = QtGui.QLabel(self.centralwidget)
        self.acertoLabel.setGeometry(QtCore.QRect(155, 20, 50, 13))
        self.acertoLabel.setObjectName(_fromUtf8("acertoLabel"))

        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 20, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.nivelLabel = QtGui.QLabel(self.centralwidget)
        self.nivelLabel.setGeometry(QtCore.QRect(204, 20, 46, 13))
        self.nivelLabel.setObjectName(_fromUtf8("nivelLabel"))

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.setWindowTitle("Tela Avaliação Qualitativa LEPÊ")
        self.salvarButton.setText("Salvar")
        self.label.setText("Professor: ")
        self.label_2.setText("Aluno: ")
        self.label_3.setText("Professor, avalie seu aluno: ")
        self.label_4.setText("Número de Acertos: ")
        self.acertoLabel.setText(" 0 ")
        self.label_5.setText("Nível: ")
        self.nivelLabel.setText(" 1")
        ##################################################################################################
        
        #uic.loadUi(os.sep.join(["templates","tela_avl_qualitativa.ui"]), self)
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

