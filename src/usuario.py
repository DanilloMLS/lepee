# -*- coding: utf8 -*-
'''
    Autor: "Mario Costa"
    Email: "mariomenezescosta@gmail.com
    Data de Criação: 04/02/2016
    Data da Ultima Modificacao:
    Author da Ultima Modifcacao
    Versão Python: 2.7
'''

# importações necessarias

class Usuario:
    '''
        A classe Usuario modela os dados básicos que usuário deve possuir no sistema.
    '''
    #NOME, ESCOLA EM QUE  LECIONA, IDADE, FORMAÇÃO (GRADUACAO, LACTO OU STRICTO SENSU);
    #def __init__(self, nome, escola, idade, formacao):
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade

class Professor(Usuario):
    def __init__(self, nome = '', idade = 0, escola = '', formacao = ''):
        
        super(Usuario, self).__init__(escola, formacao)
    
        self.__escola = escola
        self.__formacao = formacao    
    
    def getEscola(self):
        return self.__escola
    
    def getFormacao(self):
        return self.__formacao
    
class Aluno(Usuario):
    def __init__(self, nome = '', idade = 0, serie = 0, id_professor):
        
        super(Usuario, self).__init__(nome, idade)
        
        self.__serie = serie
        self.__id_professor = id_professor
    
    def getSerie(self):
        return self.__serie
    
    def getIdProfessor(self):
        return self.__id_professor
    
    
    
