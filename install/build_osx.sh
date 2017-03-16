#!/bin/bash
ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
cd $ROOT

# Deleting old build folders folders
echo Deleting old build folders folders
rm -rf $ROOT/build $ROOT/dist &>/dev/null 2>&1

# Build the .app
echo Building AutoCanary.app
pyinstaller install/pyinstaller.spec

if [ "$1" = "--release" ]; then
  mkdir -p dist
  APP_PATH="dist/AutoCanary.app"
  PKG_PATH="dist/AutoCanary.pkg"
  IDENTITY_NAME_APPLICATION="Developer ID Application: FIRST LOOK PRODUCTIONS, INC."
  IDENTITY_NAME_INSTALLER="Developer ID Installer: FIRST LOOK PRODUCTIONS, INC."

  echo "Codesigning the app bundle"
  codesign --deep -s "$IDENTITY_NAME_APPLICATION" "$APP_PATH"

  echo "Creating an installer"
  productbuild --sign "$IDENTITY_NAME_INSTALLER" --component "$APP_PATH" /Applications "$PKG_PATH"

  echo "Cleaning up"
  rm -rf "$APP_PATH"

  echo "All done, your installer is in: $PKG_PATH"
fi
