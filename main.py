import pygame as game
from screen import Screen as screen
from menu import Menu
from user import State
import sys
from settings import Settings
game.init()

game.display.set_caption("Milky May 2")

@staticmethod
def main():
    while State.sessionStarted:
      for event in game.event.get():
            if event.type == game.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == game.KEYDOWN:
              if event.key == game.K_ESCAPE:
               if screen.settingsMenu is True:
                screen.settingsMenu = False
                screen.screenMenu = True
            if event.type == game.MOUSEBUTTONDOWN:
              State.mouseDown = True
            elif event.type != game.MOUSEBUTTONDOWN:
              State.mouseDown = False
      if screen.screenMenu is True:
        Menu.runMenuScreen()
      if screen.settingsMenu is True:
        Settings.updateSettingScreen()

    game.quit()

main()
