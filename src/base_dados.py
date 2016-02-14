# -*- coding: utf-8 -*-
'''
Created on 4 de fev de 2016
 
@author: mario
'''
#Tive que instalar o python-qt4-sql
#no ubuntu 14.04: sudo apt-get install python-qt4-sql
 
from PyQt4 import QtSql, QtGui
import usuario
 
class BaseDados:
 
 
    def carrega_db_professor(self):
        
        db_professor = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        #db_professor.setDatabaseName('sports.db')
        db_professor.open('professor.db')
    
        if not db_professor.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                       QtGui.qApp.tr("Unable to establish a database connection.\n" 
                                                     "This example needs SQLite support. Please read " 
                                                     "the Qt SQL driver documentation for information " 
                                                     "how to build it.\n\n" "Click Cancel to exit."),
                                       QtGui.QMessageBox.Cancel)
            
            return False
        
        
        
        return True
    #Cria uma base comm os dados do professor
#     def cria_base_professor(self, usuario):
#          
#         try:
#             con = lite.connect('professores.db')
#                  
#             with con:
#              
#                 cur = con.cursor()    
#                 cur.execute("CREATE TABLE cadastro(id INT, nome TEXT, idade INT, escola TEXT, formacao TEXT)")
#                 cur.execute("INSERT INTO cadastro VALUES" + "(" + usuario.professor.getNome(), usuario.professor.getIdade(),
#                                             usuario.professor.getEscola(), usuario.professor.getFormacao() + ")")
#                 con.commit()
#         except lite.Erro, e:
#      
#             if con:
#                 con.rollback()
#          
#             print "Error %s:" % e.args[0]
#             sys.exit(1)
#      
#         finally:
#      
#             if con:
#                 con.close()  
#               
    #def remove_cadastro_professor(self, usuario):
        
    
    #def cria_base_alunos(self, usuario):
    def cadastra_professor(self):
        
        query = QtSql.QSqlQuery()
    
        #Se precisarmos criar uma base:
        #query.exec_("create table sportsmen(id int primary key, " "firstname varchar(20), lastname varchar(20))")
        
        ##query.exec_("insert into professores values(101, 'Roger', 'Federer')")
        query.exec_("INSERT INTO cadastro VALUES" + "(" + "NULL", usuario.professor.getNome(), 
                    usuario.professor.getIdade(), usuario.professor.getEscola(), 
                    usuario.professor.getFormacao() + ")")
        
         
