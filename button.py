import pygame as picture
from user import *
from screen import Screen
from Paths import Path
import os
         
class Button():
    def __init__(self , x , y , imagePressed,imageUnpressed):
        self.imagePressed = picture.transform.scale(imagePressed,(Screen.resizeMaterial_Width(State.currentWidth,imagePressed.get_width()),Screen.resizeMaterial_Height(State.currentHeight,imagePressed.get_height())))
        self.imageUnpressed = picture.transform.scale(imageUnpressed,(Screen.resizeMaterial_Width(State.currentWidth,imageUnpressed.get_width()),Screen.resizeMaterial_Height(State.currentHeight,imageUnpressed.get_height())))
        self.rect = self.imageUnpressed.get_rect()
        self.rect.topleft = (x,y)
    def buttonPressed(self):
       if State.mouseDown == True:
        if self.rect.collidepoint(picture.mouse.get_pos()):
                State.mouseDown = False
                State.collideWithObject = True
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
    

class SlideButton():
    def __init__(self , x , y , imagePressed,imageUnpressed,volume):
        self.imagePressed = picture.transform.scale(imagePressed,(Screen.resizeMaterial_Width(State.currentWidth,imagePressed.get_width()),Screen.resizeMaterial_Height(State.currentHeight,imagePressed.get_height())))
        self.imageUnpressed = picture.transform.scale(imageUnpressed,(Screen.resizeMaterial_Width(State.currentWidth,imageUnpressed.get_width()),Screen.resizeMaterial_Height(State.currentHeight,imageUnpressed.get_height())))
        self.__volume = volume
        self.rect = self.imageUnpressed.get_rect()
        self.rect.topleft = (x,y)

    def buttonPressed(self):
       if State.mouseDown == True:
        if self.rect.collidepoint(picture.mouse.get_pos()):
                State.mouseDown = False
                State.collideWithObject = True
                return True
    
    def showButton(self):
        
        if Button.buttonPressed(self):
            State.currentVolume = self.__volume
        if (Button.buttonOnCursor(self) or State.currentVolume >= self.__volume) and self.__volume != 0:
         Screen.WIN.blit(self.imagePressed , (self.rect.x , self.rect.y))
        elif self.__volume !=0 and State.currentVolume < self.__volume:
         Screen.WIN.blit(self.imageUnpressed,(self.rect.x,self.rect.y))
 
class FullscreenButton():
   def __init__(self , x , y , imagePressed,imageUnpressed):
        self.imagePressed = picture.transform.scale(imagePressed,(Screen.resizeMaterial_Width(State.currentWidth,imagePressed.get_width()),Screen.resizeMaterial_Height(State.currentHeight,imagePressed.get_height())))
        self.imageUnpressed = picture.transform.scale(imageUnpressed,(Screen.resizeMaterial_Width(State.currentWidth,imageUnpressed.get_width()),Screen.resizeMaterial_Height(State.currentHeight,imageUnpressed.get_height())))
        self.rect = self.imageUnpressed.get_rect()
        self.rect.topleft = (x,y)

   def buttonPressed(self):
       if State.mouseDown == True:
        if self.rect.collidepoint(picture.mouse.get_pos()):
                State.mouseDown = False
                State.collideWithObject = True
                return True
    
   def showButton(self):    
        if Button.buttonPressed(self):
            State.fullscreen = not State.fullscreen
            picture.display.toggle_fullscreen()
            State.mouseDown = False
        if State.fullscreen is True:
         Screen.WIN.blit(self.imagePressed , (self.rect.x , self.rect.y))
        else:
         Screen.WIN.blit(self.imageUnpressed,(self.rect.x,self.rect.y))
 
