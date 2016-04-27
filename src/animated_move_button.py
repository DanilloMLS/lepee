import os
from PyQt4 import uic, QtCore, QtGui
from animated import animated_widget

class AnimatedMoveButton(QtGui.QPushButton):
    def __init__(self, parent=None, name='', gifPath="icons//voltar.gif"):
        super(AnimatedMoveButton, self).__init__()
        self.setParent(parent)

        self.movie = QtGui.QMovie(gifPath)
        self.movie.stop()

        pix = QtGui.QPixmap("icons//voltar.gif")
        pix = pix.scaled(self.width(), self.height())

        self.setIcon(QtGui.QIcon(pix))
       
        self.setMouseTracking(True)
        self.moveu = False

        self.connect(self.movie, QtCore.SIGNAL("frameChanged(int)"), self.nextImage)
        self.connect(self.movie, QtCore.SIGNAL("finished()"), self.movie.stop)

    def nextImage(self):

        pix = QtGui.QPixmap(self.movie.currentPixmap())
        pix = pix.scaled(self.width(), self.height())

        self.setIcon(QtGui.QIcon(pix))
        self.setIconSize(QtCore.QSize(pix.rect().width() * 0.9,
                           pix.rect().height() * 0.9))

                

    def mouseMoveEvent (self, e):
        if self.movie.state() == QtGui.QMovie.NotRunning: 
            self.movie.start()
            self.moveu = True
        if self.movie.state() == QtGui.QMovie.Running and ((e.x() + 5 >= self.width() or e.y() + 5 >= self.height())or(e.x() <= 5 or e.y() <= 5)):
            self.movie.stop()
            self.moveu = False

    def setGeometry(self, x, y, width, height):
        super(AnimatedMoveButton, self).setGeometry(x, y, width, height)
        print "Entrou set"
        pix = QtGui.QPixmap("icons//voltar.gif")
        pix = pix.scaled(self.width(), self.height())

        self.setIcon(QtGui.QIcon(pix))
        self.setIconSize(QtCore.QSize(pix.rect().width() * 0.9,
                           pix.rect().height() * 0.9))

if __name__ == "__main__":    
    root = QtGui.QApplication([])
    a = AnimatedMoveButton()
    a.show()
    root.exec_()
