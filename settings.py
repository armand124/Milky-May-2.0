from tabnanny import check
import pygame as picture
import os
import sys
from pyparsing import White
from Paths import Path
from user import *
from gui import *
from screen import Screen
from button import *
class Sound:
    
    volume_bar_unP = picture.image.load(os.path.join(Path.settings_Screen_Assets,'volumeSlideUnpressed.png')).convert_alpha()
    volume_bar_P = picture.image.load(os.path.join(Path.settings_Screen_Assets,'volumeSlidePressed.png')).convert_alpha()
    buttonDifference = Screen.resizeMaterial_Height(State.currentHeight,30)
    slider_X_POS = State.currentWidth/2 - Screen.resizeMaterial_Width(State.currentWidth,178)
    slider_Y_POS = Screen.resizeMaterial_Height(State.currentHeight,290)
    volumeBar = []
    
    volume_icon_mute= picture.image.load(os.path.join(Path.settings_Screen_Assets,'volume-x.png')).convert_alpha()
    volume_icon_1= picture.image.load(os.path.join(Path.settings_Screen_Assets,'volume.png')).convert_alpha()
    volume_icon_2 = picture.image.load(os.path.join(Path.settings_Screen_Assets,'volume-1.png')).convert_alpha()
    volume_icon_3 = picture.image.load(os.path.join(Path.settings_Screen_Assets,'volume-2.png')).convert_alpha()
    
    volume_icon_mute = picture.transform.scale(volume_icon_mute,(Screen.resizeMaterial_Width(State.currentWidth,volume_icon_mute.get_width()),Screen.resizeMaterial_Height(State.currentHeight,volume_icon_mute.get_height())))
    volume_icon_1 = picture.transform.scale(volume_icon_1,(Screen.resizeMaterial_Width(State.currentWidth,volume_icon_1.get_width()),Screen.resizeMaterial_Height(State.currentHeight,volume_icon_1.get_height())))
    volume_icon_2 = picture.transform.scale(volume_icon_2,(Screen.resizeMaterial_Width(State.currentWidth,volume_icon_2.get_width()),Screen.resizeMaterial_Height(State.currentHeight,volume_icon_2.get_height())))
    volume_icon_3 = picture.transform.scale(volume_icon_3,(Screen.resizeMaterial_Width(State.currentWidth,volume_icon_3.get_width()),Screen.resizeMaterial_Height(State.currentHeight,volume_icon_3.get_height())))
    
    
    for i in range(0,10):
        button = SlideButton(slider_X_POS+i*buttonDifference,slider_Y_POS,volume_bar_P,volume_bar_unP,i)
        volumeBar.append(button)
        
    
    def handleVolumeIcon():
        if State.currentVolume==0:
            Screen.WIN.blit(Sound.volume_icon_mute,(Sound.slider_X_POS-Screen.resizeMaterial_Width(State.currentWidth,90),Sound.slider_Y_POS-Screen.resizeMaterial_Height(State.currentHeight,5)))
        elif State.currentVolume>=1 and State.currentVolume<=3:
            Screen.WIN.blit(Sound.volume_icon_1,(Sound.slider_X_POS-Screen.resizeMaterial_Width(State.currentWidth,90),Sound.slider_Y_POS-Screen.resizeMaterial_Height(State.currentHeight,5)))
        elif State.currentVolume>3 and State.currentVolume<=6:
            Screen.WIN.blit(Sound.volume_icon_2,(Sound.slider_X_POS-Screen.resizeMaterial_Width(State.currentWidth,90),Sound.slider_Y_POS-Screen.resizeMaterial_Height(State.currentHeight,5)))
        elif State.currentVolume>6:
            Screen.WIN.blit(Sound.volume_icon_3,(Sound.slider_X_POS-Screen.resizeMaterial_Width(State.currentWidth,90),Sound.slider_Y_POS-Screen.resizeMaterial_Height(State.currentHeight,5)))
            
    @staticmethod
    def handleVolume():
        for x in range(0,10):
            Sound.volumeBar[x].showButton()


class ScreenResolutionOptions:
    title = picture.image.load(os.path.join(Path.settings_Screen_Assets,'fullscreenText.png')).convert_alpha()
    check_square = picture.image.load(os.path.join(Path.settings_Screen_Assets,'check-square.png')).convert_alpha()
    square = picture.image.load(os.path.join(Path.settings_Screen_Assets,'square.png')).convert_alpha()
    

    title = picture.transform.scale(title,(Screen.resizeMaterial_Width(State.currentWidth,title.get_width()),Screen.resizeMaterial_Height(State.currentHeight,title.get_height())))
    
    X_POS = State.currentWidth/2 - Screen.resizeMaterial_Width(State.currentWidth,165)
    Y_POS = Screen.resizeMaterial_Height(State.currentHeight,440)
    
    __fullscreenButton = FullscreenButton(X_POS+Screen.resizeMaterial_Width(State.currentWidth,90),Y_POS+Screen.resizeMaterial_Height(State.currentHeight,80),check_square,square)
    @staticmethod
    def handleFullscreenButton():
        Screen.WIN.blit(ScreenResolutionOptions.title,(ScreenResolutionOptions.X_POS,ScreenResolutionOptions.Y_POS))
        ScreenResolutionOptions.__fullscreenButton.showButton()
        
    

class Settings:
    background = picture.image.load(os.path.join(Path.starting_Screen_Assets,'background.png')).convert_alpha()
    title = picture.image.load(os.path.join(Path.settings_Screen_Assets,'settingsText.png')).convert_alpha()
    background = picture.transform.scale(background, (State.currentWidth,State.currentHeight))
    title = picture.transform.scale(title,(Screen.resizeMaterial_Width(State.currentWidth,title.get_width()),Screen.resizeMaterial_Height(State.currentHeight,title.get_height())))
    
    
    @staticmethod
    def basicEvents():
        for event in picture.event.get():
            if event.type == picture.QUIT or State.sessionStarted == False:
                 sys.exit()
            keys = picture.key.get_pressed()
            if keys[picture.K_ESCAPE]:
                Screen.settingsMenu = False
                Screen.screenMenu = True
            if event.type == picture.MOUSEBUTTONDOWN: 
              State.mouseDown = True
    
    @staticmethod
    def updateSettingScreen():
        Screen.WIN.blit(Settings.background,(0,0))
        Screen.WIN.blit(Settings.title,(State.currentWidth/2 - Screen.resizeMaterial_Width(State.currentWidth,270), Screen.resizeMaterial_Height(State.currentHeight,40)))
        Sound.handleVolume() 
        ScreenResolutionOptions.handleFullscreenButton()
        Sound.handleVolumeIcon()
        picture.display.update()
        
        