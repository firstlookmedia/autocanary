import os, sys, platform
from glob import glob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = open('version').read().strip()

setup(
    name='autocanary',
    version=version,
    author='Micah Lee',
    author_email='micah.lee@firstlook.org',
    packages=['autocanary'],
    include_package_data=True,
    scripts=['install/autocanary'],
    data_files=[
        (os.path.join(sys.prefix, 'share/applications'), ['install/autocanary.desktop']),
        (os.path.join(sys.prefix, 'share/pixmaps'), ['install/autocanary.xpm']),
        (os.path.join(sys.prefix, 'share/autocanary'), ['share/icon.png'])
    ]
)
