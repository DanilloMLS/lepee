# -*- coding: cp1252 -*-
'''
    Autor: "Fagner Barros"
    Vers�o: "1.0.1"
    Email: "fagnerluizbarros@gmail.com
    Data de Cria��o: 12/01/2015
    Data da �ltima modifica��o: 13/03/2015
    Vers�o Python: 2.7
'''

# importa��es necess�rias
import os

class Conteudo:
    '''
        A classe Conteudo representa a modelagem de um conte�do de informa��o para uma aula.
        Este possui video, imagem e outros conte�dos a qual este cont�m.
    '''
    def __init__(self, titulo, imagem, video, cam_cont='conteudos'):
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

    def getCam_cont(self):
        '''
            getCam_cont() -> str
            Retorna o caminho do conte�do
        '''
        return self.__cam_cont

    def getLista_conts(self):
        '''
            getLista_conts() -> list_of_conteudos
            Retorna a lista de conte�dos que o conteudo corrente cont�m.
        '''
        return getLista_conteudos(self.getCam_cont())

#fun��es do m�dulo
def getLista_conteudos(cam_cont):
    '''
        getList_conteudos(cam_cont) -> list_of_conteudos
        Retorna a lista de conte�dos que o conteudo corrente cont�m.
    '''
    try:
        titulos = os.listdir(cam_cont) #t�tulos dos conte�dos contidos no conte�do corrente
        conts = []
        for titulo in titulos:
            c_img = cam_cont+titulo+'\\img\\' + os.listdir(cam_cont+titulo+'\\img\\').pop() #caminho da img do conte�do
            c_video = cam_cont+titulo+'\\video\\' + os.listdir(cam_cont+titulo+'\\video\\').pop() #caminho relativo do v�deo
            c_cont = cam_cont + titulo + '\\conts\\' #diret�rio corrente deste conte�do
            conts.append(Conteudo(titulo, c_img, c_video, c_cont))
        return conts
    except IndexError as indexError:
        raise indexError
            
