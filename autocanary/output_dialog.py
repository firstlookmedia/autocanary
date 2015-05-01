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
import platform, tempfile
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
import common

class OutputDialog(QtGui.QDialog):

    def __init__(self, app, signed_message):
        super(OutputDialog, self).__init__()
        self.app = app
        self.signed_message = signed_message
        self.setWindowTitle('Digitally Signed Canary Message')
        self.setWindowIcon(QtGui.QIcon(common.get_image_path('icon.png')))
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setModal(True)

        # signed message
        font = QtGui.QFont('Monospace')
        font.setStyleHint(QtGui.QFont.TypeWriter)
        signed_message_label = QtGui.QLabel(self.signed_message)
        signed_message_label.setWordWrap(True)
        signed_message_label.setFont(font)

        # buttons
        buttons_layout = QtGui.QHBoxLayout()
        save_to_file_button = QtGui.QPushButton('Save to File')
        save_to_file_button.clicked.connect(self.save_to_file_clicked)
        copy_to_clipboard_button = QtGui.QPushButton('Copy to Clipboard')
        copy_to_clipboard_button.clicked.connect(self.copy_to_clipboard_clicked)
        buttons_layout.addWidget(save_to_file_button)
        buttons_layout.addWidget(copy_to_clipboard_button)

        # layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(signed_message_label)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)
        self.show()

    def save_to_file_clicked(self):
        d = QtGui.QFileDialog(caption='Save to File')
        d.setAcceptMode(QtGui.QFileDialog.AcceptSave)
        d.setDefaultSuffix('asc')
        d.setNameFilter('*.asc')
        if d.exec_():
            filename = d.selectedFiles()[0]

            # save output to file
            try:
                open(filename, 'w').write(self.signed_message)
                common.alert('Digitally signed cannary message saved to:\n{0}'.format(filename))
                self.accept()
            except:
                common.alert('Failed saving file:\n{0}'.format(filename))

    def copy_to_clipboard_clicked(self):
        if platform.system() == 'Windows':
            # Qt's QClipboard isn't working in Windows
            import ctypes
            GMEM_DDESHARE = 0x2000
            ctypes.windll.user32.OpenClipboard(None)
            ctypes.windll.user32.EmptyClipboard()
            hcd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(self.signed_message))+1)
            pch_data = ctypes.windll.kernel32.GlobalLock(hcd)
            ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pch_data), bytes(self.signed_message))
            ctypes.windll.kernel32.GlobalUnlock(hcd)
            ctypes.windll.user32.SetClipboardData(1, hcd)
            ctypes.windll.user32.CloseClipboard()
        else:
            clipboard = self.app.clipboard()
            clipboard.setText(self.signed_message)

        common.alert('Digitally signed cannary message copied to clipboard')
        self.accept()
