﻿# Welcome to pyNES!
I've always wanted a straightforward way to launch NES ROMs on a Pi, without the need to use a keyboard or mouse after the very first setup. This is part of the system to get that done!


# Prerequisites 

 - Python 2.7 + pip
 - npyscreen (*via pip*)
 - FCEUX
 - antimicro or joy2key (*antimicro config included*)
		 
*NOTE: I'm using FCEUX but you can modify the script to utilize whatever emulator you prefer*

## Installation & Usage

Just place the files in the directory of your choice and execute with `python2.7 main.py`

Just remember to modify the values inside the script to match your ROM $PATH. I've included a very basic antimicro config that matches what you will find in the Python script.
