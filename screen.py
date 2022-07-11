import tkinter as tk
import pygame as game
import subprocess
from user import State
root = tk.Tk()

class Screen:
    windowedConstant = 80
    screenMenu = True
    settingsMenu = False
    
    WIN = game.display.set_mode((State.currentWidth,State.currentHeight))
    if State.fullscreen:
        WIN = game.display.set_mode((State.currentWidth,State.currentHeight),game.FULLSCREEN)
    else:
        WIN = game.display.set_mode((State.currentWidth,State.currentHeight))

