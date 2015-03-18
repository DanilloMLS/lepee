# -*- coding: cp1252 -*-

from PyQt4 import QtGui, uic
import os
import conteudo
import categorias
import criartexto

class CriarConteudo(QtGui.QDialog):
    def __init__(self, toplevel=None):
        super(CriarConteudo, self).__init__(toplevel)
        uic.loadUi('templates\\CriarCont.ui', self)
        self.criarBtn.clicked.connect(self.criarCont)
        self.cancelarBtn.clicked.connect(self.close)
        self.criarTextoBtn.clicked.connect(self.criarTexto)
        self.procurarImgBtn.clicked.connect(self.carregarImg)
        self.procurarVideoBtn.clicked.connect(self.carregarVideo)
        self.carregarCats()

        self.contProgress.hide()
        self.criandoLabel.hide()

        self.c_texto = criartexto.CriarTexto(self)
        
    def carregarCats(self):
        cats = categorias.Categorias()
        self.escolheCatComboBox.addItems(cats.getTitulosCats())

    def carregar(self, titulo, diretorio, filtro):
        return QtGui.QFileDialog.getOpenFileName(self, titulo, diretorio, filtro)

    def carregarVideo(self):
        cam = self.carregar('Selecione um vídeo:', 'C:\\Users\\Fagner\\Videos', 'Videos(*.mp4 *.avi *.mpeg *.flv)')
        self.videoLineEdit.setText(cam)

    def pegaExtensao(self, cam):
        e = cam.split('.')
        if len(e) > 1:
            return '.' + e[1]
        else:
            return ''
        
    def carregarImg(self):
        cam = self.carregar('Selecione uma imagem:', 'C:\\Users\\Fagner\\Pictures', 'Images(*.png *.gif *.jpg)')
        self.imgLineEdit.setText(cam)

    def salvaArquivo(self, cam_velho, cam_novo):
        try:
            if cam_velho != '' and cam_novo != '':
                with open(cam_velho, 'rb') as arq:
                    dados = arq.read()
                    with open(cam_novo, 'wb') as arq:
                        arq.write(dados)
            
        except IOError as io:
            raise io
    
    def criarTexto(self):
        self.c_texto.show()

    def geraNomeArq(self, cam, tipo, ext):
        l = os.listdir(cam)
        l.sort()
        
        for i in range(len(l)):
            aux = l[i].split('.')
            nome = aux[0]

            if nome != (tipo + ' ' + str(i+1)):
                return cam + '\\' + tipo + ' ' + str(i+1) + ext
        return cam + '\\' + tipo + ' ' + str(len(l) + 1) + ext

    def criarCont(self):
        try:
            #Exibe o progresso da criação do conteúdo
            self.contProgress.show()
            self.criandoLabel.show()
            
            #Obtém os dados dos campos de entrada
            velho_cam_img = self.imgLineEdit.text()
            velho_cam_v = self.videoLineEdit.text()
            titulo = str(self.tituloLineEdit.text())
            titulo = titulo.strip() #Remove espaços em branco a direita e a esquerda

            cats = categorias.Categorias()
            c = cats.getCategoria(self.escolheCatComboBox.currentText()) #Pega a categoria selecionada
            
            self.contProgress.setValue(20)#

            if velho_cam_img != '':
                ext_img = self.pegaExtensao(velho_cam_img)
                novo_cam_img = self.geraNomeArq('imagens', 'imagem', ext_img)
            else:
                novo_cam_img = ''

            if velho_cam_v != '':
                ext_v = self.pegaExtensao(velho_cam_v)
                novo_cam_v = self.geraNomeArq('videos', 'video', ext_v)
            else:
                novo_cam_v = ''
            
            #Cria o conteúdo e o salva na categoria específica
            cont = conteudo.Conteudo(titulo, novo_cam_img, novo_cam_v, self.c_texto.getTexto())
            adicionou = c.addCont(cont)
            self.contProgress.setValue(40)#

            if adicionou:
                self.salvaArquivo(velho_cam_img, novo_cam_img)
                self.contProgress.setValue(60)#

                self.salvaArquivo(velho_cam_v, novo_cam_v)
                cats.salvarCat(c)
                self.contProgress.setValue(90)#

            self.contProgress.setValue(100)#

        except IOError as io:
            print io

        except ValueError as ve:
            print ve

        finally:
            self.contProgress.setValue(0)
            self.contProgress.hide()
            self.criandoLabel.hide()
            

    def closeEvent(self, e):
        if self.parent() != None:
            self.parent().show()
        self.deleteLater()
        

'''root = QtGui.QApplication([])
app = CriarConteudo()
app.show()
root.exec_()'''
        