class MenuButtons:
    
    ButtonDifference_Y = Screen.resizeMaterial_Height(State.currentHeight,150)
    ButtonConstant_X = State.currentWidth/2 - Screen.resizeMaterial_Width(State.currentWidth,120)
    
    
    #-----------------------------------------Quit Button Declaration-----------------------------------------

    quit_P = picture.image.load(os.path.join(Path.starting_Screen_Assets,'closePressed.png')).convert_alpha()
    quit_Un = picture.image.load(os.path.join(Path.starting_Screen_Assets,'closeUnpressed.png')).convert_alpha()
    __quitButton = Button(ButtonConstant_X,Screen.resizeMaterial_Height(State.currentHeight,780),quit_P,quit_Un)
    
    @staticmethod
    def quitButton():
        if MenuButtons.__quitButton.buttonPressed():
            State.sessionStarted = False
        MenuButtons.__quitButton.showButton()
    
    #---------------------------------------------------------------------------------------------------------
    
    
    #-----------------------------------------Settings Button Declaration-----------------------------------------

    settings_P = picture.image.load(os.path.join(Path.starting_Screen_Assets,'settingsPressed.png')).convert_alpha()
    settings_Un = picture.image.load(os.path.join(Path.starting_Screen_Assets,'settingsUnpressed.png')).convert_alpha()

    __settingsButton = Button(ButtonConstant_X,Screen.resizeMaterial_Height(State.currentHeight,780)-ButtonDifference_Y,settings_P,settings_Un)
    
    @staticmethod
    def settingsButton():
        if MenuButtons.__settingsButton.buttonPressed():
            Screen.settingsMenu = True
            Screen.screenMenu = False
        MenuButtons.__settingsButton.showButton()
    
    #---------------------------------------------------------------------------------------------------------------
    
    
    #-----------------------------------------New Game Button Declaration-----------------------------------------

    newGame_P = picture.image.load(os.path.join(Path.starting_Screen_Assets,'newGamePressed.png')).convert_alpha()
    newGame_Un = picture.image.load(os.path.join(Path.starting_Screen_Assets,'newGameUnpressed.png')).convert_alpha()

    __newGameButton = Button(ButtonConstant_X,Screen.resizeMaterial_Height(State.currentHeight,780)- 2*ButtonDifference_Y,newGame_P,newGame_Un)

    @staticmethod
    def newGameButton():
        if MenuButtons.__newGameButton.buttonPressed():
            Screen.screenMenu = False
            Screen.idleMenu = True
        MenuButtons.__newGameButton.showButton()

    #---------------------------------------------------------------------------------------------------------------            



class GravityGame_Buttons:
    
     ButtonDifference_Y = Screen.resizeMaterial_Height(State.currentHeight,150)
     ButtonConstant_X = State.currentWidth/2 - Screen.resizeMaterial_Width(State.currentWidth,120)
     
     #-----------------------------------------Continue Button Declaration-----------------------------------------
     
     continue_P = picture.image.load(os.path.join(Path.gravity_game,'continuePressed.png')).convert_alpha()
     continue_Un = picture.image.load(os.path.join(Path.gravity_game,'continueUnpressed.png')).convert_alpha()
     
     __continueButton = Button(ButtonConstant_X,Screen.resizeMaterial_Height(State.currentHeight,900)- 3*ButtonDifference_Y,continue_P,continue_Un)
     
     @staticmethod
     def continueButton():
        if GravityGame_Buttons.__continueButton.buttonPressed():
             State.pausedLevel_1 = False
        GravityGame_Buttons.__continueButton.showButton()
        
     #------------------------------------------------------------------------------------------------------------------
     
        
     #-----------------------------------------Exit Button Declaration-----------------------------------------
     exit_P = picture.image.load(os.path.join(Path.gravity_game,'backPressed.png')).convert_alpha()
     exit_Un = picture.image.load(os.path.join(Path.gravity_game,'backUnpressed.png')).convert_alpha()
     
     __exitButton = Button(ButtonConstant_X,Screen.resizeMaterial_Height(State.currentHeight,900)- 2*ButtonDifference_Y,exit_P,exit_Un)
     
     @staticmethod
     def exitButton():
        if GravityGame_Buttons.__exitButton.buttonPressed():
             Screen.idleMenu = True
             State.pausedLevel_1 = False
             Screen.first_game = False
        GravityGame_Buttons.__exitButton.showButton()

     #------------------------------------------------------------------------------------------------------------------


     #-----------------------------------------Formula Button Declaration-----------------------------------------
     
     formula_P = picture.image.load(os.path.join(Path.gravity_game , 'formule.png')).convert_alpha()
     formula_Un = picture.image.load(os.path.join(Path.gravity_game, 'formulePressed.png')).convert_alpha()

     __formulaButton = Button(Screen.resizeMaterial_Width(State.currentWidth,1760),Screen.resizeMaterial_Height(State.currentHeight,850),formula_Un,formula_P)
     @staticmethod
     def formulaButton():
        if GravityGame_Buttons.__formulaButton.buttonPressed():
            State.formulaScreen_Level_1 = not State.formulaScreen_Level_1
        GravityGame_Buttons.__formulaButton.showButton()

     #-------------------------------------------------------------------------------------------------------------



