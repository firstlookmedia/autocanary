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
from PyQt5 import QtWidgets, QtGui

def get_resource_path(filename):
    system = platform.system()

    if getattr(sys, 'autocanary_dev', False):
        # Look for resources directory relative to python file
        prefix = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), 'share')

    elif system == 'Linux' and sys.argv and sys.argv[0].startswith(sys.prefix):
        # AutoCanary is installed systemwide in Linux
        prefix = os.path.join(sys.prefix, 'share/autocanary')

    elif getattr(sys, 'frozen', False):
        # Check if app is "frozen"
        # https://pythonhosted.org/PyInstaller/#run-time-information
        if system == 'Darwin':
            prefix = os.path.join(sys._MEIPASS, 'share')
        elif system == 'Windows':
            prefix = os.path.join(os.path.dirname(sys.executable), 'share')

    return os.path.join(prefix, filename)

icon = None
def get_icon():
    global icon
    if not icon:
        icon = QtGui.QIcon(get_resource_path('icon.png'))
    return icon

def alert(msg, icon=QtWidgets.QMessageBox.Warning):
    d = QtWidgets.QMessageBox()
    d.setWindowTitle('AutoCanary')
    d.setWindowIcon(get_icon())
    d.setText(msg)
    d.setIcon(icon)
    d.exec_()
