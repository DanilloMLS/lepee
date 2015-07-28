# -*- coding: cp1252 -*-

'''
    Autor: "Fagner Barros"
    Vers�o: "2.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Cria��o: 12/01/2015
    Data da �ltima modifica��o: 21/03/2015
    Vers�o Python: 2.7
    Vers�o do PyQt: 4.8
'''

#importa��es necess�rias para execu��o do m�dulo
import os
from PyQt4 import uic, QtGui, QtCore
from PyQt4 import phonon
import animated_button

class Player(QtGui.QWidget):
    '''
        Classe representa um player muito simples. Este n�o possuir�
        ferramenta de volume e fullscreen.
    '''
    def __init__(self, toplevel):
        super(Player, self).__init__()
        self.setParent(toplevel)
        
        #Layout do player
        uic.loadUi('templates\\Player.ui', self)
        self.volumeSlider.setAudioOutput(self.reprVideo.audioOutput())
        self.volumeSlider.setMaximumVolume(0)
        self.volumeSlider.hide()
        
        self.progressoSlider.setMediaObject(self.reprVideo.mediaObject())

        self.__play = animated_button.AnimatedButton(self.botoesWidget, 'icons\\play.gif')
        self.__play.setGeometry(0, 0, 80, 60)
        self.__play.clicked.connect(self.play)

        self.__parar = animated_button.AnimatedButton(self.botoesWidget, 'icons\\parar.gif')
        self.__parar.setGeometry(80, 0, 80, 60)
        self.__parar.clicked.connect(self.pause)

        self.__carregado = False
        self.__tempo = QtCore.QTimer(self) 
        self.__tempo.timeout.connect(self.atualizar_tempo) #Controle do tempo percorrido pelo video em execu��o
        
    def __setCarregado(self, carregado):
        '''
            setCarregado(bool)
            Seta o valor para indicar se o v�deo foi carregado ou n�o
        '''
        self.__carregado = carregado

    
    def __formatar_temp(self, temp):
        '''
            formata_temp(temp) -> str
            Recebe um tempo em milisegundos e retorma este no formato hh:mm:ss
        '''
        #h-hora; m-minuto; s-segundo
        h = temp // 3600000
        temp = temp % 3600000
        m = temp // 60000
        temp = temp % 60000
        s = temp // 1000
        return ' %02d:%02d:%02d ' %(h, m, s)
    
    def isCarregado(self):
        '''
            isCarregado() -> bool
            Retorna se True caso v�deo tenha sido carregado e False caso contr�rio
        '''
        return self.__carregado

    def getTempo_format(self):
        '''
            getTempo_format -> str
            Retorna o tempo do v�deo no formato hh:mm:ss/hh:mm:ss
        '''
        t_corrent = self.__formatar_temp(self.reprVideo.currentTime())
        t_total = self.__formatar_temp(self.reprVideo.totalTime())
        return t_corrent + '/' + t_total
 
    def carregar(self, cam_video):
        '''
            Carrega o video especificado pelo atributo caminho (se este existir) no reprodutor de video.
        '''
        existe = os.path.exists(cam_video)
        if existe:
            cam_midia = phonon.Phonon.MediaSource(cam_video)
            self.reprVideo.load(cam_midia)
            self.__video_atual = cam_video
        else:
            raise ValueError('Caminho especificado n�o existe!') 

        self.__setCarregado(existe) #Se o caminho existir o video ser� carregado

    def reiniciar(self):
        self.__tempo.stop()
        self.reprVideo.stop()
    
    def play(self):
        '''
            Inicia o video ap�s este ter sido carregado atrav�s da fun��o carregar
        '''
        if self.isCarregado() and not self.reprVideo.isPlaying():
            self.reprVideo.play()
            self.__tempo.start()

    def pause(self):
        '''
            Pause o video se este estiver em play
        '''
        if self.isCarregado() and  self.reprVideo.isPlaying():
            self.reprVideo.pause()
            self.__tempo.stop()

    def atualizar_tempo(self):
        '''
            Atualiza o tempo do player a cada instante de reprodu��o
        '''
        
        self.tempoLabel.setText(self.getTempo_format())
        
        #Ao t�rmino do v�deo, este � reiniciado e pausado
        #print self.reprVideo.currentTime()
        if self.reprVideo.isPlaying() and (self.reprVideo.totalTime() == self.reprVideo.currentTime()):
            self.reiniciar()
        
    def mousePressEvent(self, e):
        '''
            Trata o evento de clique do mouse com o bot�o esquerdo na tela do video
        '''
        if e.button() == QtCore.Qt.LeftButton:
            if (e.x() <= self.reprVideo.width()) and (e.y() <= self.reprVideo.height()):
                if not self.reprVideo.isPlaying():
                    self.play()
                else:
                    self.pause()
                    

    def resizeEvent(self, e):
        p = self.parent()
        self.setGeometry(0, 0, p.width(), p.height())
        
        alt_repr = p.height() - self.controlSplitter.height()
        
        self.reprVideo.setGeometry(0, 0, p.width(), alt_repr)
        
        self.controlSplitter.setGeometry(171, alt_repr,
                                       p.width()-171, self.controlSplitter.height())
        
        self.botoesWidget.move(0, alt_repr)

    def closeEvent(self, e):
        '''
            Destr�i os objetos na janela principal quando est� for fechada
        '''
        self.deleteLater()
    

'''root = QtGui.QApplication([])
app = Player()
app.show()
app.carregar('conteudos\\cadeira\\video\\Nirvana MTV Unplugged in New York.mp4')
root.exec_()'''
