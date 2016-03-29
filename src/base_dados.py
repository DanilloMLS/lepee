# -*- coding: utf-8 -*-
'''
Created on 4 de fev de 2016
 
@author: mario
'''
#Tive que instalar o python-qt4-sql
#no ubuntu 14.04: sudo apt-get install python-qt4-sql


from PyQt4 import QtSql, QtGui
 
class BaseDados:
 
 
    def erro_carregar_banco(self):
        
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Nao foi possivel abrir o banco"),
                                       QtGui.qApp.tr("Nao foi possivel estabeleces conoexao com o banco de dados.\n"),
                                       QtGui.QMessageBox.Cancel)
    
    def adiciona_analise_quantitativa(self, resposta1, resposta2, resposta3, resposta4, resposta5):
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        db.open('tabela_quanti.db')
        
        if db:
            status = True
    
        else:
            status = False
            self.erro_carregar_banco()
        
        query = QtSql.QSqlQuery(db)
        
        query.exec_("INSERT INTO professores VALUES" + "(" + resposta1, resposta2, resposta3, 
                    resposta4, resposta5 + ")")
        
        db.close()
            
        return status
        
    def adiciona_analise_qualitativa(self, resposta1, resposta2, resposta3, resposta4, resposta5):
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        db.open('tabela_quali.db')
        
        if db:
            status = True
    
        else:
            status = False
            self.erro_carregar_banco()
        
        query = QtSql.QSqlQuery(db)
        
        query.exec_("INSERT INTO professores VALUES" + "(" + resposta1, resposta2, resposta3, 
                    resposta4, resposta5 + ")")
        
        db.close()
            
        return status
    
    def adiciona_professor(self, nome, idade, nome_escola, formacao):
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        db.open('tabela_professores.db')
        
        if db:
            status = True
    
        else:
            status = False
            self.erro_carregar_banco()
            
        query = QtSql.QSqlQuery(db)
        
        
        query.exec_("INSERT INTO professores VALUES" + "(" + "NULL", nome, idade, nome_escola, 
                    formacao + ")")
        
        db.close()
        
        return status
        
    def adiciona_aluno(self, nome, idade, serie, id_professor):
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        db.open('tabela_alunos.db')
        
        if db:
            status = True
    
        else:
            status = False
            self.erro_carregar_banco()
            
        query = QtSql.QSqlQuery(db)
        
        query.exec_("INSERT INTO alunos VALUES" + "(" + "NULL", nome, idade, serie, id_professor +")")
        
        db.close()
        
        return status
        
    def consulta_professor_nome(self, nome_professor):
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        db.open('tabela_professores.db')
        
        if db:
            status = True
    
        else:
            status = False
            self.erro_carregar_banco()
        
        query = QtSql.QsqlQuery(db)
    
        sqlqry = "SELECT * FROM professores WHERE nome = " + nome_professor 
        
        if query.exec_(sqlqry):
            while query.next():
                nome = query.value(0).toString()
                print nome
        
        db.close()
        
        return status
        
    def consulta_professor_login(self, login_professor):
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        
        db.open('tabela_professores.db')
        
        if db:
            
            status = True
        else:
            self.erro_carregar_banco()
            status = False

            
        query = QtSql.QsqlQuery(db)
    
        sqlqry = "SELECT * FROM professores WHERE login = " + login_professor 
        
        if query.exec_(sqlqry):
            while query.next():
                login = query.value(0).toString()
                print login
                
        db.close()
        
        return status
        
    def consulta_aluno_nome(self, nome_aluno):
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        
        db.open('tabela_alunos.db')
        
        if db:
            
            status = True
    
        else:
            self.erro_carregar_banco()
            status = False
        
        query = QtSql.QsqlQuery(db)
    
        sqlqry = "SELECT * FROM alunos WHERE nome_luno = " + nome_aluno 
        
        if query.exec_(sqlqry):
            while query.next():
                nome = query.value(0).toString()
                print nome
                
        db.close()
        
        return status
        
    def consulta_conteudo_nome(self, nome_categoria):
        
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        db.open('tabela_conteudo.db')
        
        if db:
            
            status = True
    
        else:
            self.erro_carregar_banco()
            status = False
            
        query = QtSql.QsqlQuery(db)
    
        sqlqry = "SELECT * FROM conteudo WHERE nome_categoria = " + nome_categoria
        
        if query.exec_(sqlqry):
            while query.next():
                login = query.value(0).toString()
                print login
        
                
        db.close()
        
        return status