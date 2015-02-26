import os, sys, inspect, platform
from PyQt4 import QtCore, QtGui

def get_image_path(filename):
    if platform.system() == 'Linux':
        prefix = os.path.join(sys.prefix, 'share/autocanary')
    elif platform.system() == 'Windows':
        prefix = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    else:
        prefix = os.path.dirname(__file__)
    
    image_path = os.path.join(prefix, filename)
    return image_path

def alert(msg, icon=QtGui.QMessageBox.Warning):
    d = QtGui.QMessageBox()
    d.setWindowTitle('AutoCanary')
    d.setWindowIcon(QtGui.QIcon(get_image_path('icon.png')))
    d.setText(msg)
    d.setIcon(icon)
    d.exec_()

