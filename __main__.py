#!/usr/bin/env python
# encoding: utf-8

import npyscreen

from screens.MainScreen import MainScreen

class AudiofileTools(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.TransparentThemeLightText)
        self.addForm('MAIN', MainScreen, name='Audiofile Tools')

if __name__ == "__main__":
    app = AudiofileTools()
    app.run()
