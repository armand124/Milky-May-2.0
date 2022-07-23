import pygame as game
from screen import Screen as screen
from menu import Menu
from user import *
import user
from idle import *
import sys
from settings import Settings
game.init()

game.display.set_caption("Milky May")

@staticmethod
def main():
    clock = game.time.Clock()
    while State.sessionStarted:
      for event in game.event.get():
            if event.type == game.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == game.KEYDOWN:
              if event.key == game.K_ESCAPE:
               if screen.settingsMenu is True:
                user.Save()
                screen.settingsMenu = False
                screen.screenMenu = True
            if event.type == game.MOUSEBUTTONDOWN: 
              State.mouseDown = True
      if screen.screenMenu is True:
        Menu.runMenuScreen()
      if screen.settingsMenu is True:
        Settings.updateSettingScreen()
      if screen.idleMenu is True:
        Idle.idleScreen()
      if State.mouseDown == True:
        State.mouseDown = False
      clock.tick(60) 
    game.quit()

main()
