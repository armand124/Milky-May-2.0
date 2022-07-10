import pygame as picture
import os
from Paths import Path
from user import *
from screen import Screen
from button import *
class Sound:
    volume_bar_unP = picture.image.load(os.path.join(Path.settings_Screen_Assets,'volumeSlideUnpressed.png')).convert_alpha()
    volume_bar_P = picture.image.load(os.path.join(Path.settings_Screen_Assets,'volumeSlidePressed.png')).convert_alpha()
    buttonDifference = 30
    volumeBar = []
    for i in range(0,10):
        button = SlideButton(500+i*buttonDifference,500,volume_bar_P,volume_bar_unP,i)
        volumeBar.append(button)
        
    @staticmethod
    def handleVolume():
        for x in range(0,10):
            Sound.volumeBar[x].showButton()

class Settings:
    background = picture.image.load(os.path.join(Path.starting_Screen_Assets,'background.png')).convert_alpha()
    
    @staticmethod
    def updateSettingScreen():
        Screen.WIN.blit(Settings.background,(0,0))
        Sound.handleVolume()
        picture.display.update()
        
        