from turtle import back
import pygame as game
from Paths import *
from button import *
from user import *
import sys
background = game.image.load(os.path.join(Path.quiz , 'background.png')).convert_alpha()
background = game.transform.scale(background , (State.currentWidth,State.currentHeight))


@staticmethod
def beforeQuizScreen():
    Screen.WIN.blit(background , (0,0))
    game.display.update()

class Game:
    
    def basicEvent():
     for event in picture.event.get():
            if event.type == picture.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == picture.MOUSEBUTTONDOWN: 
              State.mouseDown = True
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    Screen.quizMenu = False
                    Screen.idleMenu = True

    idle = True

    @staticmethod
    def updateQuiz():
        if Game.idle:
            beforeQuizScreen()