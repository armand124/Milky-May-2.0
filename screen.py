import tkinter as tk
import pygame as game
import subprocess
from user import State
root = tk.Tk()

class Screen:
    windowedConstant = 80
    screenMenu = True
    settingsMenu = False
    
    WIN = game.display.set_mode((State.currentWidth,State.currentHeight),game.RESIZABLE)

    def appliedResolution(mode):
        if mode == "Windowed":
            resultingScreen = (Screen.windowed_W,Screen.windowed_H)
            return resultingScreen
        if mode == "FullScreen":
            resultingScreen = (Screen.Default_W,Screen.Default_H)
            return resultingScreen



