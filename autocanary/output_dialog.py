from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
import common

class OutputDialog(QtGui.QDialog):

    def __init__(self, signed_message):
        super(OutputDialog, self).__init__()
        self.setWindowTitle('AutoCanary')
        self.setWindowIcon(QtGui.QIcon(common.get_image_path('icon.png')))
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setModal(True)

        # signed message
        font = QtGui.QFont('Monospace')
        font.setStyleHint(QtGui.QFont.TypeWriter)
        signed_message_label = QtGui.QLabel(signed_message)
        signed_message_label.setWordWrap(True)
        signed_message_label.setFont(font)

        # buttons
        buttons_layout = QtGui.QHBoxLayout()
        save_to_file_button = QtGui.QPushButton('Save to File')
        save_to_file_button.clicked.connect(self.save_to_file_clicked)
        copy_to_clipboard_button = QtGui.QPushButton('Copy to Clipboard')
        copy_to_clipboard_button.clicked.connect(self.copy_to_clipboard_clicked)
        send_email_button = QtGui.QPushButton('Send Email')
        send_email_button.clicked.connect(self.send_email_clicked)
        buttons_layout.addWidget(save_to_file_button)
        buttons_layout.addWidget(copy_to_clipboard_button)
        buttons_layout.addWidget(send_email_button)

        # layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(signed_message_label)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)
        self.show()

    def save_to_file_clicked(self):
        filename = QtGui.QFileDialog.getSaveFileName(
            caption='Save to File',
            selectedFilter='*.asc'
        )
        print "Filename", filename

    def copy_to_clipboard_clicked(self):
        pass

    def send_email_clicked(self):
        pass

