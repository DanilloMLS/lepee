# -*- coding: cp1252 -*-

import os
from PyQt4 import uic, QtCore, QtGui
from animated import animated_widget
from player import Player
from conteudo import Conteudo


class ApresCont(QtGui.QWidget):
    '''
        Classe resposável pela apresentação de um conteúdo
        em um formato específico
    
    '''
    def __init__(self, toplevel=None, conteudo=None):
        super(ApresCont, self).__init__()
        uic.loadUi("templates" + os.sep + "apres_cont.ui", self) #template da tela de apresentação
        self.setParent(toplevel)
        self.__player = Player(self.videoWidget) #videoWidget é o contenier do template destinado a armazenar o player
        self.__cont_exibido = conteudo

        
        #self.__player.move(0, 40)
        
        '''self.setAutoFillBackground(True)
        img = QtGui.QPixmap(palette.button().texture())
        img = img.scaled(QtCore.QSize(self.width(), self.height()))
        palette.setBrush(palette.Background, QtGui.QBrush(img))
        self.setPalette(palette)'''
        
        self.apresent(conteudo)

        dir_icons = "icons" + os.sep

    
    def __carregar_img(self, cam_img):
        img = QtGui.QPixmap(cam_img)
        label = QtGui.QLabel()
        alt = self.imgScrollArea.widget().height()
        larg = self.imgScrollArea.widget().width()

        img = img.scaled(QtCore.QSize(larg, alt))
        label.setPixmap(img)

        self.imgScrollArea.setWidget(label)

    def getCont_exibido(self):
        return self.__cont_exibido

    def setCont_exibido(self, conteudo):
        self.__cont_exibido = conteudo
    
    def apresent(self, conteudo):
        '''
            Apresenta o conteúdo em um template
        '''
        if isinstance(conteudo, Conteudo):
            self.setCont_exibido(conteudo)
            self.__player.carregar(self.getCont_exibido().getCam_video())
            self.__carregar_img(self.getCont_exibido().getCam_img())
            
    def resizeEvent(self, e):
        '''p = self.parent()
        self.setGeometry(0, 0, p.width(), p.height())

        alt = self.height()
        larg = self.width()

        self.imgScrollArea.setGeometry(larg * 0.40, 0,
                                       larg * 0.2, alt * 0.20)
        
        self.sepAreasLine.setGeometry(larg * 0.04619, alt * 0.23,
                                      larg * 0.9076, 5)
        
        self.videoWidget.setGeometry(larg * 0.16, alt * 0.25,
                                     larg * 0.68, alt * 0.65)

        if self.getCont_exibido() is not None:
            self.__carregar_img(self.getCont_exibido().getCam_img())
        self.__player.resizeEvent(e)'''

    def closeEvent(self, e):
        '''
            Destrói os objetos na janela principal quando está for fechada
        '''
        self.deleteLater()


        
        

