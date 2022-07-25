from turtle import back
import pygame as game
from gui import GUI
from user import *
import random
from button import *
from screen import *
from Paths import Path
from user import *
from button import GravityGame_Buttons
import sys
from gui import *
#Game background
background = game.image.load(os.path.join(Path.gravity_game,'background.png')).convert_alpha()
background = game.transform.scale(background,(State.currentWidth,State.currentHeight))




#Planets Declarations
planets = []

#Earth
planet_earth = game.image.load(os.path.join(Path.gravity_game , 'earth.png')).convert_alpha()
info_earth = game.image.load(os.path.join(Path.gravity_game , 'infoEarth.png')).convert_alpha()
planet_earth = game.transform.scale(planet_earth , (Screen.resizeMaterial_Width(State.currentWidth,planet_earth.get_width()),Screen.resizeMaterial_Height(State.currentHeight,planet_earth.get_height())))
info_earth = game.transform.scale(info_earth , (Screen.resizeMaterial_Width(State.currentWidth,info_earth.get_width()),Screen.resizeMaterial_Height(State.currentHeight,info_earth.get_height())))
planets.append((planet_earth,info_earth))


#Jupiter
jupiter = game.image.load(os.path.join(Path.gravity_game , 'jupiter.png')).convert_alpha()
jupiter = game.transform.scale(jupiter , (Screen.resizeMaterial_Width(State.currentWidth,jupiter.get_width()),Screen.resizeMaterial_Height(State.currentHeight,jupiter.get_height())))
#info_jupiter = game.image.load(os.path.join(Path.gravity_game , 'infoJupiter.png')).convert_alpha()
#info_jupiter = game.transform.scale(info_jupiter , (Screen.resizeMaterial_Width(State.currentWidth,info_jupiter.get_width()),Screen.resizeMaterial_Height(State.currentHeight,info_jupiter.get_height())))
#planets.append((jupiter,info_jupiter))

#Mars
mars = game.image.load(os.path.join(Path.gravity_game , 'mars.png')).convert_alpha()
mars = game.transform.scale(mars , (Screen.resizeMaterial_Width(State.currentWidth,mars.get_width()),Screen.resizeMaterial_Height(State.currentHeight,mars.get_height())))
#info_mars = game.image.load(os.path.join(Path.gravity_game,'infoMars.png')).convert_alpha()
#info_mars = game.transform.scale(info_mars , (Screen.resizeMaterial_Width(State.currentWidth,info_mars.get_width()),Screen.resizeMaterial_Height(State.currentHeight,info_mars.get_height())))
#planets.append((mars , info_mars))

pausedScreen = game.image.load(os.path.join(Path.gravity_game , 'pauseScreen.png')).convert_alpha()
pausedSreen = game.transform.scale(pausedScreen,(State.currentWidth,State.currentHeight))

formuleList = game.image.load(os.path.join(Path.gravity_game))

