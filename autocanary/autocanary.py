import sys
from PyQt4 import QtCore, QtGui
import gnupg

class AutoCanaryGui(QtGui.QWidget):
    def __init__(self, app, gpg):
        super(AutoCanaryGui, self).__init__()
        self.app = app
        self.gpg = gpg
        self.setWindowTitle('AutoCanary')

        # canary text box
        self.textbox = QtGui.QTextEdit()

        # key selection
        self.key_layout = QtGui.QHBoxLayout()
        self.key_label = QtGui.QLabel('Sign statement with')
        self.key_selection = QtGui.QComboBox()
        self.key_layout.addWidget(self.key_label)
        self.key_layout.addWidget(self.key_selection)

        # buttons
        self.buttons_layout = QtGui.QHBoxLayout()
        self.sign_save_button = QtGui.QPushButton('Save & Sign')
        self.sign_once = QtGui.QPushButton('One-Time Sign')
        self.buttons_layout.addWidget(self.sign_save_button)
        self.buttons_layout.addWidget(self.sign_once)

        # layout
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.textbox)
        self.layout.addLayout(self.key_layout)
        self.layout.addLayout(self.buttons_layout)
        self.setLayout(self.layout)
        self.show()


def alert(msg, icon=QtGui.QMessageBox.Warning):
    dialog = QtGui.QMessageBox()
    dialog.setWindowTitle('AutoCanary')
    dialog.setText(msg)
    dialog.setIcon(icon)
    dialog.exec_()


def main():
    # start the app
    app = QtGui.QApplication(sys.argv)

    # initialize and check for gpg and a secret key
    gpg = gnupg.GnuPG()
    if not gpg.is_gpg_available():
        alert('GPG doesn\'t seem to be installed. Install <a href="https://gpgtools.org/">GPGTools</a>, generate a key, and run AutoCanary again.')
        sys.exit(0)
    seckeys = gpg.seckeys_list()
    if len(seckeys) == 0:
        alert('You need an encryption key to use AutoCanary. Run the GPG Keychain program, generate a key, and run AutoCanary again.')
        sys.exit(0)

    # start the gui
    gui = AutoCanaryGui(app, gpg)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

