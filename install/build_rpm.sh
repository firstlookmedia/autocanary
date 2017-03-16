#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
cd $DIR

VERSION=`cat share/version`
VERSION=${VERSION:1}

# clean up from last build
rm -r build dist >/dev/null 2>&1

# build binary package
python3 setup.py bdist_rpm --requires="python3-qt5 python3-feedparser gnupg2"

# install it
echo ""
echo "To install, run:"
echo "sudo dnf install dist/autocanary-$VERSION-1.noarch.rpm"
