"""
AutoCanary | https://firstlook.org/code/autocanary
Copyright (c) 2015 First Look Media

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
