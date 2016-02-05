from PyQt4 import QtGui, QtCore

def animated_widget(widget, pathGifAnim=None):
    
    atrib = dir(widget)

    if 'setIcon' in atrib or 'setPixmap' in atrib:
        movie = QtGui.QMovie(pathGifAnim)
        movie.start()
        
        def nextImage(self):

            pix = QtGui.QPixmap(movie.currentPixmap())
            pix = pix.scaled(widget.width(), widget.height())

            if 'setIcon' in atrib:
                widget.setIcon(QtGui.QIcon(pix))
                widget.setIconSize(QtCore.QSize(pix.rect().width() * 0.9,
                                   pix.rect().height() * 0.9))

            elif 'setPixmap' in atrib:
                widget.setPixmap(pix)
            
        def delete():
            movie.deleteLater()
            

        widget.connect(widget, QtCore.SIGNAL("destroyed()"), delete)
        widget.connect(movie, QtCore.SIGNAL("frameChanged(int)"), nextImage)
        widget.connect(movie, QtCore.SIGNAL("finished()"), movie.start)

    else:
        raise ValueError("Widget nao pode ser aniamdo com um gif")
    
        
        
