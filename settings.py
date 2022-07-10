import pygame as picture
import os
from Paths import Path
from user import *
from screen import Screen
from button import MenuButtons

class Sound:
    volume_bar_unP = picture.image.load(os.path.join(Path.settings_Screen_Assets,'volumeSlideUnpressed.png')).convert_alpha()
    volume_bar_P = picture.image.load(os.path.join(Path.settings_Screen_Assets,'volumeSlidePressed.png')).convert_alpha()
    
    
    

class Settings:
    background = picture.image.load(os.path.join(Path.starting_Screen_Assets,'background.png')).convert_alpha()
    
    @staticmethod
    def updateSettingScreen():
        Screen.WIN.blit(Settings.background,(0,0))
        picture.display.update()
        
        