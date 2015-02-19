import sys, datetime, platform
from PyQt4 import QtCore, QtGui
from gnupg import GnuPG
from settings import Settings
from output_dialog import OutputDialog
import common

class AutoCanaryGui(QtGui.QWidget):

    def __init__(self, app, gpg):
        super(AutoCanaryGui, self).__init__()
        self.app = app
        self.gpg = gpg
        self.settings = Settings()
        self.setWindowTitle('AutoCanary')
        self.setWindowIcon(QtGui.QIcon(common.get_image_path('icon.png')))

        # frequency, year
        self.date_col1_layout = QtGui.QVBoxLayout()

        self.frequency_layout = QtGui.QHBoxLayout()
        self.frequency_label = QtGui.QLabel('Frequency')
        self.frequency = QtGui.QComboBox()
        frequency_options = ["Quarterly", "Semiannually"]
        for option in frequency_options:
            self.frequency.addItem(option)
        option = self.settings.get_frequency()
        if option in frequency_options:
            self.frequency.setCurrentIndex(frequency_options.index(option))
        self.frequency_layout.addWidget(self.frequency_label)
        self.frequency_layout.addWidget(self.frequency)
        self.frequency.activated.connect(self.update_date)

        self.year_layout = QtGui.QHBoxLayout()
        self.year_label = QtGui.QLabel('Year')
        self.year = QtGui.QComboBox()
        y = datetime.date.today().year
        year_options = [str(y-1), str(y), str(y+1)]
        for option in year_options:
            self.year.addItem(option)
        option = self.settings.get_year()
        if option in year_options:
            self.year.setCurrentIndex(year_options.index(option))
            print self.year.currentIndex()
        self.year_layout.addWidget(self.year_label)
        self.year_layout.addWidget(self.year)
        self.year.activated.connect(self.update_date)

        # quarterly radio buttons
        self.quarterly_layout = QtGui.QHBoxLayout()
        self.quarterly_label = QtGui.QLabel('Quarter')
        self.quarterly_q1 = QtGui.QRadioButton("")
        self.quarterly_q2 = QtGui.QRadioButton("")
        self.quarterly_q3 = QtGui.QRadioButton("")
        self.quarterly_q4 = QtGui.QRadioButton("")
        self.quarterly_layout.addWidget(self.quarterly_label)
        self.quarterly_layout.addWidget(self.quarterly_q1)
        self.quarterly_layout.addWidget(self.quarterly_q2)
        self.quarterly_layout.addWidget(self.quarterly_q3)
        self.quarterly_layout.addWidget(self.quarterly_q4)

        # semiannual radio buttons
        self.semiannually_layout = QtGui.QHBoxLayout()
        self.semiannually_label = QtGui.QLabel('Semester')
        self.semiannually_q12 = QtGui.QRadioButton("")
        self.semiannually_q34 = QtGui.QRadioButton("")
        self.semiannually_layout.addWidget(self.semiannually_label)
        self.semiannually_layout.addWidget(self.semiannually_q12)
        self.semiannually_layout.addWidget(self.semiannually_q34)

        year_period = self.settings.get_year_period()
        if year_period == 'Q1':
            self.quarterly_q1.setChecked(True)
        elif year_period == 'Q2':
            self.quarterly_q2.setChecked(True)
        elif year_period == 'Q3':
            self.quarterly_q3.setChecked(True)
        elif year_period == 'Q4':
            self.quarterly_q4.setChecked(True)
        elif year_period == 'Q12':
            self.semiannually_q12.setChecked(True)
        elif year_period == 'Q34':
            self.semiannually_q34.setChecked(True)

        # date layout
        self.date_layout = QtGui.QVBoxLayout()
        self.date_layout.addLayout(self.frequency_layout)
        self.date_layout.addLayout(self.year_layout)
        self.date_layout.addLayout(self.quarterly_layout)
        self.date_layout.addLayout(self.semiannually_layout)

        self.update_date()

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
        self.layout.addLayout(self.status_layout)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.key_selection)
        self.layout.addLayout(self.buttons_layout)
        self.setLayout(self.layout)
        self.show()

    def update_date(self):
        # show either quarterly radio buttons or semiannually radio buttons
        if self.frequency.currentText() == 'Quarterly':
            # show quarterly
            self.quarterly_label.show()
            self.quarterly_q1.show()
            self.quarterly_q2.show()
            self.quarterly_q3.show()
            self.quarterly_q4.show()

            # hide semiannually
            self.semiannually_label.hide()
            self.semiannually_q12.hide()
            self.semiannually_q34.hide()

            # make sure a quarterly radio button is checked
            if not self.quarterly_q1.isChecked() and not self.quarterly_q2.isChecked() and not self.quarterly_q3.isChecked() and not self.quarterly_q4.isChecked():
                self.quarterly_q1.setChecked(True)
        else:
            # show semiannually
            self.semiannually_label.show()
            self.semiannually_q12.show()
            self.semiannually_q34.show()

            # hide quarterly
            self.quarterly_label.hide()
            self.quarterly_q1.hide()
            self.quarterly_q2.hide()
            self.quarterly_q3.hide()
            self.quarterly_q4.hide()

            # make sure a semiannually radio button is checked
            if not self.semiannually_q12.isChecked() and not self.semiannually_q34.isChecked():
                self.semiannually_q12.setChecked(True)

        # update freqency text
        year = self.year.currentText()
        self.quarterly_q1.setText('Q1 {}'.format(year));
        self.quarterly_q2.setText('Q2 {}'.format(year));
        self.quarterly_q3.setText('Q3 {}'.format(year));
        self.quarterly_q4.setText('Q4 {}'.format(year));
        self.semiannually_q12.setText('Q1 and Q2 {}'.format(year))
        self.semiannually_q34.setText('Q3 and Q4 {}'.format(year))

    def get_year_period(self):
        if self.quarterly_q1.isChecked():
            year_period = 'Q1'
        if self.quarterly_q2.isChecked():
            year_period = 'Q2'
        if self.quarterly_q3.isChecked():
            year_period = 'Q3'
        if self.quarterly_q4.isChecked():
            year_period = 'Q4'
        if self.semiannually_q12.isChecked():
            year_period = 'Q12'
        if self.semiannually_q34.isChecked():
            year_period = 'Q34'
        return year_period

    def sign_save_clicked(self):
        self.save()
        self.sign()

    def sign_once_clicked(self):
        self.sign()

    def save(self):
        frequency = self.frequency.currentText()
        year = self.year.currentText()
        year_period = self.get_year_period()
        status = str(self.status.currentText())
        text = self.textbox.toPlainText()

        self.settings.set_frequency(frequency)
        self.settings.set_year(year)
        self.settings.set_year_period(year_period)
        self.settings.set_status(status)
        self.settings.set_text(text)

        key_i = self.key_selection.currentIndex()
        fp = self.gpg.seckeys_list()[key_i]['fp']
        self.settings.set_fp(fp)

        self.settings.save()

    def sign(self):
        frequency = self.frequency.currentText()
        year = self.year.currentText()
        year_period = self.get_year_period()
        status = str(self.status.currentText())
        text = self.textbox.toPlainText()

        # add headers
        if year_period == 'Q1':
            period_date = 'January 1 to March 31'
        if year_period == 'Q2':
            period_date = 'April 1 to June 30'
        if year_period == 'Q3':
            period_date = 'July 1 to September 30'
        if year_period == 'Q4':
            period_date = 'October 1 to December 31'
        if year_period == 'Q12':
            period_date = 'January 1 to June 30'
        if year_period == 'Q34':
            period_date = 'July 1 to December 31'
        message = 'Status: {}\nPeriod: {}, {}\n\n{}'.format(status, period_date, year, text)

        # sign the file
        key_i = self.key_selection.currentIndex()
        fp = self.gpg.seckeys_list()[key_i]['fp']
        signed_message = self.gpg.sign(message, fp)

        if signed_message:
            # display signed message
            dialog = OutputDialog(self.app, signed_message)
            dialog.exec_()
        else:
            common.alert('Failed to sign message.')

