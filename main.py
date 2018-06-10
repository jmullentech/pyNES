#!/usr/bin/env python2.7
# encoding: utf-8

import sys, os
import fnmatch
import npyscreen, curses

rompath = '/home/john/NES/ROMs'

gameList = []
for root, dirnames, filenames in os.walk(rompath):
    for filename in fnmatch.filter(filenames, '*.nes'):
        gameList.append(os.path.join(root, filename))

class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Welcome to pyNES v0.1a!")

class InstructText(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class Browser(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineAction

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        
        y, x = self.useable_space()

        self.InstructText = self.add(InstructText, name="Instructions", value = "Just select your game and press START to launch!", max_height=y // 8, editable=False)
        self.Browser = self.add(Browser, name="Available ROMs", editable=True)

    def exit_func(self, _input):
        curses.beep()
        exit(0)

pyNES = App()
pyNES.run()