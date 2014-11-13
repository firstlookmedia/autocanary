import os, pickle, platform

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
                'text': """As of [[DATE]], (name of organization) has not received any National Security Letters or FISA court orders, and we have not been subject to any gag order by a FISA court, or any other similar court of any government. (Name of organization) has never placed any backdoors in our hardware or software and has not received any requests to do so. (Name of organization) has never disclosed any user communications to any third party.

(Name of general counsel)
General Counsel
(Name of organization)""",
                'fp': None
            }

    def save(self):
        pickle.dump(self.settings, open(self.settings_path, 'w'))
