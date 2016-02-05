# -*- coding: cp1252 -*-
'''
    Autor: "Mario Costa"
    Email: "mariomenezescosta@gmail.com
    Data de Criação: 04/02/2016
    Versão Python: 2.7
'''

# importações necessárias

class Usuario:
    '''
        A classe Conteudo representa a modelagem de um conteúdo de informação para uma aula.
        Este possui video, imagem e subconteúdos.
    '''
    #NOME, ESCOLA EM QUE  LECIONA, IDADE, FORMAÇÃO (GRADUAÇÃO, LACTO OU STRICTO SENSU);
    #def __init__(self, nome, escola, idade, formacao):
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade

class professor(Usuario):
    def __init__(self, nome = '', idade = 0, escola = '', formacao = ''):
        
        Usuario.__init__(self, escola, formacao)
    
        self.__escola = escola
        self.__formacao = formacao    
    
    def getEscola(self):
        return self.__escola
    
    def getFormacao(self):
        return self.__formacao
    
class aluno(Usuario):
    def __init__(self, nome = '', idade = 0, serie = 0):
        
        Usuario.__init__(self, nome, idade)
        
        self.__serie = serie
    
    def getSerie(self):
        return self.__serie
    
    
    