#!/usr/bin/env python

# Written by Bram Cohen
# This file is public domain
# The authors disclaim all liability for any damages resulting from
# any use of this software.

import sys
assert sys.version >= '2', "Install Python 2.0 or greater"
from distutils.core import setup, Extension

setup(
    name = "BitTorrent",
    version = "2.5.1",
    author = "Bram Cohen",
    author_email = "<bram@bitconjurer.org>",
    url = "http://www.bitconjurer.org/BitTorrent/",
    license = "Public Domain",
    
    ext_modules = [
    Extension(name    = "_StreamEncrypter",
              sources = ["_StreamEncrypter.c"]
              )
    ],

    packages = ["BitTorrent"],

    scripts = ["btdownloadgui.py", "btdownloadheadless.py", "btdownloadlibrary.py", 
        "btdownloadprefetched.py", "bttrack.py", "btpublish.py"]
    
    )
