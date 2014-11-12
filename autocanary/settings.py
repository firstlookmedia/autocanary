import os, pickle

class Settings(object):

    def __init__(self):
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
                'text': 'As of [[DATE]], (name of organization) has never received or complied with government requests for information.\n\n(name of general counsel)\nGeneral Counsel\n(name of organization)',
                'fp': None
            }

    def save(self):
        pickle.dump(self.settings, open(self.settings_path, 'w'))

