#!/usr/bin/env python2.7
# encoding: utf-8

import sys, os, npyscreen, curses

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

        self.InstructText = self.add(InstructText, name="Instructions", value = "Use the NES controller's D-Pad to choose your game and press START to launch!", max_height=y // 9, editable=False)
        self.Browser = self.add(Browser, name="Available ROMs", editable=True)

    def exit_func(self, _input):
        exit(0)

pyNES = App()
pyNES.run()