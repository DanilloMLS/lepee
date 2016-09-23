# -*- coding: cp1252 -*-

'''
    Autor: "Fagner Barros"
    Vers�o: "2.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Cria��o: 12/01/2015
    Data da �ltima modifica��o: 23/03/2015
    Vers�o Python: 2.7
    Vers�o do PyQt: 4.8
'''

# importa��es necess�rias para execu��o do m�dulo
import os
from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class ApresOps(object):
    '''
        A classe ApresOps � respons�vel pela exibi��o dos conte�dos em forma de
        um menu de bot�es (sem texto presente, s� com imagens de plano de fundo)
        para sele��o posterior. Esta tamb�m carregar� todos os conte�dos de um
        dado conte�do selecionado previamente.
    '''
    def __init__(self, toplevel=None):
        self.__menu = QtGui.QWidget(toplevel) #Menu para sele��o de conte�dos
        #uic.loadUi("templates" + os.sep + "apres_ops.ui", self.getMenu()) #Templete

        ##################################################################
        self.getMenu().setObjectName(_fromUtf8("self.getMenu()"))
        self.getMenu().resize(209, 551)
        self.getMenu().setStyleSheet(_fromUtf8("background-color: rgb(63, 63, 63);"))
        self.gridLayout = QtGui.QGridLayout(self.getMenu())
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.opWidget = QtGui.QWidget(self.getMenu())
        self.opWidget.setObjectName(_fromUtf8("opWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.opWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.displayScrollArea = QtGui.QScrollArea(self.opWidget)
        self.displayScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.displayScrollArea.setWidgetResizable(True)
        self.displayScrollArea.setObjectName(_fromUtf8("displayScrollArea"))
        self.scrAWidgetContents = QtGui.QWidget()
        self.scrAWidgetContents.setGeometry(QtCore.QRect(0, 0, 171, 513))
        self.scrAWidgetContents.setObjectName(_fromUtf8("scrAWidgetContents"))
        self.displayScrollArea.setWidget(self.scrAWidgetContents)
        self.verticalLayout_2.addWidget(self.displayScrollArea)
        self.gridLayout.addWidget(self.opWidget, 0, 0, 1, 1)

        #self.getMenu().setWindowTitle("tempAprQWidget")
        ##################################################################

        self.__signal = QtCore.SIGNAL('ConteudoMudou()')
        self.__cont_atual = None #conte�do atual

    def __setDisplayOps(self, widget):
        #Exibe conte�dos em forma de bot�es
        self.displayScrollArea.setWidget(widget) 

    def __conecta_event_btn(self, btn, cont):
        #Relaciona um bot�o e um conte�do a um evento 
        btn.clicked.connect(lambda: self.setCont_atual(cont))

    def getMenu(self):
        '''
        getMenu() -> QWidget
        retorna um Menu para sele��o de conte�dos na forma de uma lista de
        bot�es (no caso de existir algum conte�do criado previamente)  com
        imagens de backgroud.
        '''
        return self.__menu
    def getSignal(self):
        '''
            getSignal() -> str
            Retorna o tipo de sinal enviando quando o conte�do corrente muda
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
            Carraga os conte�dos contidos em um dado conte�do. Al�m de enviar um
            sinal para o cliente da classe avisando que o conte�do atual mudou
            e este deve atualizar a sua apresenta��o
        '''
        self.__cont_atual = cont
        print cont.hasSubConts()

        if cont.hasSubConts():
            self.carregar_conts(cont.getLista_conts())

        #Envia um sinal avisando que mudou o conte�do corrente
        self.getMenu().emit(self.getSignal()) 
    
    def carregar_conts(self, conts):
        '''
            Carrega os conte�dos em forma de bot�es com imagens de plano de fundo,
            para posteriormente serem selecionados.
        '''
        #print conts # para debug
        if conts: #Se n�o for um lista vazia
            layout = QtGui.QVBoxLayout()
            widget = QtGui.QWidget()
            cursor = QtGui.QCursor(QtGui.QPixmap('icons\\pointingHand.png'))
            for cont in conts:
                btn = QtGui.QPushButton('')
                btn.setToolTip(cont.getTitulo())
                btn.setIcon(QtGui.QIcon(cont.getCam_img()))
                btn.setIconSize(QtCore.QSize(150, 100))
                btn.setCursor(cursor)
                self.__conecta_event_btn(btn, cont) #Conecta o bot�o a um evento de clique
                layout.addWidget(btn)
            widget.setLayout(layout)
            self.__setDisplayOps(widget) #Exibe o conte�dos carregados

    def resizeEvent(self, e):
        '''p = self.getMenu().parent()
        self.getMenu().setGeometry(0,0, 180, p.height())'''
