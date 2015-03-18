# -*- coding: cp1252 -*-
'''
    Autor: "Fagner Barros"
    Versão: "1.0.1"
    Email: "fagnerluizbarros@gmail.com
    Data de Criação: 12/01/2015
    Data da última modificação: 13/03/2015
    Versão Python: 2.7
'''

# importações necessárias
import os

class Conteudo:
    '''
        A classe Conteudo representa a modelagem de um conteúdo de informação para uma aula.
        Este possui video, imagem e outros conteúdos a qual este contém.
    '''
    def __init__(self, titulo, imagem, video, cam_cont='conteudos'):
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

    def getCam_cont(self):
        '''
            getCam_cont() -> str
            Retorna o caminho do conteúdo
        '''
        return self.__cam_cont

    def getLista_conts(self):
        '''
            getLista_conts() -> list_of_conteudos
            Retorna a lista de conteúdos que o conteudo corrente contém.
        '''
        return getLista_conteudos(self.getCam_cont())

#funções do módulo
def getLista_conteudos(cam_cont):
    '''
        getList_conteudos(cam_cont) -> list_of_conteudos
        Retorna a lista de conteúdos que o conteudo corrente contém.
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
            
