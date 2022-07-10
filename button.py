import pygame as picture
from user import State
from screen import Screen
from Paths import Path
import os
class Button():
    def __init__(self , x , y , imagePressed,imageUnpressed):
        self.imagePressed = imagePressed
        self.imageUnpressed = imageUnpressed
        self.rect = self.imageUnpressed.get_rect()
        self.rect.topleft = (x,y)

    def buttonPressed(self):
       if State.mouseDown == True:
        if self.rect.collidepoint(picture.mouse.get_pos()):
                State.mouseDown = False
                return True
            
    def buttonOnCursor(self):
        if self.rect.collidepoint(picture.mouse.get_pos()):
                return True
    
    
    def showButton(self):
        if Button.buttonOnCursor(self):
         Screen.WIN.blit(self.imagePressed , (self.rect.x-5 , self.rect.y-5))
        elif Button.buttonPressed(self):
         Screen.WIN.blit(self.imagePressed,(self.rect.x,self.rect.y))
        else:
         Screen.WIN.blit(self.imageUnpressed,(self.rect.x,self.rect.y))
    

class MenuButtons:
    
    ButtonDifference_Y = 150
    
    #-----------------------------------------Quit Button Declaration-----------------------------------------
    quit_P = picture.image.load(os.path.join(Path.starting_Screen_Assets,'closePressed.png')).convert_alpha()
    quit_Un = picture.image.load(os.path.join(Path.starting_Screen_Assets,'closeUnpressed.png')).convert_alpha()
    
    __quitButton = Button(680,650,quit_P,quit_Un)
    
    @staticmethod
    def quitButton():
        if MenuButtons.__quitButton.buttonPressed():
            State.sessionStarted = False
        MenuButtons.__quitButton.showButton()
    
    #---------------------------------------------------------------------------------------------------------
    
    
    #-----------------------------------------Settings Button Declaration-----------------------------------------
    settings_P = picture.image.load(os.path.join(Path.starting_Screen_Assets,'settingsPressed.png')).convert_alpha()
    settings_Un = picture.image.load(os.path.join(Path.starting_Screen_Assets,'settingsUnpressed.png')).convert_alpha()
    
    __settingsButton = Button(680,650-ButtonDifference_Y,settings_P,settings_Un)
    
    @staticmethod
    def settingsButton():
        if MenuButtons.__settingsButton.buttonPressed():
            Screen.settingsMenu = True
            Screen.screenMenu = False
        MenuButtons.__settingsButton.showButton()
    
    #---------------------------------------------------------------------------------------------------------------
    
    
        
        
