#!/bin/bash

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
TITLE=AutoCanary
SIGNING_IDENTITY_APP="Developer ID Application: Micah Lee"
SIGNING_IDENTITY_INSTALLER="Developer ID Installer: Micah Lee"

cd $ROOT

# deleting dist
echo Deleting dist folder
rm -rf $ROOT/dist &>/dev/null 2>&1

# build the .app
echo Building AutoCanary.app
python setup.py py2app

# codesign the app
echo Codesigning and building installer
python $ROOT/install/prepare_for_codesign.py
cd $ROOT/dist
codesign --deep --verbose --sign "$SIGNING_IDENTITY_APP" AutoCanary.app
productbuild --component AutoCanary.app /Applications AutoCanary.pkg --sign "$SIGNING_IDENTITY_INSTALLER"
cd $ROOT
