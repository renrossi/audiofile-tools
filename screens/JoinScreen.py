#!/usr/bin/env python
# encoding: utf-8

import npyscreen

from .AppScreen import AppScreen

class JoinScreen(AppScreen):
    def create(self):
        self.add(npyscreen.ButtonPress, name='Join')
