import os
import sys
import ajudaMenuInicial
from PyQt4 import QtGui, QtCore, uic

class TelaAjudaContainer(QtGui.QMainWindow):
    def __init__(self):
            super(TelaAjudaContainer, self).__init__()
            uic.loadUi(os.sep.join(["templates", "ajudaContainer.ui"]), self)
            #self.__ajuda = ajudaMenuInicial.TelaAjuda(self.widgetMainAjuda)
            w = QtGui.QWidget()
            w.resize(250, 150)
            w.move(300, 300)
            w.setWindowTitle('Simple')
            w.show()
            self.setMaximumHeight(self.height())
            self.setMaximumWidth(self.width())
            self.setMinimumHeight(self.height())
            self.setMinimumWidth(self.width())
            self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    window = TelaAjudaContainer()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())
