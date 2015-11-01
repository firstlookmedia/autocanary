# Building AutoCanary

## Mac OS X

Install the [latest python 2.x](https://www.python.org/downloads/) from python.org. If you use the built-in version of python that comes with OS X, your .app might not run on other people's computers.

To install the right dependencies, you need homebrew and pip installed on your Mac. Follow instructions at http://brew.sh/ to install homebrew, and run `sudo easy_install pip` to install pip.

The first time you're setting up your dev environment:

```sh
brew install qt4 pyqt
sudo pip install py2app
```

To run locally:

```sh
python autocanary.py
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

Setting up your dev environment:

* Download and install the latest python 2.7 from https://www.python.org/downloads/ -- make sure you install the 32-bit version.
* Right click on Computer, go to Properties. Click "Advanced system settings". Click Environment Variables. Under "System variables" double-click on Path to edit it. Add `;C:\Python27;C:\Python27\Scripts` to the end. Now you can just type `python` to run python scripts in the command prompt.
* Go to http://www.riverbankcomputing.com/software/pyqt/download and download the latest PyQt4 for Windows for python 2.7, 32-bit (I downloaded `PyQt4-4.11-gpl-Py2.7-Qt4.8.6-x32.exe`), then install it.
* Go to http://www.py2exe.org/ and download the latest 32-bit version of py2exe (I downloaded `py2exe-0.6.9.win32-py2.7.exe`), then install it.
* Go to http://sourceforge.net/projects/pywin32/ and download and install the latest 32-bit pywin32 binary for python 2.7. I downloaded `pywin32-219.win32-py2.7.exe`.
* Download and install the [Microsoft Visual C++ 2008 Redistributable Package (x86)](http://www.microsoft.com/en-us/download/details.aspx?id=29).
* Copy `MSVCP90.dll` (I found mine in `C:\Windows\winsxs\*`) into `C:\Python27\DLLs`.

If you want to build the installer:

* Go to http://nsis.sourceforge.net/Download and download the latest NSIS. I downloaded `nsis-3.0b0-setup.exe`.
* Right click on Computer, go to Properties. Click "Advanced system settings". Click Environment Variables. Under "System variables" double-click on Path to edit it. Add `;C:\Program Files (x86)\NSIS` to the end. Now you can just type `makensisw [script]` to build an installer.

If you want to sign binaries with Authenticode:

* Go to http://msdn.microsoft.com/en-us/vstudio/aa496123 and install the latest .NET Framework. I installed `.NET Framework 4.5.1`.
* Go to http://www.microsoft.com/en-us/download/confirmation.aspx?id=8279 and install the Windows SDK.
* Right click on Computer, go to Properties. Click "Advanced system settings". Click Environment Variables. Under "System variables" double-click on Path to edit it. Add `;C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin` to the end.
* You'll also, of course, need a code signing certificate. I roughly followed [this guide](http://blog.assarbad.net/20110513/startssl-code-signing-certificate/) to make one using my StartSSL account.
* Once you get a code signing key and certificate and covert it to a pfx file, import it into your certificate store.

### To make a .exe:

* Open a command prompt, cd into the autocanary directory, and type: `python setup.py py2exe`. Inside the `dist` folder you will find `autocanary.exe`.

### To build the installer:

Note that you must have a code signing certificate installed in order to use the `build_exe.bat` script, because it tries code signing `autocanary.exe`, as well as `AutoCanary_Setup.exe` and `uninstall.exe`.

Open a command prompt, cd to the autocanary directory, and type: `install\build_exe.bat`

A NSIS window will pop up, and once it's done you will have `dist\AutoCanary_Setup.exe`.

## Linux

Install the dependencies:

```sh
sudo apt-get install -y build-essential fakeroot python-all python-stdeb python-qt4 gnupg2
```

To run locally:

```sh
python autocanary.py
```

Build and install the .deb:

```sh
install/build_deb.sh
sudo dpkg -i deb_dist/autocanary_*.deb
```
