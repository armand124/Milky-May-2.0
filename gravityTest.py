import pygame as game
from user import *

class Player:
 #Default player position when game starts
 current_Y = State.currentHeight/2 
 current_X = State.currentWidth/2

 #Function that helps with player movement
 @staticmethod
 def player_Movement(event):
    if event == game.K_UP:
        Player.current_Y += 1
    if event == game.K_DOWN:
        Player.current_Y -= 1
    if event == game.K_LEFT:
        Player.current_X -= 1
    if event == game.K_RIGHT:
        Player.current_X += 1
 
 character = game.image.load(os.path.join())
 def update_Player(event):
    Player.player_Movement(event)

    