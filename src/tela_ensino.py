# -*- coding: cp1252 -*-
from PyQt4 import QtGui, QtCore, uic
import apres_ops
import conteudo

class TelaEnsino(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(TelaEnsino, self).__init__()
        uic.loadUi("templates\\tela_ensino.ui", self)
        self.__apres_ops = apres_ops.ApresOps(self)
        
        
        self.getApres_ops().carregar_conts(conteudo.getLista_conteudos('conteudos\\conts\\'))
        self.connect(self.getApres_ops(),
                     self.getApres_ops().getSignal(), self.muda_ap_cont)

    def muda_ap_cont(self):
        '''
            Apresenta o novo conteúdo selecionado
        '''
        print 'fagfafaf'

    def getApres_ops(self):
        return self.__apres_ops
    
    '''def resizeEvent(self, e):
        self.__ap.resizeEvent(e)
        self.__ap_ops.resizeEvent(e)'''

    '''
        Destrói os objetos na janela principal quando está for fechada
    '''
    def closeEvent(self, e):
        self.deleteLater()
        
root = QtGui.QApplication([])
app = TelaEnsino()
app.show()
root.exec_()
