"""
AutoCanary | https://firstlook.org/code/autocanary
Copyright © 2015 First Look Media

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
