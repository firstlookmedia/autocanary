import os, sys, inspect, platform

def get_autocanary_dir():
    if platform.system() == 'Darwin':
        autocanary_dir = os.path.dirname(__file__)
    else:
        autocanary_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return autocanary_dir

autocanary_dir = get_autocanary_dir()

def get_image_path(filename):
    if platform.system() == 'Linux':
        prefix = os.path.join(sys.prefix, 'share/autocanary')
    else:
        prefix = os.path.join(os.path.dirname(get_autocanary_dir()), 'share')
    return os.path.join(prefix, filename)
