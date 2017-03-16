#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
cd $DIR

VERSION=`cat share/version`
VERSION=${VERSION:1}

# clean up from last build
rm -r deb_dist >/dev/null 2>&1

# build binary package
python3 setup.py --command-packages=stdeb.command bdist_deb

# install it
echo ""
echo "To install, run:"
echo "sudo dpkg -i deb_dist/autocanary_$VERSION-1_all.deb"
