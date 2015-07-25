from PyQt4 import QtGui, QtCore
class AnimatedButton(QtGui.QPushButton):
    def __init__(self, toplevel=None, camImgAnim=None):
        super(AnimatedButton, self).__init__()
        self.setParent(toplevel)
        self.__movie = QtGui.QMovie(camImgAnim)
        self.setIconSize(QtCore.QSize(10, 10))
        self.connect(self.__movie, QtCore.SIGNAL("frameChanged(int)"), self.__setButtonIcon)
        self.connect(self.__movie, QtCore.SIGNAL("finished()"), self.__movie.start)
        self.__movie.start()

    def __setButtonIcon(self):
        self.setIcon(QtGui.QIcon(self.__movie.currentPixmap()))
        
    
    def setGeometry(self, x, y, width, height):
        super(AnimatedButton, self).setGeometry(x, y, width, height)
        self.setIconSize(QtCore.QSize(width, height))
    

    def setHeight(self, height_value):
        super(AnimatedButton, self).setHeight(height_value)
        self.setIconSize(QtCore.QSize(self.width(), height_value))
    
    def setWidth(self, width_value):
        super(AnimatedButton, self).setWidth(width_value)
        self.setIconSize(QtCore.QSize(width_value, self.height()))
