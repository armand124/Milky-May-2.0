from tkinter import Menubutton
import pygame as picture
import os
from Paths import Path
from user import State
from screen import Screen
import sys
from button import MenuButtons
class Menu():
    background = picture.image.load(os.path.join(Path.starting_Screen_Assets,'background.png'))
    def basicEvent():
        for event in picture.event.get():
            if event.type == picture.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == picture.MOUSEBUTTONDOWN: 
              State.mouseDown = True
    @staticmethod
    def runMenuScreen():
        Screen.WIN.blit(Menu.background,(0,0))
        MenuButtons.quitButton()
        MenuButtons.newGameButton()
        Menu.background = picture.transform.scale(Menu.background,(State.currentWidth,State.currentHeight))
        MenuButtons.settingsButton()
        picture.display.update()
