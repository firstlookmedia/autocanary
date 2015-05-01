"""
AutoCanary | https://firstlook.org/code/autocanary
Copyright (c) 2015 First Look Media

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
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
