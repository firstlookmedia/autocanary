import sys, datetime, platform
from PyQt4 import QtCore, QtGui
from gnupg import GnuPG
from settings import Settings
import common

class AutoCanaryGui(QtGui.QWidget):

    def __init__(self, app, gpg):
        super(AutoCanaryGui, self).__init__()
        self.app = app
        self.gpg = gpg
        self.settings = Settings()
        self.setWindowTitle('AutoCanary')
        self.setWindowIcon(QtGui.QIcon(common.get_image_path('icon.png')))

        # current date
        self.date_layout = QtGui.QHBoxLayout()
        self.date_label = QtGui.QLabel('Date')
        self.date = QtGui.QCalendarWidget()
        self.date.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.date_layout.addWidget(self.date_label)
        self.date_layout.addWidget(self.date)

        # expires
        self.expires_layout = QtGui.QHBoxLayout()
        self.expires_label = QtGui.QLabel('Expires after')
        self.expires = QtGui.QComboBox()
        expires_options = ['1 week', '2 weeks', '1 month', '3 months', '6 months', '1 year']
        for option in expires_options:
            self.expires.addItem(option)
        option = self.settings.get_expires()
        if option in expires_options:
            self.expires.setCurrentIndex(expires_options.index(option))
        self.expires_layout.addWidget(self.expires_label)
        self.expires_layout.addWidget(self.expires)

        # status
        self.status_layout = QtGui.QHBoxLayout()
        self.status_label = QtGui.QLabel('Status')
        self.status = QtGui.QComboBox()
        status_options = ["All good", "It's complicated", "It's bad"]
        for option in status_options:
            self.status.addItem(option)
        option = self.settings.get_status()
        if option in status_options:
            self.status.setCurrentIndex(status_options.index(option))
        self.status_layout.addWidget(self.status_label)
        self.status_layout.addWidget(self.status)

        # canary text box
        self.textbox = QtGui.QTextEdit()
        self.textbox.setText(self.settings.get_text())

        # key selection
        seckeys = gpg.seckeys_list()
        self.key_selection = QtGui.QComboBox()
        for seckey in seckeys:
            uid = seckey['uid']
            if len(uid) >= 53:
                uid = '{0}...'.format(uid[:50])
            fp = seckey['fp'][-8:]
            text = '{0} [{1}]'.format(uid, fp)
            self.key_selection.addItem(text)
        fp = self.settings.get_fp()
        if fp:
            key_i = 0
            for i, seckey in enumerate(seckeys):
                if seckey['fp'] == fp:
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
        self.layout.addLayout(self.date_layout)
        self.layout.addLayout(self.expires_layout)
        self.layout.addLayout(self.status_layout)
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
        date = self.get_date_string()
        expires = str(self.expires.currentText())
        status = str(self.status.currentText())
        text = self.textbox.toPlainText()

        self.settings.set_date(date)
        self.settings.set_expires(expires)
        self.settings.set_status(status)
        self.settings.set_text(text)

        key_i = self.key_selection.currentIndex()
        fp = self.gpg.seckeys_list()[key_i]['fp']
        self.settings.set_fp(fp)

        self.settings.save()

    def get_date_string(self):
        return self.date.selectedDate().toString('MMMM d, yyyy')

    def sign(self):
        date = self.get_date_string()
        expires = str(self.expires.currentText())
        status = str(self.status.currentText())
        text = self.textbox.toPlainText()

        # replace date in text
        text = text.replace('[[DATE]]', self.get_date_string())

        # add headers
        message = 'Date: {0}\nExpires: {1}\nStatus: {2}\n\n{3}'.format(
            date,
            expires,
            status,
            text
        )

        # sign the file
        key_i = self.key_selection.currentIndex()
        fp = self.gpg.seckeys_list()[key_i]['fp']
        signed_message = self.gpg.sign(message, fp)

        if signed_message:
            # todo: build a dialog to display the signed message
            alert(signed_message)
        else:
            alert('Failed to sign message.')

def alert(msg, icon=QtGui.QMessageBox.Warning):
    dialog = QtGui.QMessageBox()
    dialog.setWindowTitle('AutoCanary')
    dialog.setWindowIcon(QtGui.QIcon(common.get_image_path('icon.png')))
    dialog.setText(msg)
    dialog.setIcon(icon)
    dialog.exec_()

def main():
    # start the app
    app = QtGui.QApplication(sys.argv)

    # initialize and check for gpg and a secret key
    gpg = GnuPG()

    system = platform.system()
    if system == 'Darwin':
        if not gpg.is_gpg_available():
            alert('GPG doesn\'t seem to be installed. Install <a href="https://gpgtools.org/">GPGTools</a>, generate a key, and run AutoCanary again.')
            sys.exit(0)

        seckeys = gpg.seckeys_list()
        if len(seckeys) == 0:
            alert('You need an encryption key to use AutoCanary. Run the GPG Keychain program, generate a key, and run AutoCanary again.')
            sys.exit(0)

    elif system == 'Linux':
        seckeys = gpg.seckeys_list()
        if len(seckeys) == 0:
            alert('You need an encryption key to use AutoCanary. Generate a key, and run AutoCanary again.')
            sys.exit(0)
    
    elif system == 'Windows':
        if not gpg.is_gpg_available():
            alert('GPG doesn\'t seem to be installed. Install <a href="http://gpg4win.org/">Gpg4win</a>, generate a key, and run AutoCanary again.')
            sys.exit(0)

        seckeys = gpg.seckeys_list()
        if len(seckeys) == 0:
            alert('You need an encryption key to use AutoCanary. Run the Kleopatra program, generate a new personal OpenPGP key pair, and run AutoCanary again.')
            sys.exit(0)

    # start the gui
    gui = AutoCanaryGui(app, gpg)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
