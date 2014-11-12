import sys, datetime, platform
from PyQt4 import QtCore, QtGui
from gnupg import GnuPG
from settings import Settings

class AutoCanaryGui(QtGui.QWidget):

    def __init__(self, app, gpg):
        super(AutoCanaryGui, self).__init__()
        self.app = app
        self.gpg = gpg
        self.settings = Settings()
        self.setWindowTitle('AutoCanary')

        # canary text box
        self.textbox = QtGui.QTextEdit()
        self.textbox.setText(self.settings.get_text())

        # key selection
        seckeys = gpg.seckeys_list()
        print seckeys
        self.key_selection = QtGui.QComboBox()
        for seckey in seckeys:
            uid = seckey['uid']
            if len(uid) >= 53:
                uid = '{0}...'.format(uid[:50])
            keyid = seckey['keyid'][-8:]
            text = '{0} [{1}]'.format(uid, keyid)
            self.key_selection.addItem(text)
        keyid = self.settings.get_keyid()
        if keyid:
            key_i = 0
            for i, seckey in enumerate(seckeys):
                if seckey['keyid'] == keyid:
                    key_i = i
            self.key_selection.setCurrentIndex(key_i)

        # buttons
        self.buttons_layout = QtGui.QHBoxLayout()
        self.sign_save_button = QtGui.QPushButton('Save and Sign')
        self.sign_save_button.clicked.connect(self.sign_save_clicked)
        self.sign_once = QtGui.QPushButton('One-Time Sign')
        self.sign_once.clicked.connect(self.sign_once_clicked)
        self.buttons_layout.addWidget(self.sign_save_button)
        self.buttons_layout.addWidget(self.sign_once)

        # layout
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.key_selection)
        self.layout.addLayout(self.buttons_layout)
        self.setLayout(self.layout)
        self.show()

    def sign_save_clicked(self):
        self.save()
        self.sign()

    def sign_once_clicked(self):
        self.sign()

    def save(self):
        text = self.textbox.toPlainText()
        self.settings.set_text(text)

        key_i = self.key_selection.currentIndex()
        fp = self.gpg.seckeys_list()[key_i]['fp']
        self.settings.set_fp(fp)

        self.settings.save()

    def sign(self):
        # replace date in text
        text = self.textbox.toPlainText()
        current_date = datetime.date.today().strftime("%B %d, %Y")
        text = text.replace('[[DATE]]', current_date)

        # sign the file
        key_i = self.key_selection.currentIndex()
        fp = self.gpg.seckeys_list()[key_i]['fp']
        signed_message = self.gpg.sign(text, fp)

        if signed_message:
            # todo: build a dialog to display the signed message
            alert(signed_message)
        else:
            alert('Failed to sign message.')

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
    gpg = GnuPG()
    seckeys = gpg.seckeys_list()

    system = platform.system()
    if system == 'Darwin':
        if not gpg.is_gpg_available():
            alert('GPG doesn\'t seem to be installed. Install <a href="https://gpgtools.org/">GPGTools</a>, generate a key, and run AutoCanary again.')
            sys.exit(0)

        if len(seckeys) == 0:
            alert('You need an encryption key to use AutoCanary. Run the GPG Keychain program, generate a key, and run AutoCanary again.')
            sys.exit(0)

    elif system == 'Linux':
        if len(seckeys) == 0:
            alert('You need an encryption key to use AutoCanary. Generate a key, and run AutoCanary again.')
            sys.exit(0)

    # start the gui
    gui = AutoCanaryGui(app, gpg)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

