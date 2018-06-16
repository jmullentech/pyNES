#!/usr/bin/env python2.7
# encoding: utf-8

import sys, os
import subprocess
import fnmatch
import npyscreen, curses
import logging

# NOT NEEDED
#logging.basicConfig(level=logging.DEBUG, filename='tst.log')
#logger = logging.getLogger()

# CHANGE THIS TO MATCH YOUR ROM $PATH
rompath = '/home/john/NES/ROMs'

gameList = []
for root, dirnames, filenames in os.walk(rompath):
    for filename in fnmatch.filter(filenames, '*.nes'):
        gameList.append(os.path.join(root, filename))
        gameList.sort()

class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Welcome to pyNES v0.2a!")

class InstructText(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class Browser(npyscreen.BoxTitle):
    _contained_widget = npyscreen.SelectOne
class MainForm(npyscreen.FormBaseNew):
    def create(self): 
        
    	self.add_event_hander("exit_func", self.exit_func)
        
    	# I'm using 'CTRL-F' and 'r' here but you can change this to whatever you want
    	# Joy2Key makes this possible

        new_handlers = {
			 "^F":	self.exit_func,
			 "r":	self.launch_game,
        }

        self.add_handlers(new_handlers)

        y, x = self.useable_space()

        self.InstructText = self.add(InstructText, name="Instructions", value = "Use A/B to scroll, SELECT your game and press START to launch!", max_height=y // 8, editable=False)
        self.Browser = self.add(Browser, name="Available ROMs", editable=True, values=gameList, footer="ROMs LOADED!")

    def exit_func(self, _input):
        curses.beep()
        exit(0)

    def launch_game(self, _input):
    	
    	# Docs for npyscreen suck. This is the best I could do. You can probably do better.

    	# Convert returned list index value to its associated list value
    	# ie, convert "21" to the full $PATH for selected game of matching value "21"
    	indexedVal = [self.Browser.values[idx] for idx in self.Browser.value]
    	
    	# Convert resulting list value to a string that can be parsed by subprocess
    	selectedROM = ''.join(map(str, indexedVal))
    	#logger.debug('ROM selected: %s', selectedROM)
    	
    	# Very basic! Will tweak later.
    	# Simply opens the selected ROM via FCEUX
    	subprocess.Popen(["fceux", selectedROM])
    	
    	## TODO
    	# Clear/clean/redraw screen and allow re-entry when done with your ROM

	def quit_menu(self, _input):
		exit(0)

pyNES = App()
pyNES.run()