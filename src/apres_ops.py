# -*- coding: cp1252 -*-

'''
    Autor: "Fagner Barros"
    Vers�o: "1.0.1"
    Email: "fagnerluizbarros@gmail.com
    Data de Cria��o: 12/01/2015
    Data da �ltima modifica��o: 10/03/2015
    Vers�o Python: 2.7
    Vers�o do PyQt: 4.8
'''

# importa��es necess�rias para execu��o do m�dulo
from PyQt4 import uic, QtGui, QtCore

class ApresOps(QtGui.QWidget):
    '''
        A classe ApresOps � respons�vel pela exibi��o dos conte�dos em forma de
        um menu de bot�es (sem texto presente s� com imagens de plano de fundo) para
        sele��o posterior. Esta tamb�m carregar� todos os conte�dos de um dado conte�do
        selecionado anteriormente.
    '''
    def __init__(self, toplevel=None):
        super(ApresOps, self).__init__()
        uic.loadUi('templates\\apres_ops.ui', self)
        self.setParent(toplevel)
        self.__signal = QtCore.SIGNAL('ConteudoMudou()')
        self.__cont_atual = None #conte�do atual

    def __setDisplayOps(self, widget):
        #Exibe conte�dos em forma de bot�es
        self.displayScrollArea.setWidget(widget) 

    def __conecta_event_btn(self, btn, cont):
        #Relaciona um bot�o e um conte�do a um evento 
        btn.clicked.connect(lambda: self.setCont_atual(cont))

    def getSignal(self):
        '''
            getSignal() -> str
            Retorna um sinal indicando que o conte�do corrente mudou
        '''
        return self.__signal

    def getCont_atual(self):
        '''
            getCont_atual() -> Conteudo
            Retorna o conte�do corrente
        '''
        return self.__cont_atual

    def setCont_atual(self, cont):
        '''
            Carraga os conte�dos contidos em um dado conteudo. Al�m de enviar um sinal para o cliente da classe avisando
            que o conte�do atual mudou e este deve atualizar a sua apresenta��o
        '''
        self.__cont_atual = cont
        self.carregar_conts(cont.getLista_conts())

        #Envia um sinal avisando que mudou o conte�do corrente
        self.emit(self.getSignal()) 
    
    def carregar_conts(self, conts):
        '''
            Carrega os conte�dos em forma de bot�es com imagens de plano de fundo, para posteriormente serem selecionados.
        '''
        if conts: #Se n�o for um lista vazia
            layout = QtGui.QVBoxLayout()
            widget = QtGui.QWidget()
            for cont in conts:
                btn = QtGui.QPushButton('')
                btn.setToolTip(cont.getTitulo())
                btn.setGeometry(0,0, 80, 80)
                btn.setIcon(QtGui.QIcon(cont.getCam_img()))
                btn.setIconSize(QtCore.QSize(100, 100))
                self.__conecta_event_btn(btn, cont) #Conecta o bot�o a um evento de clique
                layout.addWidget(btn)
            widget.setLayout(layout)
            self.__setDisplayOps(widget) #Exibe o conte�dos carregados

    def resizeEvent(self, e):
        p = self.parent()
        self.setGeometry(0,0, 180, p.height())
