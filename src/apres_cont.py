# -*- coding: cp1252 -*-

from PyQt4 import uic, QtCore, QtGui
from player import Player
from conteudo import Conteudo


'''
    Classe resposável pela apresentação de um conteúdo
    
'''
class ApresentaCont(QtGui.QDockWidget):
    def __init__(self, topleveal=None, conteudo=None):
        super(ApresentaCont, self).__init__()
        uic.loadUi('templates\\AprCont.ui', self)
        self.setParent(topleveal)
        self.__player = Player(self.contWidget)
        self.__player.hide()
        self.__imgAtual = ''
        self.apresent(conteudo)
        
    '''
        Apresenta o conteúdo em um template
    '''
    def apresent(self, conteudo):
        if isinstance(conteudo, Conteudo):
            self.tituloLabel.setText(conteudo.getTitulo())
            self.setWindowTitle(conteudo.getTitulo())

            self.__imgAtual = conteudo.getCam_img()
            p = QtGui.QPixmap(conteudo.getCam_img())
            alt = self.imgLabel.height()
            larg = self.imgLabel.width()
            self.imgLabel.setPixmap(p.scaled(QtCore.QSize(alt, larg)))
            
            self.assistLabel.setText('Assista o Vídeo a baixo:')
            self.textoEdit.setText(conteudo.getTexto())
            
            self.__player.carregar(conteudo.getCam_video())
            if self.__player.isCarregado():
                self.__player.show()
            else:
                self.__player.hide()
                self.assistLabel.setText('Não possui Video!')


    def resizeEvent(self, e):
        p = self.parent()
        self.setGeometry(180, 0, p.width() - 180, p.height())
        self.contWidget.setGeometry(0, 0, self.width() * 0.34, self.height())

        self.textoEdit.setGeometry(self.contWidget.width(), 0, self.width() * 0.66, self.height())
        self.assistLabel.move(self.contWidget.width()*0.02, self.contWidget.height() * 0.39)
        self.tituloLabel.move(self.contWidget.width()*0.03, self.contWidget.width()*0.017)

        self.__player.setGeometry(0, self.contWidget.height() * 0.45, self.contWidget.width(), self.contWidget.height() * 0.4)

        img = QtGui.QPixmap(self.__imgAtual)
        if img != None:
            self.imgLabel.setGeometry(self.contWidget.width() * 0.25, self.contWidget.height() * 0.05, self.contWidget.width() * 0.5, self.contWidget.height() * 0.35)
            alt = self.imgLabel.height()
            larg = self.imgLabel.width()
            self.imgLabel.setPixmap(img.scaled(QtCore.QSize(alt, larg)))
            
        

        
        
        
        

