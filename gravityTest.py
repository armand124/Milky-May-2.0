from turtle import back
import pygame as game
from gui import GUI
from user import *
from screen import *
from Paths import Path
import sys
from gui import *
#Game background
background = game.image.load(os.path.join(Path.gravity_game,'background.png')).convert_alpha()
background = game.transform.scale(background,(State.currentWidth,State.currentHeight))

character = game.image.load(os.path.join(Path.gravity_game , 'ship.png')).convert_alpha()
character = game.transform.scale(character,(Screen.resizeMaterial_Width(State.currentWidth,character.get_width()),Screen.resizeMaterial_Height(State.currentHeight,character.get_height())))

class Player:
 #Default player position when game starts
 current_Y = State.currentHeight/2 
 current_X = State.currentWidth/2

 up_key = False
 down_key = False
 right_key = False
 left_key = False
 movementConstant = 10
 currentSpeed = 1
 

 #Updating velocity depending of the current fps
 @staticmethod
 def modifyVelocity():
     Player.currentSpeed = (60/State.current_FPS) * Player.movementConstant

 @staticmethod
 def movePlayer():
    if Player.up_key and Player.current_Y - Player.currentSpeed >= 0:
       Player.current_Y -= Player.currentSpeed
    if Player.down_key and Player.current_Y + Player.currentSpeed <= State.currentHeight:
       Player.current_Y += Player.currentSpeed
    if Player.right_key and Player.current_X + Player.currentSpeed <= State.currentWidth:
       Player.current_X += Player.currentSpeed
    if Player.left_key and Player.current_X - Player.currentSpeed >=0:
       Player.current_X -= Player.currentSpeed
@staticmethod
def basicEvents():
   for event in game.event.get():
    if event.type == game.QUIT or State.sessionStarted == False:
                 sys.exit()
    if event.type == game.KEYDOWN:
     if game.K_w == event.key or game.K_UP == event.key:
        Player.up_key = True
     if game.K_s == event.key or game.K_DOWN == event.key:
        Player.down_key = True
     if game.K_a == event.key or game.K_LEFT == event.key:
        Player.left_key = True
     if game.K_d == event.key or game.K_RIGHT == event.key:
        Player.right_key = True
        
    if event.type == game.KEYUP:
     if game.K_w == event.key or game.K_UP == event.key:
        Player.up_key = False
     if game.K_s == event.key or game.K_DOWN == event.key:
        Player.down_key = False
     if game.K_a == event.key or game.K_LEFT == event.key:
        Player.left_key = False
     if game.K_d == event.key or game.K_RIGHT == event.key:
        Player.right_key = False

#Function that updates the whole game     
def updateGame():
  Screen.WIN.blit(background,(0,0))
  Player.movePlayer()
  Screen.WIN.blit(character,(Player.current_X,Player.current_Y))
  game.display.update()
   