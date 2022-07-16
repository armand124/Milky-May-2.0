import pygame as picture
import os
from Paths import Path
from user import State
from screen import Screen
from button import MenuButtons
class Menu():
    background = picture.image.load(os.path.join(Path.starting_Screen_Assets,'background.png'))
    @staticmethod
    def runMenuScreen():
        Screen.WIN.blit(Menu.background,(0,0))
        MenuButtons.quitButton()
        Menu.background = picture.transform.scale(Menu.background,(State.currentWidth,State.currentHeight))
        MenuButtons.settingsButton()
        picture.display.update()
