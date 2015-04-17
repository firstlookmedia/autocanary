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
