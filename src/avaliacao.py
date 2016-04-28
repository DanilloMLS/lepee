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

#import plataform

import os
from pergunta import Pergunta
import random

class Avaliacao(object):

    def __init__(self, nivel):
        #self.__lista_perguntas = []
        self.__num_acertos = 0
        self.__nivel = nivel

    def getNumAcertos(self):
        return self.__num_acertos

    def getNivel(self):
        return self.__nivel

    #def getListaPerguntas(self):
    #    return self.__lista_perguntas

    def acertou(self):
        self.__num_acertos = self.__num_acertos + 1

def gerarQuestionario(nivel):
    pastas = os.listdir("avaliacoes/"+nivel)
    questoes = []
    q = []
    
    for pasta in pastas:
        a = [1,2,3,4]
        random.shuffle(a)
        p = Pergunta("avaliacoes/"+nivel+"/"+pasta+"/vidperg",
                     "avaliacoes/"+nivel+"/"+pasta+"/alter"+str(a[0]),
                     "avaliacoes/"+nivel+"/"+pasta+"/alter"+str(a[1]),
                     "avaliacoes/"+nivel+"/"+pasta+"/alter"+str(a[2]),
                     "avaliacoes/"+nivel+"/"+pasta+"/alter"+str(a[3]),
                     "avaliacoes/"+nivel+"/"+pasta+"/alter3",
                     nivel)
        questoes.append(p)

    random.shuffle(questoes)
    while(len(questoes) > 5):
        questoes.pop()

    return questoes

'''
a = Avaliacao("nivel1")
q = []
q = gerarQuestionario("nivel1")

for i in q:
    print i.getAlter1()
'''

'''
n = "nivel1"
pastas = os.listdir("avaliacoes/"+n)
questoes = []
for pasta in pastas:
    questoes.append(pasta)

random.shuffle(questoes)
while(len(questoes) > 5):
    questoes.pop()
for questao in questoes:
    print questao 
'''
