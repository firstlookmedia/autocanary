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
from distutils.core import setup

version = open('share/version').read().strip().lstrip('v')

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
