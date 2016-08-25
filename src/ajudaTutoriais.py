import sys
import os
import ajudaMenuInicial
from player import Player
from PyQt4 import QtGui, Qt, uic

class TelaAjudaTutoriais(QtGui.QMainWindow):
    def __init__(self):
        super(TelaAjudaTutoriais, self).__init__()
        uic.loadUi(os.sep.join(["templates", "ajudaTutoriais.ui"]), self)
        self.__player1 = Player(self.tutorialWidget)
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())
        self.show()

        self.__player1.carregar("niveis\\nivel 1\\conts\\Cores\\video\\1- CORES ok.avi")
        self.tutorial1Bt.clicked.connect(self.mostrarTutorial1)
        self.tutorial2Bt.clicked.connect(self.mostrarTutorial2)
        self.tutorial3Bt.clicked.connect(self.mostrarTutorial3)
        
        self.voltarBt.clicked.connect(self.voltar)

    def mostrarTutorial1(self):
        self.__player1.carregar("ajuda\\tutorial1.avi")

    def mostrarTutorial2(self):
        self.__player1.carregar("ajuda\\tutorial2.avi") 

    def mostrarTutorial3(self):
        self.__player1.carregar("ajuda\\tutorial3.avi") 
    
    def voltar(self,e):
        self.a = ajudaMenuInicial.TelaAjuda()
        self.a.show()
        self.close()

    
def main():
    app = QtGui.QApplication(sys.argv)
    window = TelaAjudaTutoriais()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())
