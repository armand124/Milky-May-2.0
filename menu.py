from tkinter import Menubutton
import pygame as picture
import os
from Paths import Path
from user import State
from screen import Screen
import sys
from button import MenuButtons
class Menu():
    background = picture.image.load(os.path.join(Path.starting_Screen_Assets,'background.png')).convert_alpha()
    logo = picture.image.load(os.path.join(Path.starting_Screen_Assets , 'Logo.png')).convert_alpha()
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
        Screen.WIN.blit(Menu.logo , (State.currentWidth/2 - Screen.resizeMaterial_Width(State.currentWidth , 270), Screen.resizeMaterial_Height(State.currentHeight,40)))
        MenuButtons.settingsButton()
        picture.display.update()
