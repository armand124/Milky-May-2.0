from pydoc import describe
import tkinter as tk
import pygame as game
import subprocess
from user import State
root = tk.Tk()

class Screen:
    windowedConstant = 80
    screenMenu = True
    settingsMenu = False
    askingMenu = False
    idleMenu = False
    quizMenu = False
    lessonMenu = False
    first_game = False 
    
    WIN = game.display.set_mode((State.currentWidth,State.currentHeight))

    if State.fullscreen:
        WIN = game.display.set_mode((State.currentWidth,State.currentHeight),game.FULLSCREEN)
    else:
        WIN = game.display.set_mode((State.currentWidth,State.currentHeight))

    def resizeMaterial_Width(desiredResolution,default1920Res):
        return (default1920Res * desiredResolution / 1920)
    
    def resizeMaterial_Height(desiredResolution,default1080Res):
        return (default1080Res * desiredResolution / 1080)

