import os, pickle

class Settings(object):

    def __init__(self):
        self.settings_path = os.path.abspath('~/.autocanary')
        self.load()


    def get_text(self):
        return self.settings['text']


    def get_fp(self):
        return self.settings['fp']


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

