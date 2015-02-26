#!/bin/bash

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
TITLE=AutoCanary

cd $ROOT

# deleting dist
echo Deleting dist folder
rm -rf $ROOT/dist &>/dev/null 2>&1

# build the .app
echo Building AutoCanary.app
python setup.py py2app

# codesign the app
# note: you need to be a Mac Developer to do this
#echo Codesigning all of the frameworks, and finally the .app itself
#DEVELOPER_ID="Micah Lee"
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtCore.framework/Versions/4/QtCore
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtDeclarative.framework/Versions/4/QtDeclarative
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtGui.framework/Versions/4/QtGui
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtHelp.framework/Versions/4/QtHelp
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtMultimedia.framework/Versions/4/QtMultimedia
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtNetwork.framework/Versions/4/QtNetwork
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtScript.framework/Versions/4/QtScript
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtScriptTools.framework/Versions/4/QtScriptTools
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtSql.framework/Versions/4/QtSql
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtSvg.framework/Versions/4/QtSvg
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/QtXmlPatterns.framework/Versions/4/QtXmlPatterns
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app/Contents/Frameworks/libQtCLucene.4.8.6.dylib
#codesign --force --verify --verbose --sign "$DEVELOPER_ID" $ROOT/dist/AutoCanary.app

