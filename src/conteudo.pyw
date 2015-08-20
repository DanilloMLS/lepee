# -*- coding: cp1252 -*-
'''
    Autor: "Fagner Barros"
    Versão: "2.0.0"
    Email: "fagnerluizbarros@gmail.com
    Data de Criação: 12/01/2015
    Data da última modificação: 20/08/2015
    Versão Python: 2.7
'''

# importações necessárias
import os

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

#funções do módulo
def getCont_intr():
    return Conteudo("conteudos","conteudos\\img\\intro.jpg","conteudos\\video\\intro.avi","conteudos\\conts\\")

def getLista_conts(cam_cont="conteudos\\"):
    '''
        getList_conteudos(cam_cont) -> list_of_conteudos
        Retorna os subconteudos que o caminho do contéudo referenciado contém.
    '''
    try:
        titulos = os.listdir(cam_cont) #títulos dos conteúdos contidos no conteúdo corrente
        conts = []
        for titulo in titulos:
            c_img = cam_cont+titulo+'\\img\\' + os.listdir(cam_cont+titulo+'\\img\\').pop() #caminho da img do conteúdo
            c_video = cam_cont+titulo+'\\video\\' + os.listdir(cam_cont+titulo+'\\video\\').pop() #caminho relativo do vídeo
            c_cont = cam_cont + titulo + '\\conts\\' #diretório corrente deste conteúdo
            conts.append(Conteudo(titulo, c_img, c_video, c_cont))
        return conts

    except IndexError as indexError:
        raise indexError

def getCam_conteudo(titulo):
    if not titulo:
        return 'conteudos\\'
    else:
        for cont in getLista_conts():
            if cont.getTitulo() == titulo:
                return cont.getCam_list_conts()
        raise ValueError('Conteudo inexistente!!!')

def cont_existe(cam_cont, titulo):
        if not cam_cont:
            return titulo in os.listdir('conteudos\\')
        return titulo in os.listdir(cam_cont)

def getTitulos(cont=None):
    if cont is None:
        return os.listdir('conteudos\\')
    else:
        return os.listdir(cont.getCam_list_conts())
    
