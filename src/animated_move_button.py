import os
from PyQt4 import uic, QtCore, QtGui
from animated import animated_widget

class AnimatedMoveButton(QtGui.QPushButton):
    def __init__(self, parent=None, gifPath="icons//voltar.gif", name=''):
        super(AnimatedMoveButton, self).__init__()
        self.setParent(parent)

        cursor = QtGui.QCursor(QtGui.QPixmap('icons\\pointingHand.png'))

        self.setCursor(cursor)
        
        self.gifPath = ""
        self.movie = QtGui.QMovie() #m gifPath
        self.setMouseTracking(True)
        self.setGif(gifPath)

    def nextImage(self):

        pix = QtGui.QPixmap(self.movie.currentPixmap())
        pix = pix.scaled(self.width(), self.height())

        self.setIcon(QtGui.QIcon(pix))
        self.setIconSize(QtCore.QSize(pix.rect().width() * 0.9,
                           pix.rect().height() * 0.9))

    def setGif(self, gifPath):
        self.gifPath = gifPath
        self.movie.setFileName(self.gifPath)
        self.movie.stop()

        pix = QtGui.QPixmap(self.gifPath) #m "icons//voltar.gif"
        pix = pix.scaled(self.width(), self.height())

        self.setIcon(QtGui.QIcon(pix))
       
        self.connect(self.movie, QtCore.SIGNAL("frameChanged(int)"), self.nextImage)
        self.connect(self.movie, QtCore.SIGNAL("finished()"), self.movie.stop)

        
    def setGeometry(self, x, y, width, height):
        super(AnimatedMoveButton, self).setGeometry(x, y, width, height)
        print "Entrou set"
        pix = QtGui.QPixmap(self.gifPath) #m "icons//voltar.gif"
        pix = pix.scaled(self.width(), self.height())

        self.setIcon(QtGui.QIcon(pix))
        self.setIconSize(QtCore.QSize(pix.rect().width() * 0.9,
                           pix.rect().height() * 0.9))


    def leaveEvent(self, event):
        self.movie.stop()

    def enterEvent(self, event):
        self.movie.start()
        

if __name__ == "__main__":    
    root = QtGui.QApplication([])
    a = AnimatedMoveButton()
    a.show()
    root.exec_()