class Player:
 #Default player position when game starts
 current_Y = State.currentHeight/2 
 current_X = State.currentWidth/2

 character = game.image.load(os.path.join(Path.gravity_game , 'ship.png')).convert_alpha()
 character = game.transform.scale(character,(Screen.resizeMaterial_Width(State.currentWidth,character.get_width()),Screen.resizeMaterial_Height(State.currentHeight,character.get_height())))
 
 left = game.image.load(os.path.join(Path.gravity_game , 'shipLeft.png')).convert_alpha()
 left = game.transform.scale(left , (Screen.resizeMaterial_Width(State.currentWidth , left .get_width()),Screen.resizeMaterial_Height(State.currentHeight,left.get_height())))
 
 leftUp = game.image.load(os.path.join(Path.gravity_game , 'shipLeftUp.png')).convert_alpha()
 leftUp = game.transform.scale(leftUp , (Screen.resizeMaterial_Width(State.currentWidth , left .get_width()),Screen.resizeMaterial_Height(State.currentHeight,left.get_height())))

 leftDown = game.image.load(os.path.join(Path.gravity_game , 'shipLeftDown.png')).convert_alpha()
 leftDown = game.transform.scale(leftDown , (Screen.resizeMaterial_Width(State.currentWidth , left .get_width()),Screen.resizeMaterial_Height(State.currentHeight,left.get_height())))

 right = game.image.load(os.path.join(Path.gravity_game , 'shipRight.png')).convert_alpha()
 right = game.transform.scale(right , (Screen.resizeMaterial_Width(State.currentWidth , left .get_width()),Screen.resizeMaterial_Height(State.currentHeight,left.get_height())))

 rightDown = game.image.load(os.path.join(Path.gravity_game , 'shipRightDown.png')).convert_alpha()
 rightDown = game.transform.scale(rightDown , (Screen.resizeMaterial_Width(State.currentWidth , left .get_width()),Screen.resizeMaterial_Height(State.currentHeight,left.get_height())))

 rightUp = game.image.load(os.path.join(Path.gravity_game , 'shipRightUp.png')).convert_alpha()
 rightUp = game.transform.scale(rightUp , (Screen.resizeMaterial_Width(State.currentWidth , left .get_width()),Screen.resizeMaterial_Height(State.currentHeight,left.get_height())))

 up = game.image.load(os.path.join(Path.gravity_game , 'shipUp.png')).convert_alpha()
 up = game.transform.scale(up , (Screen.resizeMaterial_Width(State.currentWidth , left .get_width()),Screen.resizeMaterial_Height(State.currentHeight,left.get_height())))

 down = game.image.load(os.path.join(Path.gravity_game , 'shipDown.png')).convert_alpha()
 down = game.transform.scale(down , (Screen.resizeMaterial_Width(State.currentWidth , left .get_width()),Screen.resizeMaterial_Height(State.currentHeight,left.get_height())))

 

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
       Player.character = Player.up
    if Player.down_key and Player.current_Y + Player.currentSpeed <= State.currentHeight-100:
       Player.current_Y += Player.currentSpeed
       Player.character = Player.down
    if Player.right_key and Player.current_X + Player.currentSpeed <= State.currentWidth-100:
       Player.current_X += Player.currentSpeed
       Player.character = Player.right
    if Player.left_key and Player.current_X - Player.currentSpeed >=0:
       Player.current_X -= Player.currentSpeed
       Player.character = Player.left
    if Player.up_key and Player.left_key:
       Player.character = Player.leftUp
    if Player.up_key and Player.right_key:
       Player.character = Player.rightUp
    if Player.down_key and Player.right_key:
       Player.character = Player.rightDown
    if Player.down_key and Player.left_key:
       Player.character = Player.leftDown
@staticmethod
def basicEvents():
   for event in game.event.get():
    if event.type == game.QUIT or State.sessionStarted == False:
                 sys.exit()
    if event.type == picture.MOUSEBUTTONDOWN: 
              State.mouseDown = True
    if event.type == game.KEYDOWN:
     if game.K_w == event.key or game.K_UP == event.key:
        Player.up_key = True
     if game.K_s == event.key or game.K_DOWN == event.key:
        Player.down_key = True
     if game.K_a == event.key or game.K_LEFT == event.key:
        Player.left_key = True
     if game.K_d == event.key or game.K_RIGHT == event.key:
        Player.right_key = True
     if game.K_ESCAPE == event.key and State.formulaScreen_Level_1 is False:
        State.pausedLevel_1 = not State.pausedLevel_1
     if game.K_ESCAPE == event.key and State.pausedLevel_1 is False and State.formulaScreen_Level_1 is True:
        State.formulaScreen_Level_1 = False
    if event.type == game.KEYUP:
     if game.K_w == event.key or game.K_UP == event.key:
        Player.up_key = False
     if game.K_s == event.key or game.K_DOWN == event.key:
        Player.down_key = False
     if game.K_a == event.key or game.K_LEFT == event.key:
        Player.left_key = False
     if game.K_d == event.key or game.K_RIGHT == event.key:
        Player.right_key = False
     

class World_Generation():
   positions = [(140,170),(600,650),(900,155)]
   random.shuffle(planets)
   random.shuffle(positions)
   
   def blitRandom():
      for i in range(0,1):
         imgPlanet , infoPlanet = planets[i]
         Screen.WIN.blit(imgPlanet, World_Generation.positions[i])
   
   def checkCollision():
      for i in range(0,1):
         x,y = World_Generation.positions[i]
         imgPlan , infoPlanet = planets[i]
         if Player.current_X >= x and Player.current_X <= x+planet_earth.get_width() and Player.current_Y >= y and Player.current_Y <= y+planet_earth.get_height():
            Screen.WIN.blit(infoPlanet , (x+planet_earth.get_width(),y))


#Function that updates the whole game     
def updateGame():
  Screen.WIN.blit(background,(0,0))
  if State.pausedLevel_1 is False and State.formulaScreen_Level_1 is False:
   Player.movePlayer()
  World_Generation.blitRandom()
  World_Generation.checkCollision()
  Screen.WIN.blit(Player.character,(Player.current_X,Player.current_Y))
  if State.pausedLevel_1:
     Screen.WIN.blit(pausedScreen,(0,0))
     GravityGame_Buttons.continueButton()
     GravityGame_Buttons.exitButton()
  if State.formulaScreen_Level_1 is True:
      Screen.WIN.blit(pausedScreen , (0,0))
  GravityGame_Buttons.formulaButton()
  game.display.update()
   