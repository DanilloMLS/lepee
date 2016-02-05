#-*- coding: iso-8859-1 -*-

import os
import shutil
from PyQt4 import QtGui, uic, QtCore
import conteudo

class CriarConteudo(QtGui.QDialog):
    def __init__(self, toplevel=None):
        super(CriarConteudo, self).__init__(toplevel)
        #uic.loadUi('templates\\criar_cont.ui', self)
        uic.loadUi('templates' + os.sep + 'criar_cont.ui', self)
        self.criarBtn.clicked.connect(self.criar_cont)
        self.cancelarBtn.clicked.connect(self.close)
        self.procurarImgBtn.clicked.connect(self.carregar_img)
        self.procurarVideoBtn.clicked.connect(self.carregar_video)
        
        self.__dst_img = ''
        self.__dst_video = ''
        print "testando saida"
        self.__carregarTitulos()
        

        
        self.contProgress.hide()
        self.criandoLabel.hide()
        self.errorLabel.hide()
        
    def __carregar(self, titulo, diretorio, filtro):
        return QtGui.QFileDialog.getOpenFileName(self, titulo, diretorio, filtro)

    def __carregarTitulos(self):
        self.escolheComboBox.clear()
        self.escolheComboBox.addItem('')
        #Pega os titulos dos conteudos localizado no conteudo principal
        
        
        msg = ""
        for i in os.listdir('conteudos'):
            msg += str(i) + ","
        msg = msg[:-1]
        
        print msg
             
        
        self.escolheComboBox.addItems(conteudo.getTitulos()) 
    
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
        #i = cam.find('/')
        i = cam.find(os.sep)
        j = i
        while i != -1 :
            j = i
            #i = cam.find('/', i+1)
            i = cam.find(os.sep, i+1)
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
            
            if not conteudo.cont_existe(cam_cont_selec, titulo_subcont) and titulo_subcont != '' and cam_img != '' and cam_video != '':
                self.contProgress.setValue(15)
                cam_cont_selec = QtCore.QString(cam_cont_selec).toUtf8()
                cam_cont = cam_cont_selec + titulo_subcont
                
                cam_cont = str(cam_cont).decode('utf8')
                
                os.mkdir(cam_cont)
                #os.mkdir(cam_cont+'\\conts\\')
                os.mkdir(cam_cont+ os.sep + 'conts' + os.sep)
                #os.mkdir(cam_cont+'\\img\\')
                os.mkdir(cam_cont+ os.sep + 'img' + os.sep)
                #os.mkdir(cam_cont+'\\video\\')
                os.mkdir(cam_cont+ os.sep + 'video' + os.sep)

                self.contProgress.setValue(40)

                #self.copia_arq(cam_video, cam_cont+'\\video\\')
                self.copia_arq(cam_video, cam_cont+ os.sep + 'video' + os.sep)
                self.contProgress.setValue(80)

                #self.copia_arq(cam_img, cam_cont+'\\img\\')
                self.copia_arq(cam_img, cam_cont+ os.sep + 'img' + os.sep)
                self.contProgress.setValue(100)
                
            elif titulo_subcont == '' or cam_img == '' or cam_video == '':
                self.errorLabel.show();
                self.errorLabel.setText('Título, imagem e vídeo são obrigatórios')

        except IOError:
            self.errorLabel.show()
            self.errorLabel.setText('Um dos arquivos não foi encontrado')

        #Doesn't matter. It's not needed anyway, since WindowsError is derived 
        #from OSError. So just use OSError in the except clause. 

#         except WindowsError:
#             self.errorLabel.show()
#             self.errorLabel.setText('O título deve ser diferente dos outros, e não deve conter \:/?*"|')
        
#         if not getattr(__builtins__, "WindowsError", None):
#             class WindowsError(OSError): pass
# 
#         try:
#             print "teste"
#         except WindowsError, e:
#                 self.errorLabel.show()
#                 self.errorLabel.setText('O título deve ser diferente dos outros, e não deve conter \:/?*"|')
                
        except Exception:
            self.errorLabel.show()
            self.errorLabel.setText('Erro Desconhecido')

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
        
