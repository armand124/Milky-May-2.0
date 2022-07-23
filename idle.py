import pygame as game
import os
from Paths import *
from screen import *
from user import *
class Idle:
    background = game.image.load(os.path.join(Path.starting_Screen_Assets,'background.png'))
    background = game.transform.scale(background,(State.currentWidth,State.currentHeight))    
    @staticmethod
    def idleScreen():
        Screen.WIN.blit(Idle.background,(0,0))
        game.display.update()