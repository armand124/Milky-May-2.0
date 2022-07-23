import pygame as game
from user import *
from screen import *
from Paths import Path
import sys
#Game background
background = game.image.load(os.path.join(Path.gravity_game,'background.png')).convert_alpha()
background = game.transform.scale(background,(State.currentWidth,State.currentHeight))

character = game.image.load(os.path.join(Path.gravity_game , 'ship.png')).convert_alpha()
character = game.transform.scale(character,(Screen.resizeMaterial_Width(State.currentWidth,character.get_width()),
Screen.resizeMaterial_Height(State.currentHeight,character.get_height())))

class Player:
 #Default player position when game starts
 current_Y = State.currentHeight/2 
 current_X = State.currentWidth/2

 #Function that helps with player movement
 @staticmethod
 def player_Movement():
   for event in game.event.get():
    if event .type== game.KEYDOWN:
     if event.key == game.K_UP or event.key == game.K_w:
        Player.current_Y += 1
     if event.key == game.K_DOWN or event.key == game.K_s:
        Player.current_Y -= 1
     if event.key == game.K_LEFT or event.key == game.K_a:
        Player.current_X -= 1
     if event.key == game.K_RIGHT or event.key == game.K_d:
        Player.current_X += 1

#Function that implements basic screen events
def basicEvent():
    for event in game.event.get():
            if event.type == game.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == game.MOUSEBUTTONDOWN: 
              State.mouseDown = True

#Function that updates the whole game     
def updateGame():
  Screen.WIN.blit(background,(0,0))
  Screen.WIN.blit(character,(Player.current_X,Player.current_Y))
  game.display.update()
   