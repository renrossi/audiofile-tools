#!/usr/bin/env python
# encoding: utf-8

import npyscreen

from .AppScreen import AppScreen

class MainScreen(AppScreen):
    def create(self):
        self.add(npyscreen.ButtonPress, name='test')
        self.add(npyscreen.ButtonPress)
        self.add(npyscreen.ButtonPress)
