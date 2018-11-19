#!/usr/bin/env python
# encoding: utf-8

import npyscreen

class AppScreen(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)


