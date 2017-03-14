# Building AutoCanary

## Mac OS X

Install Xcode from the Mac App Store. Once it's installed, run it for the first time to set it up.

Install Python 3.5.3 from https://www.python.org/downloads/release/python-353/. I downloaded `python-3.5.3-macosx10.6.pkg`. (Note that PyQt does not yet work with Python 3.6.)

Install Qt 5.7.1 from https://www.qt.io/download-open-source/. I downloaded `qt-unified-mac-x64-2.0.4-online.dmg`. In the installer, you can skip making an account, and all you need is Qt 5.7 for macOS.

Now install some python dependencies with pip (note, there's issues building a .app if you install this in a virtualenv):

```sh
sudo pip3 install -r install/requirements.txt
```

To run during development:

```sh
./dev_scripts/autocanary
```

To build the .app:

```sh
install/build_osx.sh
```

Now you should have `dist/AutoCanary.app`.

To build a codesigned and ready to distribute .pkg (note, you must be a Mac Developer to do this, and you'll need to edit `build_osx.sh` to use your own signing identity):

```sh
install/build_osx.sh --sign
```

Now you should have `dist/AutoCanary.pkg`.

## Windows

### Setting up your dev environment

Download the latest Python 3.5.2, 32-bit (x86) from https://www.python.org/downloads/release/python-352/ (note that there's a pyinstaller/pywin32 bug that prevents 3.6.x from working). I downloaded `python-3.5.2.exe`. When installing it, make sure to check the "Add Python 3.5 to PATH" checkbox on the first page of the installer.

Open a command prompt, cd to the onionshare folder, and install dependencies with pip:

```cmd
pip3 install -r install\requirements.txt
```

Download and install Qt5 from https://www.qt.io/download-open-source/. I downloaded `qt-unified-windows-x86-2.0.4-online.exe`. There's no need to login to a Qt account during installation. Make sure you install the latest Qt 5.x. I installed Qt 5.7.

To run during development:

```
python dev_scripts\autocanary
```

If you want to build a .exe:

These instructions include adding folders to the path in Windows. To do this, go to Start and type "advanced system settings", and open "View advanced system settings" in the Control Panel. Click Environment Variables. Under "System variables" double-click on Path. From there you can add and remove folders that are available in the PATH.

Download and install the 32-bit [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-US/download/details.aspx?id=48145). I downloaded `vc_redist.x86.exe`.

Download and install the standalone [Windows 10 SDK](https://dev.windows.com/en-us/downloads/windows-10-sdk). Note that you may not need this if you already have Visual Studio. Add the following directories to the path:

* `C:\Program Files (x86)\Windows Kits\10\bin\x86`
* `C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x86`
* `C:\Users\user\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\PyQt5\Qt\bin`

If you want to build the installer:

* Go to http://nsis.sourceforge.net/Download and download the latest NSIS. I downloaded `nsis-3.01-setup.exe`.
* Add `C:\Program Files (x86)\NSIS` to the path.

If you want to sign binaries with Authenticode:

* You'll need a code signing certificate.
* Once you get a code signing key and certificate and covert it to a pfx file, import it into your certificate store.

### To make a .exe:

For PyInstaller to work, you might need to edit `Scripts\pyinstaller-script.py` in your Python 3.5 folder, to work around [this bug](https://stackoverflow.com/questions/31808180/installing-pyinstaller-via-pip-leads-to-failed-to-create-process) in pip.

* Open a command prompt, cd into the autocanary directory, and type: `pyinstaller install\autocanary.spec`. `autocanary.exe` and all of their supporting files will get created inside the `dist` folder.

### To build the installer:

Note that you must have a codesigning certificate installed in order to use the `install\build_exe.bat` script, because it codesigns `autocanary.exe`, `uninstall.exe`, and `AutoCanary_Setup.exe`.

Open a command prompt, cd to the onionshare directory, and type: `install\build_exe.bat`

This will prompt you to codesign three binaries and execute one unsigned binary. When you're done clicking through everything you will have `dist\AutoCanary_Setup.exe`.

## Linux

Install the dependencies:

For Debian-like distros: `sudo apt install -y build-essential fakeroot python3-all python3-stdeb python3-qt5 python3-feedparser gnupg2`

For Fedora-like distros: `sudo dnf install rpm-build python3-qt5 gnupg2 python3-feedparser`

To run during development:

```sh
python autocanary.py
```

You can also build AutoCanary packages to install:

Create a .deb on Debian-like distros: `./install/build_deb.sh`

Create a .rpm on Fedora-like distros: `./install/build_rpm.sh`
