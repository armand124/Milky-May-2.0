import tkinter as tk
import pygame as game
root = tk.Tk()

class Screen:
    windowedConstant = 80
    Default_W = root.winfo_screenmmwidth()
    Default_H = root.winfo_screenmmheight()

    screenMenu = True
    settingsMenu = False
    
    windowed_W = Default_W - windowedConstant
    windowed_H = Default_H - windowedConstant
    WIN = game.display.set_mode((1600,900),game.RESIZABLE)
    
    def appliedResolution(mode):
        if mode == "Windowed":
            resultingScreen = (Screen.windowed_W,Screen.windowed_H)
            return resultingScreen
        if mode == "FullScreen":
            resultingScreen = (Screen.Default_W,Screen.Default_H)
            return resultingScreen