def main():
    # start the app
    app = QtGui.QApplication(sys.argv)

    # initialize and check for gpg and a secret key
    gpg = GnuPG()

    system = platform.system()
    if system == 'Darwin':
        if not gpg.is_gpg_available():
            common.alert('GPG doesn\'t seem to be installed. Install <a href="https://gpgtools.org/">GPGTools</a>, generate a key, and run AutoCanary again.')
            sys.exit(0)

        seckeys = gpg.seckeys_list()
        if len(seckeys) == 0:
            common.alert('You need an encryption key to use AutoCanary. Run the GPG Keychain program, generate a key, and run AutoCanary again.')
            sys.exit(0)

    elif system == 'Linux':
        seckeys = gpg.seckeys_list()
        if len(seckeys) == 0:
            common.alert('You need an encryption key to use AutoCanary. Generate a key, and run AutoCanary again.')
            sys.exit(0)

    elif system == 'Windows':
        if not gpg.is_gpg_available():
            common.alert('GPG doesn\'t seem to be installed. Install <a href="http://gpg4win.org/">Gpg4win</a>, generate a key, and run AutoCanary again.')
            sys.exit(0)

        seckeys = gpg.seckeys_list()
        if len(seckeys) == 0:
            common.alert('You need an encryption key to use AutoCanary. Run the Kleopatra program, generate a new personal OpenPGP key pair, and run AutoCanary again.')
            sys.exit(0)

    # start the gui
    gui = AutoCanaryGui(app, gpg)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
