# Python script for generating a cover for the original Tri-Bahtinov Mask 

This directory contains the source code of _cover_v1_ that I have
written in python for generating a Tri-Bahtinov mask cover for the original
Tri-Bahtinov mask. To make a cover for S. Takagi's improved version of
the Tri-Bahtinov mask use _cover_v2_.

This cover is used for covering two of the three Bahtinov
patterns. The cover is to make it easy to use K. Evan's [Tri-Bahtinov
Grabber program](https://github.com/1CM69/Tri-Bahtinov_Grabber).


## Executing cover_v1.py

The python version has to be version 2.7.x

I use [cairo](https://cairographics.org/) graphics for generating the
tribahtinov mask cover, you will have to download and install graphics
libraries that I list below. Since I develop on the Mac, I cannot
guarantee that the instructions below are 100% correct for other
platforms.

### Required libraries

The necessary libraries and python programs necessary to get
the _cover_v1.py_ to work are detailed below. I've divided them into two
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
  
## Running cover_v1.py

To run _cover_v1.py_, you can do the following:
```
python cover_v1.py
```
## The result

Here is a typical result of the cover that covers 2 of the 3 Bahtinov patterns.

![Tri-Bahtinov mask cover](https://github.com/cytan299/tribahtinov/blob/master/pics/cover1.png)

## Copyright

The software that is written by the author is copyright 2018 C.Y. Tan
and released under GPLv3.


