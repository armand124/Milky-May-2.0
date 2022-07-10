import tkinter as tk
import pygame as game
import subprocess

root = tk.Tk()

class Screen:
    windowedConstant = 80

    
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    
    WIDTH = int(resolution[0].decode('UTF-8'))
    HEIGHT = int(resolution[1].decode('UTF-8'))

    screenMenu = True
    settingsMenu = False
    
    windowed_W = WIDTH - windowedConstant
    windowed_H = HEIGHT - windowedConstant
    WIN = game.display.set_mode((windowed_W,windowed_H),game.RESIZABLE)
    
    def appliedResolution(mode):
        if mode == "Windowed":
            resultingScreen = (Screen.windowed_W,Screen.windowed_H)
            return resultingScreen
        if mode == "FullScreen":
            resultingScreen = (Screen.Default_W,Screen.Default_H)
            return resultingScreen



