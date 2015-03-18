# -*- coding: cp1252 -*-

#importações necessárias para execução do módulo
import os
from PyQt4 import uic, QtGui, QtCore
from PyQt4 import phonon

class Player(QtGui.QWidget):
    def __init__(self, toplevel=None):
        super(Player, self).__init__()
        self.setParent(toplevel)
        
        #Layout do player
        uic.loadUi('templates\\Player.ui', self)
        self.volumeSlider.setAudioOutput(self.reprVideo.audioOutput())
        self.volumeSlider.setMaximumVolume(0)
        self.volumeSlider.hide()
        self.progressoSlider.setMediaObject(self.reprVideo.mediaObject())
        self.playBtn.clicked.connect(self.play)
        self.playBtn.setToolTip('Play')
        self.pauseBtn.clicked.connect(self.pause)
        self.pauseBtn.setToolTip('Pause')
        self.reprVideo.finished.connect(self.reprVideo.stop)
        
        self.__carregado = False
        self.__video_atual = ''
        self.__tempo = QtCore.QTimer(self) 
        self.__tempo.timeout.connect(self.atualizar_tempo) #Controle do tempo percorrido pelo video em execução
        

    def __setCarregado(self, carregado):
        '''
            setCarregado(bool)
            Seta o valor para indicar se o vídeo foi carregado ou não
        '''
        self.__carregado = carregado
    
    def isCarregado(self):
        '''
            isCarregado() -> bool
            Retorna se True caso vídeo tenha sido carregado e False caso contrário
        '''
        return self.__carregado

    def getVideo_atual(self):
        '''
            getVideo_atual() -> str
            Retorna o caminho do vídeo corrente
        '''
        return self.__video_atual

    def formatar_temp(self, temp):
        '''
            formata_temp(temp) -> str
            Recebe um tempo em milisegundos e retorma este no formato hh:mm:ss
        '''
        h = temp // 3600000
        temp = temp % 3600000
        m = temp // 60000
        temp = temp % 60000
        s = temp // 1000
        return ' %02d:%02d:%02d ' %(h, m, s)


    def getTempo_format(self):
        '''
            getTempo_format -> str
            Retorna o tempo do vídeo no formato hh:mm:ss/hh:mm:ss
        '''
        t_corrent = self.formatar_temp(self.reprVideo.currentTime())
        t_total = self.formatar_temp(self.reprVideo.totalTime())
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
            raise ValueError('Caminho especificado não existe!') 

        self.__setCarregado(existe) #Se o caminho existir o video será carregado
    
    def play(self):
        '''
            Inicia o video após este ter sido carregado através da função carregar
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
            Atualiza o tempo do player a cada instante de reprodução
        '''
        
        self.tempoLabel.setText(self.getTempo_format())
        
    def mousePressEvent(self, e):
        '''
            Trata o evento de clique do mouse com o botão esquerdo na tela do video
        '''
        if e.button() == QtCore.Qt.LeftButton:
            if (e.x() <= self.reprVideo.width()) and (e.y() <= self.reprVideo.height()):
                if not self.reprVideo.isPlaying():
                    self.play()
                    self.reprVideo.setToolTip('Pause')
                else:
                    self.pause()
                    self.reprVideo.setToolTip('Play')

    '''def resizeEvent(self, e):
        self.reprVideo.setGeometry(0, 0, self.width(), self.height() - 65)
        self.progrWidget.setGeometry(10, self.height() - 65, self.width() - 20, self.progrWidget.height())
        self.controlWidget.move(10, self.reprVideo.height() + self.progrWidget.height())'''
    

root = QtGui.QApplication([])
app = Player()
app.show()
app.carregar('conteudos\\conts\\cadeira\\video\\Nirvana MTV Unplugged in New York.mp4')
root.exec_()
