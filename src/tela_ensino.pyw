# -*- coding: cp1252 -*-

'''
    Autor: "Fagner Barros"
    Versão: "2.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Criação: 12/01/2015
    Data da última modificação: 20/08/2015
    Versão Python: 2.7
    Versão do PyQt: 4.8
'''
import os
from PyQt4 import QtGui, QtCore, uic
import apres_ops
import conteudo
import apres_cont
from animated import animated_widget

class TelaEnsino(QtGui.QMainWindow):
    def __init__(self, parent=None, cam_cont_nivel=''):
        super(TelaEnsino, self).__init__()
        print "Entrou na Tela de Ensino"
        print cam_cont_nivel
        self.setParent(parent)
                       
        #Template da janela
        #os.sep = separador de diretorios do SO
        uic.loadUi(os.sep.join(["templates","tela_ensino.ui"]), self)

        #Cria um botão com um gif animado para indicar a volta ao menu inicial
        animated_widget(self.voltarButton,
                       os.sep.join(['icons','voltar.gif']))
        #self.voltarButton.show()
        self.voltarButton.clicked.connect(self.__voltar) 

        #Cria as áres de menu e apresentação de conteúdo
        self.__apres_ops = apres_ops.ApresOps(self.menuWidget)
        self.__apres_cont= apres_cont.ApresCont(self.apresContWidget)
        self.__apres_cont.hide()
        self.__conteudos = conteudo.getLista_conts(cam_cont_nivel)
        
        #Carrega os conteúdos no menu
        self.getApres_ops().carregar_conts(self.__conteudos)

        #Apresenta um novo conteúdo selecionado
        self.connect(self.getApres_ops().getMenu(),
                     self.getApres_ops().getSignal(), self.muda_ap_cont)

        #self.showMaximized()#Exibe em fullscreen

        #Desabilita o botão maximizar
        
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())
        
    def __voltar(self):
        self.getApres_ops().carregar_conts(self.__conteudos)
        
    def muda_ap_cont(self):
        '''
            Apresenta o novo conteudo selecionado
        '''
        if self.getApres_cont().isHidden():
            self.getApres_cont().show()
        self.getApres_cont().apresent(self.getApres_ops().getCont_atual())

    def getApres_ops(self):
        '''
            getApres_ops() -> ApresOp
            retorna a área de menu atual
        '''
        return self.__apres_ops

    def getApres_cont(self):
        '''
            getApres_ops() -> ApresCont
            retorna a área de apresentação atual
        '''
        return self.__apres_cont
    
    def resizeEvent(self, e):
        '''
            Redimensiona a tela inicial e seus objetos
        '''
        '''p = self.geometry()
        
        self.apresContWidget.setGeometry(190, 0,
                                         p.width() - 190, p.height())
        
        self.menuWidget.setGeometry(0, 0,
                                    self.menuWidget.width(),
                                    p.height() - 2 * self.voltarButton.height())

        self.voltarButton.setGeometry(15, self.menuWidget.height() + 10,
                                      150, 80)

        self.sepAreasLine.setGeometry(self.sepAreasLine.x(),
                                      self.sepAreasLine.y(),
                                      self.sepAreasLine.width(),
                                      p.height())
        
        self.getApres_cont().resizeEvent(e)
        self.getApres_ops().resizeEvent(e)'''

    def closeEvent(self, e):
        '''
            Destroi os objetos na janela principal quando esta for fechada
        '''
        self.deleteLater()
        
if __name__ == "__main__":    
    root = QtGui.QApplication([])
    app = TelaEnsino()
    app.show()
    root.exec_()
