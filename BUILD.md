# Building AutoCanary

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
