# -*- coding: cp1252 -*-

'''
    Autor: "Danillo Moraes"
    Versão: "2.0.0"
    Email: "moraesdanillo10@gmail.com
    Data de Criação: 28/10/2015
    Data da última modificação: 12/02/2016
    Autor da úlitma mod: Danillo Moraes
    Versão Python: 2.7
    Versão do PyQt: 4.8
'''
import os
import time
from PyQt4 import QtGui, QtCore
from animated import animated_widget
import tela_nivel
#import tela_login
import ajudaTutoriais

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class TelaIntro(QtGui.QMainWindow):
    def __init__(self,parent=None):

        super(TelaIntro,self).__init__()

        ########################################################################
        
        self.setObjectName(_fromUtf8("self"))
        self.setEnabled(True)
        self.resize(786, 546)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons\\logo lepe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 300, 731, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 20, 481))
        self.line_3.setStyleSheet(_fromUtf8(""))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))

        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(760, 20, 20, 491))
        self.line_4.setStyleSheet(_fromUtf8(""))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))

        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(20, 490, 751, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))

        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(20, 10, 751, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))

        self.profButton = QtGui.QPushButton(self.centralwidget)
        self.profButton.setGeometry(QtCore.QRect(320, 340, 171, 141))
        self.profButton.setText(_fromUtf8(""))
        self.profButton.setObjectName(_fromUtf8("profButton"))
        self.profButton.setToolTip("Ir para a plataforma do Professor")

        self.introLabel = QtGui.QLabel(self.centralwidget)
        self.introLabel.setGeometry(QtCore.QRect(140, 40, 501, 251))
        self.introLabel.setText(_fromUtf8(""))
        self.introLabel.setObjectName(_fromUtf8("introLabel"))

        self.ajudaBt = QtGui.QPushButton(self.centralwidget)
        self.ajudaBt.setGeometry(QtCore.QRect(730, 30, 31, 31))

        font = QtGui.QFont()
        font.setPointSize(18)

        self.ajudaBt.setFont(font)
        self.ajudaBt.setObjectName(_fromUtf8("ajudaBt"))
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.setWindowTitle("Tela de Introdução LEPÊ")
        self.ajudaBt.setText("?")
        self.ajudaBt.setToolTip("Ajuda")

        ########################################################################
        
        #uic.loadUi("templates" + os.sep + "tela_intro.ui", self)
        dir_icons = "icons" + os.sep
        
        cursor = QtGui.QCursor(QtGui.QPixmap(dir_icons + 'pointingHand.png'))

        '''animated_widget(self.alunoButton, dir_icons + 'parar.gif')
        self.alunoButton.setGeometry(self.alunoButton.x(), self.alunoButton.y(), 251, 200)
        self.alunoButton.setCursor(cursor)
        self.alunoButton.show()'''

        palette = QtGui.QPalette()
        self.setAutoFillBackground(True)
        img = QtGui.QPixmap("background\\introducao.jpg")
        img = img.scaled(QtCore.QSize(self.width(), self.height()))
        palette.setBrush(palette.Background, QtGui.QBrush(img))
        self.setPalette(palette)

        self.profButton.setIcon(QtGui.QIcon('icons\\Viviane.jpg'))
        self.profButton.setIconSize(QtCore.QSize(160,200))
        #animated_widget(self.profButton, dir_icons + 'parar.gif')
        #self.profButton.setGeometry(self.profButton.x(), self.profButton.y(), 251, 200)
        self.profButton.setCursor(cursor)
        self.profButton.show()
    
        animated_widget(self.introLabel, dir_icons + 'apres.gif')
        self.introLabel.setGeometry(self.introLabel.x(), self.introLabel.y(),
                                    self.introLabel.width(), self.introLabel.height())
        self.introLabel.show()
        
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

        #self.alunoButton.clicked.connect(self.abre_tela_nivelEvent)
        self.profButton.clicked.connect(self.abre_tela_login)

        self.ajudaBt.setCursor(cursor)
        self.ajudaBt.clicked.connect(self.ajuda)

    def ajuda(self,e):
        self.a = ajudaTutoriais.TelaAjudaTutoriais()
        self.a.show()
        
    def abre_tela_nivelEvent(self, e):
        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()
    
    def abre_tela_login(self, e):
        self.a = tela_nivel.TelaNivel()
        self.a.show()

        self.close()
    
    def closeEvent(self, e):
        '''
            Destrói os objetos na janela principal quando está for fechada
        '''
        self.deleteLater()


if __name__ == "__main__":        
    root = QtGui.QApplication([])
    app = TelaIntro()
    splash_pix = QtGui.QPixmap("background\\abertura.png")
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    
    splash.setMask(splash_pix.mask())
    splash.show()
    root.processEvents()

    time.sleep(5)
    
    
    splash.finish(app)
    app.show()
    
    root.exec_()

        
