import json
import os
from Paths import Path
class State:
    sessionStarted = True
    mouseDown = False
    collideWithObject = False
    f = open(os.path.join(Path.settings_Screen_Assets,'settings.json'),'r')
    fileReader = f.read()
    f.close()
    user = json.loads(fileReader)
    currentVolume = user["volume"]
    currentWidth = user["width"]
    currentHeight = user["height"]

def Save():
    f = open(os.path.join(Path.settings_Screen_Assets,'settings.json'),'w')
    settings = {
        "volume" : State.currentVolume,
        "height" : State.currentHeight,
        "width" : State.currentWidth
    }
    with f as outfile:
        json.dump(settings,outfile)
    f.close()
    