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
from PyQt4 import QtGui, QtCore
from PyQt4 import phonon
from animated import animated_widget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Player(QtGui.QWidget):
    '''
        Classe representa um player muito simples. Este não possuirá
        ferramenta de volume e fullscreen.
    '''
    def __init__(self, toplevel):
        super(Player, self).__init__()
        self.setParent(toplevel)

        dir_icons = 'icons' + os.sep

        ###############################################################

        self.setObjectName(_fromUtf8("self"))
        self.resize(551, 371)
        self.setStyleSheet(_fromUtf8(""))

        self.reprVideo = phonon.Phonon.VideoPlayer(self)
        self.reprVideo.setGeometry(QtCore.QRect(6, 8, 541, 311))
        self.reprVideo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reprVideo.setMouseTracking(True)
        self.reprVideo.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.reprVideo.setObjectName(_fromUtf8("reprVideo"))

        self.controlSplitter = QtGui.QSplitter(self)
        self.controlSplitter.setGeometry(QtCore.QRect(140, 320, 411, 51))
        self.controlSplitter.setMouseTracking(True)
        self.controlSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.controlSplitter.setObjectName(_fromUtf8("controlSplitter"))

        self.progrWidget = QtGui.QWidget(self.controlSplitter)
        self.progrWidget.setStyleSheet(_fromUtf8("background-color: rgb(63, 63, 63);"))
        self.progrWidget.setObjectName(_fromUtf8("progrWidget"))

        self.gridLayout = QtGui.QGridLayout(self.progrWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.tempoLabel = QtGui.QLabel(self.progrWidget)
        self.tempoLabel.setEnabled(True)

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        self.tempoLabel.setFont(font)
        self.tempoLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.tempoLabel.setObjectName(_fromUtf8("tempoLabel"))

        self.gridLayout.addWidget(self.tempoLabel, 1, 1, 1, 1)

        self.progressoSlider = phonon.Phonon.SeekSlider(self.progrWidget)
        self.progressoSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.progressoSlider.setMouseTracking(False)
        self.progressoSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.progressoSlider.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressoSlider.setStyleSheet(_fromUtf8(""))
        self.progressoSlider.setIconVisible(False)

        self.progressoSlider.setObjectName(_fromUtf8("progressoSlider"))
        self.gridLayout.addWidget(self.progressoSlider, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.volumeSlider = phonon.Phonon.VolumeSlider(self)
        self.volumeSlider.setGeometry(QtCore.QRect(490, 400, 109, 22))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))

        self.horizontalWidget = QtGui.QWidget(self)
        self.horizontalWidget.setGeometry(QtCore.QRect(2, 320, 141, 51))
        self.horizontalWidget.setStyleSheet(_fromUtf8("background-color: rgb(63, 63, 63);"))
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.playButton = QtGui.QPushButton(self.horizontalWidget)
        self.playButton.setStyleSheet(_fromUtf8(""))
        self.playButton.setText(_fromUtf8(""))
        self.playButton.setObjectName(_fromUtf8("playButton"))

        self.horizontalLayout.addWidget(self.playButton)

        self.pauseButton = QtGui.QPushButton(self.horizontalWidget)
        self.pauseButton.setStyleSheet(_fromUtf8(""))
        self.pauseButton.setText(_fromUtf8(""))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))

        self.horizontalLayout.addWidget(self.pauseButton)

        self.playIlustrativoButton = QtGui.QPushButton(self)
        self.playIlustrativoButton.setGeometry(QtCore.QRect(220, 130, 111, 71))
        self.playIlustrativoButton.setText(_fromUtf8(""))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons\\play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.playIlustrativoButton.setIcon(icon)
        self.playIlustrativoButton.setIconSize(QtCore.QSize(500, 500))
        self.playIlustrativoButton.setObjectName(_fromUtf8("playIlustrativoButton"))

        self.setStyleSheet(_fromUtf8("background-color: rgb(63, 63, 63);"))
        self.setWindowTitle("Player")
        self.reprVideo.setToolTip("Play")
        self.tempoLabel.setText(' 00:00:00/00:00:00 ')

        #self.progressoSlider.setToolTip(_translate("playerWidget", "Progresso do video", None))
        self.playButton.setToolTip('Play')
        self.pauseButton.setToolTip('Pause')


            
        ###############################################################
        
        #Layout do player
	#uic.loadUi("templates" + os.sep + "player.ui", self)
        
        cursor = QtGui.QCursor(QtGui.QPixmap('icons\\pointingHand.png'))
	
        self.volumeSlider.setAudioOutput(self.reprVideo.audioOutput())
        self.volumeSlider.setMaximumVolume(0)
        self.volumeSlider.hide()
        
        self.progressoSlider.setMediaObject(self.reprVideo.mediaObject())

        #animated_widget(self.playButton, dir_icons + 'play.gif')
        self.playButton.setIcon(QtGui.QIcon('icons\\play.jpg'))
        self.playButton.setIconSize(QtCore.QSize(45,120))
        #self.playButton.setGeometry(0, 0, 80, 60)
        self.playButton.clicked.connect(self.play)
        self.playIlustrativoButton.clicked.connect(self.play)

        self.pauseButton.setIcon(QtGui.QIcon('icons\\parar1.jpg'))
        self.pauseButton.setIconSize(QtCore.QSize(45,120))
        #animated_widget(self.pauseButton, dir_icons + 'parar.gif')
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
            self.reprVideo.setToolTip("Pause")
            self.reprVideo.play()
            self.__tempo.start()
            

    def pause(self):
        '''
            Pause o video se este estiver em play
        '''
        if self.isCarregado() and  self.reprVideo.isPlaying():
            print "Entrou no pause"
            self.playIlustrativoButton.show()
            self.reprVideo.setToolTip("Play")
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

if __name__=='__main__':
    root = QtGui.QApplication([])
    app = Player(None)
    app.show()
    app.carregar('niveis\\nivel 1\\conts\\Cores\\video\\1- CORES ok.avi')
    root.exec_()
