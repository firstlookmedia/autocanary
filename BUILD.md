# Building AutoCanary

## Mac OS X

To install the right dependencies, you need homebrew and pip installed on your Mac. Follow instructions at http://brew.sh/ to install homebrew, and run `sudo easy_install pip` to install pip.

The first time you're setting up your dev environment:

```sh
brew install qt4 pyqt
sudo pip install py2app
```

To build the .app:

```sh
python setup.py py2app
```

Now you should have `dist/AutoCanary.app`.


## Windows

### Setting up your dev environment

* Download and install the latest python 2.7 from https://www.python.org/downloads/ -- make sure you install the 32-bit version.
* Right click on Computer, go to Properties. Click "Advanced system settings". Click Environment Variables. Under "System variables" double-click on Path to edit it. Add `;C:\Python27;C:\Python27\Scripts` to the end. Now you can just type `python` to run python scripts in the command prompt.
* Go to http://www.riverbankcomputing.com/software/pyqt/download and download the latest PyQt4 for Windows for python 2.7, 32-bit (I downloaded `PyQt4-4.11-gpl-Py2.7-Qt4.8.6-x32.exe`), then install it.

... these instructions are not done yet.


## Linux

Install the dependencies:

'''sh
sudo apt-get install -y build-essential fakeroot python-all python-stdeb python-qt4 gnupg2
```

Build and install the .deb:

```sh
install/build_deb.sh
sudo dpkg -i deb_dist/autocanary_*.deb
```
