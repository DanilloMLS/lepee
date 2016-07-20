import sys
import os
import ajudaMenuInicial
from PyQt4 import QtGui, Qt, uic

class TelaAjudaSobre(QtGui.QMainWindow):
    def __init__(self):
        super(TelaAjudaSobre, self).__init__()
        uic.loadUi(os.sep.join(["templates", "ajudaSobre.ui"]), self)
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMinimumWidth(self.width())
        self.show()

        self.voltarBt.clicked.connect(self.voltar)

    def voltar(self,e):
        self.a = ajudaMenuInicial.TelaAjuda()
        self.a.show()
        self.close()

    
def main():
    app = QtGui.QApplication(sys.argv)
    window = TelaAjudaSobre()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())