class Idle_Buttons:

    earth_icon_P = picture.image.load(os.path.join(Path.idle , 'earthPressed.png')).convert_alpha()
    earth_icon_Un = picture.image.load(os.path.join(Path.idle , 'earth.png')).convert_alpha()

    __earthIconButton = Button(Screen.resizeMaterial_Width(State.currentWidth,260),Screen.resizeMaterial_Height(State.currentHeight,450),earth_icon_P,earth_icon_Un)

    @staticmethod
    def gravityButton():
        if Idle_Buttons.__earthIconButton.buttonPressed():
            Screen.first_game = True
            Screen.idleMenu = False
        Idle_Buttons.__earthIconButton.showButton()

    
    solarSystem_P = picture.image.load(os.path.join(Path.quiz, 'solarSystemPressed.png')).convert_alpha()
    solarSystem_Un = picture.image.load(os.path.join(Path.quiz , 'solarSystem.png')).convert_alpha()

    __solarSystemIconButton = Button(Screen.resizeMaterial_Width(State.currentWidth,1250),Screen.resizeMaterial_Height(State.currentHeight,250),solarSystem_P,solarSystem_Un)

    @staticmethod
    def solarSystemButton():
        if Idle_Buttons.__solarSystemIconButton.buttonPressed():
            Screen.quizMenu = True
            Screen.idleMenu = False
        Idle_Buttons.__solarSystemIconButton.showButton()



class QuizButtons:

    lectie_P = picture.image.load(os.path.join(Path.quiz , 'lectiePressed.png')).convert_alpha()
    lectie_Un = picture.image.load(os.path.join(Path.quiz, 'lectieUnpressed.png')).convert_alpha()

    __lectieButton = Button(Screen.resizeMaterial_Width(State.currentWidth,500),Screen.resizeMaterial_Height(State.currentHeight,500),lectie_P,lectie_Un)

    @staticmethod
    def lessonButton():
        if QuizButtons.__lectieButton.buttonPressed():
            Screen.lessonMenu = True
            Screen.quizMenu = False
        QuizButtons.__lectieButton.showButton()

    
    quiz_P = picture.image.load(os.path.join(Path.quiz , 'evaluarePressed.png')).convert_alpha()
    quiz_Un = picture.image.load(os.path.join(Path.quiz, 'evaluareUnpressed.png')).convert_alpha()

    __quizButton= Button(Screen.resizeMaterial_Width(State.currentWidth,1120),Screen.resizeMaterial_Height(State.currentHeight,500),quiz_P,quiz_Un)

    @staticmethod
    def askingButton():
        if QuizButtons.__quizButton.buttonPressed():
            Screen.askingMenu = True
            Screen.quizMenu = False
        QuizButtons.__quizButton.showButton()

    finish_P = picture.image.load(os.path.join(Path.quiz , 'finalPressed.png')).convert_alpha()
    finish_Un = picture.image.load(os.path.join(Path.quiz , 'finalUnpressed.png')).convert_alpha()

    __finishButton= Button(Screen.resizeMaterial_Width(State.currentWidth,850),Screen.resizeMaterial_Height(State.currentHeight,700),finish_P,finish_Un)

    @staticmethod
    def finalButtonSlide():
        if QuizButtons.__finishButton.buttonPressed():
            Screen.lessonMenu = False
            Screen.quizMenu = True
        QuizButtons.__finishButton.showButton()


    @staticmethod
    def finalButtonSlideQuestions():
        if QuizButtons.__finishButton.buttonPressed():
            Screen.askingMenu = False
            Screen.quizMenu = True
        QuizButtons.__finishButton.showButton()

    
    truth_P = picture.image.load(os.path.join(Path.quiz , 'truePressed.png')).convert_alpha()
    truth_Un = picture.image.load(os.path.join(Path.quiz ,  'trueUnpressed.png')).convert_alpha()

    false_P = picture.image.load(os.path.join(Path.quiz , 'falsePressed.png')).convert_alpha()
    false_Un = picture.image.load(os.path.join(Path.quiz,'falseUnpressed.png')).convert_alpha()

    __truthButton = Button(Screen.resizeMaterial_Width(State.currentWidth,1020),Screen.resizeMaterial_Height(State.currentHeight,800),truth_P,truth_Un)
    __falseButton = Button(Screen.resizeMaterial_Width(State.currentWidth,600),Screen.resizeMaterial_Height(State.currentHeight,800),false_P,false_Un)

    @staticmethod
    def resultfromAnwear():
        if QuizButtons.__truthButton.buttonPressed():
            State.answearYet = True
            State.pressedDecision = True
        elif QuizButtons.__falseButton.buttonPressed():
            State.answearYet = False
            State.pressedDecision = True
        QuizButtons.__truthButton.showButton()
        QuizButtons.__falseButton.showButton()
        
