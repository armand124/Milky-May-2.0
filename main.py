import pygame as game
from screen import Screen as screen
from menu import Menu
from user import *
import user
from presentation import *
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
      
      #Idle Men8
      if screen.idleMenu is True:
        Idle.basicEvent()
        Idle.idleScreen()
      
      if screen.first_game is True:
        gravityTest.Player.modifyVelocity()
        gravityTest.basicEvents()
        gravityTest.updateGame()

      if screen.quizMenu is True:
        Game.basicEvent()
        Game.updateQuiz()

      if State.mouseDown == True:
        State.mouseDown = False
      clock.tick()
      State.current_FPS = clock.get_fps() 
    game.quit()

main()
 