from turtle import back
import pygame as game
from Paths import *
from button import *
import gui
from user import *
import sys
background = game.image.load(os.path.join(Path.quiz , 'background.png')).convert_alpha()
background = game.transform.scale(background , (State.currentWidth,State.currentHeight))


background_2 = game.image.load(os.path.join(Path.quiz , 'backgroundSecond.png')).convert_alpha()
background_2 = game.transform.scale(background_2 , (State.currentWidth,State.currentHeight))

backgroundText = game.image.load(os.path.join(Path.quiz , 'backgroundText.png')).convert_alpha()

facts = ['aoidjaojfoiawaaiogjaoighawuoifawuoifqwuoiahfioqwufjoiqwufjoaisgagoiaugaijgaioeugoatoaieutatiawaaiogjaoighawuoifawuoifqwuoiahfioqwuiawaaiogjaoighawuoifawuoifqwuoiahfioqwuiawaaiogjaoighawuoifawuoifqwuoiahfioqwu','oiajw','aifhoahoifafj']
questions = []
questionsMode = []

class Game:
    
    def basicEvent():
     for event in picture.event.get():
            if event.type == picture.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == picture.MOUSEBUTTONDOWN: 
              State.mouseDown = True
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    Screen.quizMenu = False
                    Screen.idleMenu = True



    @staticmethod
    def beforeQuizScreen():
        Screen.WIN.blit(background , (0,0))
        QuizButtons.lessonButton()
        QuizButtons.askingButton()
        picture.display.update()


class LessonGame:
    currentSlide = 0
    def basicEvent():
     for event in picture.event.get():
            if event.type == picture.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == picture.MOUSEBUTTONDOWN: 
              State.mouseDown = True
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    Screen.lessonMenu = False
                    Screen.quizMenu = True
                if event.key == game.K_RIGHT:
                    LessonGame.currentSlide +=1
                if event.key == game.K_LEFT and LessonGame.currentSlide > 0:
                    LessonGame.currentSlide -=1

    @staticmethod
    def run():
        Screen.WIN.blit(background_2,(0,0))
        maxSlide = len(facts)
        if LessonGame.currentSlide == maxSlide:
            QuizButtons.finalButtonSlide()
        else:
            Screen.WIN.blit(backgroundText,(0,0))
            gui.GUI.arraging_text(600,Screen.WIN,facts[LessonGame.currentSlide],(20,20),Font.mainFont)
        picture.display.update()

class QuizGame:
    def basicEvent():
     for event in picture.event.get():
            if event.type == picture.QUIT or State.sessionStarted == False:
                 sys.exit()
            if event.type == picture.MOUSEBUTTONDOWN: 
              State.mouseDown = True
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    Screen.askingMenu = False
                    Screen.quizMenu = True

    


