import os, pickle, platform, datetime

class Settings(object):

    def __init__(self):
        system = platform.system()
        if system == 'Windows':
            appdata = os.environ['APPDATA']
            self.settings_path = '{0}\\autocanary_settings'.format(appdata)

        else:
            home = os.path.expanduser("~")
            self.settings_path = '{0}/{1}'.format(home, '.autocanary')

        self.load()

    def get_frequency(self):
        return self.settings['frequency']
    def set_frequency(self, frequency):
        self.settings['frequency'] = frequency

    def get_year(self):
        return self.settings['year']
    def set_year(self, year):
        self.settings['year'] = year

    def get_year_period(self):
        return self.settings['year_period']
    def set_year_period(self, year_period):
        self.settings['year_period'] = year_period

    def get_status(self):
        return self.settings['status']
    def set_status(self, status):
        self.settings['status'] = status

    def get_text(self):
        return self.settings['text']
    def set_text(self, text):
        self.settings['text'] = text

    def get_fp(self):
        return self.settings['fp']
    def set_fp(self, fp):
        self.settings['fp'] = fp

    def load(self):
        if os.path.isfile(self.settings_path):
            self.settings = pickle.load(open(self.settings_path))
        else:
            # default settings
            self.settings = {
                'frequency': 'Semiannually',
                'year': str(datetime.date.today().year),
                'year_period': 'Q12',
                'status': None,
                'text': """During this period, (name of organization) has not received any National Security Letters or FISA court orders, and we have not been subject to any gag order by a FISA court, or any other similar court of any government.

(Name of general counsel)
General Counsel
(Name of organization)""",
                'fp': None
            }

    def save(self):
        pickle.dump(self.settings, open(self.settings_path, 'w'))
