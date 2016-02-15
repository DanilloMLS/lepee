# -*- coding: cp1252 -*-

from PyQt4 import QtGui, QtCore, uic
import os

import base_dados
import tela_ensino

class TelaCadLogin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        
        #reload(sys)
        
        #sys.setdefaultencoding = "utf-8"
 
        
        #print str(a) # no exception
        
        super(TelaCadLogin, self).__init__()
        #uic.loadUi("templates\\intro.ui",self)
        uic.loadUi('templates' + os.sep + 'tela_cad_login.ui', self)
        
    
        #Lendo os dados do Cadastro professor
        self._nome = QtCore.QString(self.nomeLineEdit.text()).toUtf8()
        self._nome_usuario = QtCore.QString(self.usuarioLineEdit.text()).toUtf8()
        self._idade = QtCore.QString(self.idadeLineEdit.text()).toUtf8()
        self._escola = QtCore.QString(self.escolaLineEdit.text()).toUtf8()
        self._formacao = QtCore.QString(self.formacaoLineEdit.text()).toUtf8()        
        
        print self._nome
        print self._nome_usuario
        print self._idade
        print self._escola
        print self._formacao
         

    
            
        
        #mytext = self.textEdit.toPlainText()
        

#         self.__alunoButton = animated_button.AnimatedButton(self.alunoWidget,'icons' + os.sep +'voltar.gif')
#         self.__alunoButton.setGeometry(self.__alunoButton.x(),self.__alunoButton.y(), 251,200)
#         self.__alunoButton.show()
#         
#         self.__profButton = animated_button.AnimatedButton(self.profWidget,'icons' + os.sep + 'voltar.gif')
#         self.__profButton.setGeometry(self.__profButton.x(),self.__profButton.y(), 251,200)
#         self.__profButton.show()
# 
#         self.__introGif = animated_button.AnimatedButton(self.introGif,'icons' + os.sep + 'voltar.gif')
#         self.__introGif.setGeometry(self.__introGif.x(),self.__introGif.y(), 211,121)
#         self.__introGif.show()
        
        #TODO verificar a necessidade dessas chamadas
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())

#         self.__alunoButton.clicked.connect(self.abre_tela_nivelEvent)


    def abre_tela_nivelEvent(self, e):
        self.a = tela_ensino.TelaEnsino()
        self.a.show()

        self.close()


    def closeEvent(self, e):
        '''
            Destroi os objetos na janela principal quando esta for fechada
        '''
        self.deleteLater()
        
def testaFocus(self):
        widget = self.focusWidget()
        if isinstance(widget, QtGui.QLineEdit):
            widget.setText('')

        
root = QtGui.QApplication([])
app = TelaCadLogin()
app.show()
app.connect(root, QtCore.SIGNAL("focusChanged(QWidget *, QWidget *)"), testaFocus)
root.exec_()

# '''
# Created on 13 de fev de 2016
# 
# @author: mario
# '''
# from PyQt4 import QtGui, uic
# import os
# 
# class TelaCadLogin(QtGui.QMainWindow):
#     
#     def __init__(self):
#         print "ENTROUUUU"
#         super(TelaCadLogin, self).__init__()
#         print "ENTROUUUU"
#         #Template da janela
#         #uic.loadUi("templates\\tela_ensino.ui", self)
#         uic.loadUi(os.path.join('templates' + os.sep + 'tela_cad_login.ui'), self)
#     
#         
#         #testar se funciona
#         
#         self.login_button.clicked.connect(self.login_professor)
#         
#         
#         def login_professor(self):
# #             __nome =  QtGui.QInputDialog.getText(self, 'Input Dialog', 
# #             'Enter your name:')
#             #text = self.text.toPlainText()
#             __nome = self.cad_nome_textEdit.text.toPlainText()
#             
#             print __nome
#         
# #         'self.okButton.clicked.connect(self.accept)'
# #         
# # 
# #         #Cria as ares de menu e apresentacao de conteudo
# # #         self.__apres_ops = apres_ops.ApresOps(self.menuWidget)
# # #         self.__apres_cont= apres_cont.ApresCont(self.apresContWidget)
# # #         self.__conteudoIntr = conteudo.getCont_intr()
# # #         self.getApres_cont().apresent(self.__conteudoIntr)
# # #         
# #         #Carrega os conteudos no menu
# #         self.getApres_ops().carregar_conts(self.__conteudoIntr.getLista_conts())
# # 
# #         #Apresenta um novo conteudo selecionado
# #         self.connect(self.getApres_ops().getMenu(),
# #                      self.getApres_ops().getSignal(), self.muda_ap_cont)
# # 
# #         self.showMaximized()#Exibe em fullscreen
# # 
# #         #Desabilita o botao maximizar
# #         self.setMaximumHeight(self.height())
# #         self.setMaximumWidth(self.width())
# #         self.setMinimumHeight(self.height())
# #         self.setMinimumWidth(self.width())
# # 
# #     def __voltar(self):
# #         self.getApres_ops().carregar_conts(self.__conteudoIntr.getLista_conts())
# #         
# #     def muda_ap_cont(self):
# #         '''
# #             Apresenta o novo conteudo selecionado
# #         '''
# #         self.getApres_cont().apresent(self.getApres_ops().getCont_atual())
# # 
# #     def getApres_ops(self):
# #         '''
# #             getApres_ops() -> ApresOp
# #             retorna a area de menu atual
# #         '''
# #         return self.__apres_ops
# # 
# #     def getApres_cont(self):
# #         '''
# #             getApres_ops() -> ApresCont
# #             retorna a area de apresentacao atual
# #         '''
# #         return self.__apres_cont
# #     
# #     def resizeEvent(self, e):
# #         '''
# #             Redimensiona a tela inicial e seus objetos
# #         '''
# #         p = self.geometry()
# #         
# #         self.apresContWidget.setGeometry(190, 0,
# #                                          p.width() - 190, p.height())
# #         
# #         self.menuWidget.setGeometry(0, 0,
# #                                     self.menuWidget.width(),
# #                                     p.height() - 2 * self.__voltarBtn.height())
# # 
# #         self.__voltarBtn.setGeometry(15, self.menuWidget.height() + 10, 150, 80)
# # 
# #         self.sepAreasLine.setGeometry(self.sepAreasLine.x(),
# #                                       self.sepAreasLine.y(),
# #                                       self.sepAreasLine.width(), p.height())
# # 
# #         self.getApres_cont().resizeEvent(e)
# #         self.getApres_ops().resizeEvent(e)
# # 
# #     def closeEvent(self, e):
# #         '''
# #             Destroi os objetos na janela principal quando esta for fechada
# #         '''
# #         self.deleteLater()
