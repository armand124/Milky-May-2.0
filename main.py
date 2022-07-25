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
        Settings.basicEvents()
        Settings.updateSettingScreen()
      
      #Gravity Game 
      if screen.idleMenu is True:
        gravityTest.Player.modifyVelocity()
        gravityTest.basicEvents()
        gravityTest.updateGame()

      if State.mouseDown == True:
        State.mouseDown = False
      clock.tick()
      State.current_FPS = clock.get_fps() 
    game.quit()

main()
 