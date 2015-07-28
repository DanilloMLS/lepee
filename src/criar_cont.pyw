#-*- coding: iso-8859-1 -*-

import os
import shutil
from PyQt4 import QtGui, uic, QtCore
import conteudo

class CriarConteudo(QtGui.QDialog):
    def __init__(self, toplevel=None):
        super(CriarConteudo, self).__init__(toplevel)
        uic.loadUi('templates\\criar_cont.ui', self)
        self.criarBtn.clicked.connect(self.criar_cont)
        self.cancelarBtn.clicked.connect(self.close)
        self.procurarImgBtn.clicked.connect(self.carregar_img)
        self.procurarVideoBtn.clicked.connect(self.carregar_video)
        
        self.__dst_img = ''
        self.__dst_video = ''
        self.__carregarTitulos()
        
        self.contProgress.hide()
        self.criandoLabel.hide()

    def __carregar(self, titulo, diretorio, filtro):
        return QtGui.QFileDialog.getOpenFileName(self, titulo, diretorio, filtro)

    def __carregarTitulos(self):
        self.escolheComboBox.clear()
        self.escolheComboBox.addItem('')
        self.escolheComboBox.addItems(conteudo.getTitulos()) #Pega os titulos dos conteudos localizado no conteudo principal
    
    def carregar_img(self):
        cam = self.__carregar('Selecione uma imagem:', self.__dst_img, 'Images(*.png *.gif *.jpg )')
        self.imgLineEdit.setText(cam)

    def carregar_video(self):
        cam = self.__carregar('Selecione um vídeo:', self.__dst_video, 'Videos(*.avi *.mpeg *.flv *.wmv)')
        self.videoLineEdit.setText(cam)

    def limpar(self):
        self.tituloLineEdit.setText('')
        self.videoLineEdit.setText('')
        self.imgLineEdit.setText('')

    def atualiza_cam_busca(self, cam):
        i = cam.find('/')
        
        while i != -1 :
            j = i
            i = cam.find('/', i+1)
        return cam[:j+1]
    
    def copia_arq(self, src, dst):
        shutil.copy(src, dst)

    def criar_cont(self):
        try:
            
            #Exibe o progresso da criação do conteúdo
            self.contProgress.show()
            self.criandoLabel.show()
            
            cam_video = str(self.videoLineEdit.text().toUtf8()).decode('utf8')
            cam_img = str(self.imgLineEdit.text().toUtf8()).decode('utf8')
            

            self.__dst_video = self.atualiza_cam_busca(cam_video)
            self.__dst_img = self.atualiza_cam_busca(cam_img)
        
            titulo = self.escolheComboBox.currentText() #titulo do conteúdo selecionado
            titulo_subcont = str(self.tituloLineEdit.text().toUtf8())
            titulo_subcont = titulo_subcont.strip()
            
            cam_cont_selec = conteudo.getCam_conteudo(titulo)
            
            if not conteudo.cont_existe(cam_cont_selec, titulo_subcont):
                self.contProgress.setValue(15)
                cam_cont_selec = QtCore.QString(cam_cont_selec).toUtf8()
                cam_cont = cam_cont_selec + titulo_subcont
                
                cam_cont = str(cam_cont).decode('utf8')
                
                os.mkdir(cam_cont)
                os.mkdir(cam_cont+'\\conts\\')
                os.mkdir(cam_cont+'\\img\\')
                os.mkdir(cam_cont+'\\video\\')

                self.contProgress.setValue(40)

                self.copia_arq(cam_video, cam_cont+'\\video\\')
                self.contProgress.setValue(80)

                self.copia_arq(cam_img, cam_cont+'\\img\\')
                self.contProgress.setValue(100)
            
        except IOError as io:
            raise io

        finally:
            self.contProgress.setValue(0)
            self.contProgress.hide()
            self.criandoLabel.hide()
            self.__carregarTitulos()
            self.limpar()
            

    def closeEvent(self, e):
        self.deleteLater()
        

root = QtGui.QApplication([])
app = CriarConteudo()
app.show()
root.exec_()
        
