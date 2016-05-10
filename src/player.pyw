# -*- coding: cp1252 -*-

'''
    Autor: "Fagner Barros"
    Versão: "2.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Criação: 12/01/2015
    Data da última modificação: 21/03/2015
    Versão Python: 2.7
    Versão do PyQt: 4.8
'''

#importações necessárias para execução do módulo
import os
from PyQt4 import uic, QtGui, QtCore
from PyQt4 import phonon
from animated import animated_widget

class Player(QtGui.QWidget):
    '''
        Classe representa um player muito simples. Este não possuirá
        ferramenta de volume e fullscreen.
    '''
    def __init__(self, toplevel):
        super(Player, self).__init__()
        self.setParent(toplevel)

        dir_icons = 'icons' + os.sep
        
        #Layout do player
	uic.loadUi("templates" + os.sep + "player.ui", self)
        
        cursor = QtGui.QCursor(QtGui.QPixmap('icons\\pointingHand.png'))
	
        self.volumeSlider.setAudioOutput(self.reprVideo.audioOutput())
        self.volumeSlider.setMaximumVolume(0)
        self.volumeSlider.hide()
        
        self.progressoSlider.setMediaObject(self.reprVideo.mediaObject())

        animated_widget(self.playButton, dir_icons + 'play.gif')
        #self.playButton.setGeometry(0, 0, 80, 60)
        self.playButton.clicked.connect(self.play)
        self.playIlustrativoButton.clicked.connect(self.play)

        animated_widget(self.pauseButton, dir_icons + 'parar.gif')
        #self.pauseButton.setGeometry(80, 0, 80, 60)
        self.pauseButton.clicked.connect(self.pause)

        
        self.playButton.setCursor(cursor)
        self.playIlustrativoButton.setCursor(cursor)
        self.pauseButton.setCursor(cursor)
        self.volumeSlider.setCursor(cursor)
        self.progressoSlider.setCursor(cursor)
        self.reprVideo.setCursor(cursor)

        self.__carregado = False
        self.__tempo = QtCore.QTimer(self) 
        self.__tempo.timeout.connect(self.atualizar_tempo) #Controle do tempo percorrido pelo video em execução
        
    def __setCarregado(self, carregado):
        '''
            setCarregado(bool)
            Seta o valor para indicar se o vídeo foi carregado ou não
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
            Retorna se True caso vídeo tenha sido carregado e False caso contrário
        '''
        return self.__carregado

    def getTempo_format(self):
        '''
            getTempo_format -> str
            Retorna o tempo do vídeo no formato hh:mm:ss/hh:mm:ss
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
            self.playIlustrativoButton.show()
            self.reprVideo.load(cam_midia)
            self.__video_atual = cam_video

        else:
            raise ValueError('Caminho especificado não existe!') 

        self.__setCarregado(existe) #Se o caminho existir o video será carregado

    def reiniciar(self):
        self.__tempo.stop()
        self.reprVideo.stop()
        self.playIlustrativoButton.show()
    
    def play(self):
        '''
            Inicia o video após este ter sido carregado através da função carregar
        '''
        if self.isCarregado() and not self.reprVideo.isPlaying():
            print "Entrou no play"
            self.playIlustrativoButton.setHidden(True)
            self.reprVideo.play()
            self.__tempo.start()

    def pause(self):
        '''
            Pause o video se este estiver em play
        '''
        if self.isCarregado() and  self.reprVideo.isPlaying():
            print "Entrou no pause"
            self.playIlustrativoButton.show()
            self.reprVideo.pause()
            self.__tempo.stop()

    def atualizar_tempo(self):
        '''
            Atualiza o tempo do player a cada instante de reprodução
        '''
        
        self.tempoLabel.setText(self.getTempo_format())
        
        #Ao término do vídeo, este é reiniciado e pausado
        #print self.reprVideo.currentTime()
        if self.reprVideo.isPlaying() and (self.reprVideo.totalTime() == self.reprVideo.currentTime()):
            self.reiniciar()
        
    def mousePressEvent(self, e):
        '''
            Trata o evento de clique do mouse com o botão esquerdo na tela do video
        '''
        if e.button() == QtCore.Qt.LeftButton:
            if (e.x() <= self.reprVideo.width()) and (e.y() <= self.reprVideo.height()):
                if not self.reprVideo.isPlaying():
                    self.play()
                else:
                    self.pause()
                    

    def resizeEvent(self, e):
        '''p = self.parent()
        self.setGeometry(0, 0, p.width(), p.height())
        
        alt_repr = p.height() - self.controlSplitter.height()
        
        self.reprVideo.setGeometry(0, 0, p.width(), alt_repr)
        
        self.controlSplitter.setGeometry(171, alt_repr,
                                       p.width()-171, self.controlSplitter.height())
        
        self.botoesWidget.move(0, alt_repr)'''

    def closeEvent(self, e):
        '''
            Destrói os objetos na janela principal quando está for fechada
        '''
        self.deleteLater()
    

'''root = QtGui.QApplication([])
app = Player()
app.show()
app.carregar('conteudos\\cadeira\\video\\Nirvana MTV Unplugged in New York.mp4')
root.exec_()'''
