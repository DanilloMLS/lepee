# -*- coding: cp1252 -*-
'''
    Autor: "Fagner Barros"
    Versão: "2.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Criação: 29/01/2015
    Data da última modificação: 07/12/2015
    Autor da úlitma mod: Fagner Luiz
    Versão Python: 2.7
'''

# importações necessárias
import os
import platform

class Conteudo(object):
    '''
        A classe Conteudo representa a modelagem de um conteúdo de informação para uma aula.
        Este possui video, imagem e subconteúdos.
    '''
    def __init__(self, titulo, imagem, video, cam_cont):
        self.__titulo = titulo
        self.__cam_img = imagem
        self.__cam_video = video
        self.__cam_cont = cam_cont

    def getTitulo(self):
        '''
            getTitulo() -> str
            Retorna o título do conteúdo
        '''
        return self.__titulo

    def getCam_img(self):
        '''
            getCam_img() -> str
            Retorna o caminho da imagem do conteúdo
        '''
        return self.__cam_img

    def getCam_video(self):
        '''
            getCam_video() -> str
            Retorna o caminho do video do conteúdo
        '''
        return self.__cam_video

    def getCam_list_conts(self):
        '''
            getCam_cont() -> str
            Retorna o caminho do conteúdo
        '''
        return self.__cam_cont

    def getLista_conts(self):
        '''
            getLista_conts() -> lista_de_conteudos
            Retorna os subconteúdos que o conteudo corrente contém.
        '''
        return getLista_conts(self.getCam_list_conts())

    def hasSubConts(self):
        return os.path.exists(self.getCam_list_conts())

#funções do módulo

def getLista_conts(cam_cont):
    '''
        getList_conteudos(cam_cont) -> list_of_conteudos
        Retorna os subconteudos que o caminho do contéudo referenciado contém.
    '''

    if os.path.exists(cam_cont):
        print "Conteudo existe"
        print cam_cont
        sep = os.sep
        titulos = os.listdir(cam_cont) #títulos dos conteúdos contidos no conteúdo corrente
        conts = []
        dir_img = sep + 'img' + sep
        dir_video = sep + 'video' + sep
        dir_conts = sep + 'conts' + sep
        
        for titulo in titulos:
            c_img = c_video = ''
            
            if (os.path.exists(cam_cont + titulo + dir_img)):
                c_img = (cam_cont + titulo + dir_img +
                         os.listdir(cam_cont + titulo + dir_img).pop()) #caminho da img do conteúdo

            if (os.path.exists(cam_cont+titulo + dir_video)):
                c_video = (cam_cont+titulo + dir_video +
                           os.listdir(cam_cont+titulo + dir_video).pop()) #caminho relativo do vídeo

            #diretório onde serão guardados os subconteúdos do conteúdo
            
            c_cont = cam_cont + titulo + dir_conts
            conts.append(Conteudo(titulo, c_img, c_video, c_cont))
            
    else:
        raise ValueError("Diretorio não encontrado")

    return conts

