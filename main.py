import pygame as game
from screen import Screen as screen
from menu import Menu
from user import *
import user
from idle import *
import sys
import gravityTest
from settings import Settings
game.init()

game.display.set_caption("Milky May")

@staticmethod
def main():
    clock = game.time.Clock()
    while State.sessionStarted:

      #Main Menu
      if screen.screenMenu is True:
        Menu.basicEvent()
        Menu.runMenuScreen()
      
      #Settings Menu
      if screen.settingsMenu is True:
        Settings.updateSettingScreen()
      
      #Gravity Game 
      if screen.idleMenu is True:
        #gravityTest.Player.player_Movement()
        gravityTest.basicEvent()
        gravityTest.updateGame()

      
      if State.mouseDown == True:
        State.mouseDown = False
      clock.tick(60) 
    game.quit()

main()
