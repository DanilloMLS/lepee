'''
    Autor: "Fagner Barros"
    Versao: "2.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Criacao: 12/01/2015
    Data da ultima modificacao: 20/08/2015

    Dependencias:
        Versao Python: 2.7
        Versao do PyQt: 4.8
'''

from PyQt4 import QtGui, uic
import os
import apres_ops
import conteudo
import apres_cont
import animated_button

class TelaEnsino(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(TelaEnsino, self).__init__()
        print "ENTROUUUU"
        #Template da janela
        #uic.loadUi("templates\\tela_ensino.ui", self)
        uic.loadUi(os.path.join('templates' + os.sep + 'tela_ensino.ui'), self)

        #Cria um botao com um gif animado para indicar a volta ao menu inicial
        #self.__voltarBtn = animated_button.AnimatedButton(self.principalWidget, 'icons\\voltar.gif')
        self.__voltarBtn = animated_button.AnimatedButton(self.principalWidget, 
                                os.path.join('icons' + os.sep + 'voltar.gif'))
        self.__voltarBtn.show()
        self.__voltarBtn.clicked.connect(self.__voltar)
        
        #Cria as areas de menu e apresentacao de conteudo
        self.__apres_ops = apres_ops.ApresOps(self.menuWidget)
        self.__apres_cont= apres_cont.ApresCont(self.apresContWidget)
        self.__conteudoIntr = conteudo.getCont_intr()
        self.getApres_cont().apresent(self.__conteudoIntr)
        
        #Carrega os conteudos no menu
        self.getApres_ops().carregar_conts(self.__conteudoIntr.getLista_conts())

        #Apresenta um novo conteudo selecionado
        self.connect(self.getApres_ops().getMenu(),
                     self.getApres_ops().getSignal(), self.muda_ap_cont)

        self.showMaximized()#Exibe em fullscreen

        #Desabilita o botao maximizar
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

    def __voltar(self):
        self.getApres_ops().carregar_conts(self.__conteudoIntr.getLista_conts())
        
    def muda_ap_cont(self):
        '''
            Apresenta o novo conteudo selecionado
        '''
        self.getApres_cont().apresent(self.getApres_ops().getCont_atual())

    def getApres_ops(self):
        '''
            getApres_ops() -> ApresOp
            retorna a area de menu atual
        '''
        return self.__apres_ops

    def getApres_cont(self):
        '''
            getApres_ops() -> ApresCont
            retorna a area de apresentacao atual
        '''
        return self.__apres_cont
    
    def resizeEvent(self, e):
        '''
            Redimensiona a tela inicial e seus objetos
        '''
        p = self.geometry()
        
        self.apresContWidget.setGeometry(190, 0,
                                         p.width() - 190, p.height())
        
        self.menuWidget.setGeometry(0, 0,
                                    self.menuWidget.width(),
                                    p.height() - 2 * self.__voltarBtn.height())

        self.__voltarBtn.setGeometry(15, self.menuWidget.height() + 10, 150, 80)

        self.sepAreasLine.setGeometry(self.sepAreasLine.x(),
                                      self.sepAreasLine.y(),
                                      self.sepAreasLine.width(), p.height())

        self.getApres_cont().resizeEvent(e)
        self.getApres_ops().resizeEvent(e)

    def closeEvent(self, e):
        '''
            Destroi os objetos na janela principal quando esta for fechada
        '''
        self.deleteLater()
        
'''root = QtGui.QApplication([])
app = TelaEnsino()
app.show()
root.exec_()'''
