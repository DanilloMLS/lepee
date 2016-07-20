import sys
import os
import ajudaNiveis
import ajudaTelaEnsino
import ajudaQualitativa
import ajudaQuantitativa
import ajudaTutoriais
import ajudaSobre
from PyQt4 import QtGui, QtCore, uic

class TelaAjuda(QtGui.QMainWindow):
    def __init__(self):
        super(TelaAjuda, self).__init__()
        uic.loadUi(os.sep.join(["templates", "ajudaMenuInicial.ui"]), self)
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())
        self.show()

        self.niveisBt.clicked.connect(self.abre_ajuda_niveis)
        self.ensinoBt.clicked.connect(self.abre_ajuda_telaEnsino)
        self.qualitBt.clicked.connect(self.abre_ajuda_qualitativa)
        self.quantBt.clicked.connect(self.abre_ajuda_quantitativa)
        self.tutorialBt.clicked.connect(self.abre_ajuda_tutoriais)
        self.sobreBt.clicked.connect(self.abre_ajuda_sobre)

    def abre_ajuda_niveis(self,e):
        self.a = ajudaNiveis.TelaAjudaNiveis()
        self.a.show()
        self.close()
    def abre_ajuda_telaEnsino(self,e):
        self.a = ajudaTelaEnsino.TelaAjudaEnsino()
        self.a.show()
        self.close()
    def abre_ajuda_qualitativa(self,e):
        self.a = ajudaQualitativa.TelaAjudaQualitativa()
        self.a.show()
        self.close()
    def abre_ajuda_quantitativa(self,e):
        self.a = ajudaQuantitativa.TelaAjudaQuantitativa()
        self.a.show()
        self.close()
    def abre_ajuda_tutoriais(self,e):
        self.a = ajudaTutoriais.TelaAjudaTutoriais()
        self.a.show()
        self.close()
    def abre_ajuda_sobre(self,e):
        self.a = ajudaSobre.TelaAjudaSobre()
        self.a.show()
        self.close()

def main():
    app = QtGui.QApplication(sys.argv)
    window = TelaAjuda()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())


