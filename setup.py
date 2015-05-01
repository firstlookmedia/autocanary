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
import os, sys, platform
system = platform.system()

if system == "Windows":
    from distutils.core import setup
else:
    from setuptools import setup

version = open('version').read().strip()

if system == 'Linux':
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

elif system == 'Darwin':
    setup(
        name='AutoCanary',
        version=version,
        app=['autocanary.py'],
        data_files=[],
        options={
            'py2app': {
                'argv_emulation': True,
                'iconfile':'install/icon.icns',
                'includes': ['sip', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui'],
                'excludes': ['PyQt4.QtDesigner', 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL', 'PyQt4.QtScript', 'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.QtXml', 'PyQt4.phonon']
            }
        },
        setup_requires=['py2app'],
    )

elif system == 'Windows':
    import py2exe
    setup(
        name='AutoCanary',
        version=version,
        data_files=[('', ['share/icon.png'])],
        windows=[{'script':'autocanary.py'}],
        options={
            'py2exe': {
                'includes': ['sip', 'PyQt4'],
                'bundle_files': 1,
                'compressed': True
            }
        }
    )
