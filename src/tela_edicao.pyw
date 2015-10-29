

from PyQt4 import QtGui, QtCore, uic

class TelaEdicao(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(TelaEdicao, self).__init__()

        #Template da janela
        uic.loadUi("tela_edicao.ui", self)

    def closeEvent(self, e):
        '''
            Destrói os objetos na janela principal quando está for fechada
        '''
        self.deleteLater()

        
#criar tela
root = QtGui.QApplication([])
app = TelaEdicao()
app.show()
root.exec_()
