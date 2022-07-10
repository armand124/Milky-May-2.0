import json
import os
from Paths import Path
class State:
    sessionStarted = True
    mouseDown = False
    collideWithObject = False
    f = open(os.path.join(Path.settings_Screen_Assets,'settings.json'),'r')
    volume = f.read()
    f.close()
    user = json.loads(volume)
    currentVolume = user["volume"]

def Save():
    f = open(os.path.join(Path.settings_Screen_Assets,'settings.json'),'w')
    settings = {
        "volume" : State.currentVolume
    }
    with f as outfile:
        json.dump(settings,outfile)
    f.close()
    