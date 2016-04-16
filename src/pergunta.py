# -*- coding: cp1252 -*-
'''
    Autor: "Danillo Moraes"
    Versão: "2.0.0"
    Email: "moraesdanillo10@gmail.com
    Data de Criação: 14/04/2016
    Data da última modificação: 14/04/2016
    Autor da úlitma mod: Danillo Moraes
    Versão Python: 2.7
'''

#import os
#import plataform

class Pergunta(object):

    def __init__(self, perg, alter1, alter2, alter3, alter4, alter5, resp, nivel):
        self.__cam_perg = perg
        self.__cam_alter1 = alter1
        self.__cam_alter2 = alter2
        self.__cam_alter3 = alter3
        self.__cam_alter4 = alter4
        self.__cam_alter5 = alter5
        self.__cam_resp = resp
        self.__nivel = nivel

    def getPerg(self):
        return self.__cam_perg

    def getAlter1(self):
        return self.__cam_alter1

    def getAlter2(self):
        return self.__cam_alter2
    
    def getAlter3(self):
        return self.__cam_alter3
    
    def getAlter4(self):
        return self.__cam_alter4

    def getAlter5(self):
        return self.__cam_alter5

    def getResp(self):
        return self.__cam_resp

    def getNivel(self):
        return self.__nivel
