import json
import os
from Paths import Path
import pygame as picture

class State:
    sessionStarted = True
    mouseDown = False
    current_FPS = 0
    collideWithObject = False
    f = open(os.path.join(Path.settings_Screen_Assets,'settings.json'),'r')
    fileReader = f.read()
    f.close()
    user = json.loads(fileReader)
    currentVolume = user["volume"]
    currentWidth = user["width"]
    currentHeight = user["height"]
    __fullscreenStatus = user["Fullscreen"]
    fullscreen = False
    if __fullscreenStatus == 1:
        fullscreen = True
def Save():
    f = open(os.path.join(Path.settings_Screen_Assets,'settings.json'),'w')
    def savingFullscreen():
        if State.fullscreen == False:
            return 0
        else:
            return 1
    __fullscreenSavingPoint = savingFullscreen()
    settings = {
        "volume" : State.currentVolume,
        "height" : State.currentHeight,
        "width" : State.currentWidth,
        "Fullscreen" : __fullscreenSavingPoint
    }
    with f as outfile:
        json.dump(settings,outfile)
    f.close()


class Font:
 picture.init()
 __fontAcre = os.path.join(Path.fonts,'acre.otf')
 mainFont = picture.font.Font(__fontAcre, 100)
 