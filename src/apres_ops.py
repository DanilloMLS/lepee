# -*- coding: cp1252 -*-

'''
    Autor: "Fagner Barros"
    Versão: "1.0.1"
    Email: "fagnerluizbarros@gmail.com
    Data de Criação: 12/01/2015
    Data da última modificação: 10/03/2015
    Versão Python: 2.7
    Versão do PyQt: 4.8
'''

# importações necessárias para execução do módulo
from PyQt4 import uic, QtGui, QtCore

class ApresOps(QtGui.QWidget):
    '''
        A classe ApresOps é responsável pela exibição dos conteúdos em forma de
        um menu de botões (sem texto presente só com imagens de plano de fundo) para
        seleção posterior. Esta também carregará todos os conteúdos de um dado conteúdo
        selecionado anteriormente.
    '''
    def __init__(self, toplevel=None):
        super(ApresOps, self).__init__()
        uic.loadUi('templates\\apres_ops.ui', self)
        self.setParent(toplevel)
        self.__signal = QtCore.SIGNAL('ConteudoMudou()')
        self.__cont_atual = None #conteúdo atual

    def __setDisplayOps(self, widget):
        #Exibe conteúdos em forma de botões
        self.displayScrollArea.setWidget(widget) 

    def __conecta_event_btn(self, btn, cont):
        #Relaciona um botão e um conteúdo a um evento 
        btn.clicked.connect(lambda: self.setCont_atual(cont))

    def getSignal(self):
        '''
            getSignal() -> str
            Retorna um sinal indicando que o conteúdo corrente mudou
        '''
        return self.__signal

    def getCont_atual(self):
        '''
            getCont_atual() -> Conteudo
            Retorna o conteúdo corrente
        '''
        return self.__cont_atual

    def setCont_atual(self, cont):
        '''
            Carraga os conteúdos contidos em um dado conteudo. Além de enviar um sinal para o cliente da classe avisando
            que o conteúdo atual mudou e este deve atualizar a sua apresentação
        '''
        self.__cont_atual = cont
        self.carregar_conts(cont.getLista_conts())

        #Envia um sinal avisando que mudou o conteúdo corrente
        self.emit(self.getSignal()) 
    
    def carregar_conts(self, conts):
        '''
            Carrega os conteúdos em forma de botões com imagens de plano de fundo, para posteriormente serem selecionados.
        '''
        if conts: #Se não for um lista vazia
            layout = QtGui.QVBoxLayout()
            widget = QtGui.QWidget()
            for cont in conts:
                btn = QtGui.QPushButton('')
                btn.setToolTip(cont.getTitulo())
                btn.setGeometry(0,0, 80, 80)
                btn.setIcon(QtGui.QIcon(cont.getCam_img()))
                btn.setIconSize(QtCore.QSize(100, 100))
                self.__conecta_event_btn(btn, cont) #Conecta o botão a um evento de clique
                layout.addWidget(btn)
            widget.setLayout(layout)
            self.__setDisplayOps(widget) #Exibe o conteúdos carregados

    def resizeEvent(self, e):
        p = self.parent()
        self.setGeometry(0,0, 180, p.height())
