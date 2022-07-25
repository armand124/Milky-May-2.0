import pygame as game
import os
from Paths import *
from screen import *
from user import *
from button import *
import sys
class Idle:
    background = game.image.load(os.path.join(Path.idle,'background.png')).convert_alpha()
    background = game.transform.scale(background,(State.currentWidth,State.currentHeight))
    game_icon_gravity = game.image.load(os.path.join(Path.idle , 'earth.png')).convert_alpha()
    game_icon_gravity = game.transform.scale(game_icon_gravity,(Screen.resizeMaterial_Width(State.currentWidth,game_icon_gravity.get_width()), Screen.resizeMaterial_Height(State.currentHeight,game_icon_gravity.get_height())))
    @staticmethod
    def basicEvent():
        for event in picture.event.get():
            if event.type == picture.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == picture.MOUSEBUTTONDOWN: 
              State.mouseDown = True
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    Screen.screenMenu = True
                    Screen.idleMenu = False

    @staticmethod
    def idleScreen():
        Screen.WIN.blit(Idle.background,(0,0))
        Idle_Buttons.gravityButton()
        Idle_Buttons.solarSystemButton()
        game.display.update()