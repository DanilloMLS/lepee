# -*- coding: utf-8 -*-
'''
Created on 4 de fev de 2016
 
@author: mario
'''
 
 
import sqlite3
import sys
#import usuario
#from usuario import Usuario
 
class BaseDados:
 
    #Cria uma base comm os dados do professor
    def cria_base_professor(self, usuario):
         
        try:
            con = lite.connect('professores.db')
                 
            with con:
             
                cur = con.cursor()    
                cur.execute("CREATE TABLE cadastro(id INT, nome TEXT, idade INT, escola TEXT, formacao TEXT)")
                cur.execute("INSERT INTO cadastro VALUES" + "(" + usuario.professor.getNome(), usuario.professor.getIdade(),
                                            usuario.professor.getEscola(), usuario.professor.getFormacao() + ")")
                con.commit()
        except lite.Erro, e:
     
            if con:
                con.rollback()
         
            print "Error %s:" % e.args[0]
            sys.exit(1)
     
        finally:
     
            if con:
                con.close()  
              
    def remove_cadastro_professor(self, usuario):
        
    
    def cria_base_alunos(self, usuario):
        
         
