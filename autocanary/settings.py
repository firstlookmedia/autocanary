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
                'status': None,
                'text': """During this period, (name of organization) has received:

Zero National Security Letters
Zero Foreign Intelligence Surveillance Court orders
Zero gag orders that prevent us from from stating that we have received legal process seeking our customers' information

(Name of general counsel)
General Counsel
(Name of organization)""",
                'fp': None
            }

    def save(self):
        pickle.dump(self.settings, open(self.settings_path, 'w'))
