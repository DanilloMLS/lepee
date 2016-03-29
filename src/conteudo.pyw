# -*- coding: cp1252 -*-
'''
    Autor: "Fagner Barros"
    Vers�o: "2.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Cria��o: 29/01/2015
    Data da �ltima modifica��o: 07/12/2015
    Autor da �litma mod: Fagner Luiz
    Vers�o Python: 2.7
'''

# importa��es necess�rias
import os
import platform

class Conteudo(object):
    '''
        A classe Conteudo representa a modelagem de um conte�do de informa��o para uma aula.
        Este possui video, imagem e subconte�dos.
    '''
    def __init__(self, titulo, imagem, video, cam_cont):
        self.__titulo = titulo
        self.__cam_img = imagem
        self.__cam_video = video
        self.__cam_cont = cam_cont

    def getTitulo(self):
        '''
            getTitulo() -> str
            Retorna o t�tulo do conte�do
        '''
        return self.__titulo

    def getCam_img(self):
        '''
            getCam_img() -> str
            Retorna o caminho da imagem do conte�do
        '''
        return self.__cam_img

    def getCam_video(self):
        '''
            getCam_video() -> str
            Retorna o caminho do video do conte�do
        '''
        return self.__cam_video

    def getCam_list_conts(self):
        '''
            getCam_cont() -> str
            Retorna o caminho do conte�do
        '''
        return self.__cam_cont

    def getLista_conts(self):
        '''
            getLista_conts() -> lista_de_conteudos
            Retorna os subconte�dos que o conteudo corrente cont�m.
        '''
        return getLista_conts(self.getCam_list_conts())

    def hasSubConts(self):
        return os.path.exists(self.getCam_list_conts())

#fun��es do m�dulo

def getLista_conts(cam_cont):
    '''
        getList_conteudos(cam_cont) -> list_of_conteudos
        Retorna os subconteudos que o caminho do cont�udo referenciado cont�m.
    '''

    if os.path.exists(cam_cont):
        print "Conteudo existe"
        print cam_cont
        sep = os.sep
        titulos = os.listdir(cam_cont) #t�tulos dos conte�dos contidos no conte�do corrente
        conts = []
        dir_img = sep + 'img' + sep
        dir_video = sep + 'video' + sep
        dir_conts = sep + 'conts' + sep
        
        for titulo in titulos:
            c_img = c_video = ''
            
            if (os.path.exists(cam_cont + titulo + dir_img)):
                c_img = (cam_cont + titulo + dir_img +
                         os.listdir(cam_cont + titulo + dir_img).pop()) #caminho da img do conte�do

            if (os.path.exists(cam_cont+titulo + dir_video)):
                c_video = (cam_cont+titulo + dir_video +
                           os.listdir(cam_cont+titulo + dir_video).pop()) #caminho relativo do v�deo

            #diret�rio onde ser�o guardados os subconte�dos do conte�do
            
            c_cont = cam_cont + titulo + dir_conts
            conts.append(Conteudo(titulo, c_img, c_video, c_cont))
            
    else:
        raise ValueError("Diretorio n�o encontrado")

    return conts

