# Python script for generating a Tri-Bahtinov Mask

This directory contains the source code of _generate_ that I have
written in python for generating a Tri-Bahtinov mask for your
telescope.

## Using generate.py

The easiest way to use _generate_ is download the executable that is
in 
[releases](https://github.com/cytan299/tribahtinov/releases). Please
read the README.md file in that directory for installation
directions. If you do this, then the following instructions do not
apply.

## Executing generate.py

I use [cairo](https://cairographics.org/) graphics for generating the
tribahtinov mask, you will have to download and install graphics
libraries that I list below. Since I develop on the Mac, I cannot
guarantee that the instructions below are 100% correct for other
platforms.

### Required libraries

The necessary libraries and python programs necessary to get
the _generate.py_ to work are detailed below. I've divided them into two
sections for _Mac  OS X_ and _Windows_.

#### Mac OS X

* **pip** This python script is necessary for installing the cairocffi
library. On _Mac OS X_, do the following:
```
sudo easy_install pip
```
For _Linux_,  (I cannot test this, because I don't run _Linux_), 
the pip python script can be downloaded from
[here](https://pip.pypa.io/en/stable/installing/). It is installed using
```
python get-pip.py
```
* **cairocffi** For my python script to work, it is necessary to
  install the [cairocffi](https://github.com/SimonSapin/cairocffi)
  library. Do the following to install it:
```
  sudo -H pip install cairocffi
  ```
* **cairo** Finally, you have to install
[macports][http://www.macports.org] and then install _cairo_
```
sudo port install cairo
```

#### Windows
It is a lot more involved for getting _generate.py_ to run in
_Windows_.

* **python** (Python)[https://www.python.org/downloads/] must be
  installed. I use version 2.7.10 which is the version that also comes
  with _Mac OS X_. 
* **pip** _pip_ comes with the the _python_ installation.
* **Microsoft Visual C++ Compiler for Python 2.7** Before installing
  _cairocffi_, you must also have installed. You can download it
  [here](https://www.microsoft.com/en-us/download/details.aspx?id=44266).
* **cairocffi** _cairocffi_ can be installed using
```
python install cairocffi
```
* **cairo** _cairo_ must be downloaded from
  [here](http://ftp.gnome.org/pub/GNOME/binaries/win64/gtk+/2.22/gtk+-bundle_2.22.1-20101229_win64.zip). Unzip
  and rename the root directory in the zip file to _c:\GTK_.
  
## Running generate.py

To run _generate.py_, you can do the following:
```
python generate.py
```

## Generating executables

I generated _Mac OS X_ and _Windows_ executables using
[PyInstaller](http://www.pyinstaller.org/). _PyInstaller_ is installed
with the following command
```
pip install pyinstaller
```
I generate the executables using
```
pyinstaller --onefile generate.py
```
The _build_ directory contains the executable _generate_
created by _pyinstaller_.

I bundle the _generate_ that I created on both _Mac OS X_ and
_Windows_ platforms in the
[releases](https://github.com/cytan299/tribahtinov/releases) directory.

## Copyright

The software that is written by the author is copyright 2016 C.Y. Tan
and released under GPLv3.


