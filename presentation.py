from turtle import back
import pygame as game
from Paths import *
import random
from button import *
import gui
from user import State
from user import Font as fnt
import sys
background = game.image.load(os.path.join(Path.quiz , 'background.png')).convert_alpha()
background = game.transform.scale(background , (State.currentWidth,State.currentHeight))


background_2 = game.image.load(os.path.join(Path.quiz , 'backgroundSecond.png')).convert_alpha()
background_2 = game.transform.scale(background_2 , (State.currentWidth,State.currentHeight))

backgroundText = game.image.load(os.path.join(Path.quiz , 'backgroundText.png')).convert_alpha()

facts = ['Universul este totalitatea spațiului și timpului, a tuturor formelor de materie și energie.' , 'Dimensiunea întregului Univers nu este cunoscută.', 'Universul observabil poate fi măsurat și este estimat în prezent la 93 miliarde de ani-lumină în diametru.' , 'Numărul de galaxii estimat este de 2 trilioane' , 'Calea Lactee este galaxia din care face parte sistemul solar ' , 'În sistemul solar se află 8 planete : Mercur, Venus, Pământ, Marte, Jupiter, Saturn, Uranus și Neptun' , 'Între Marte și Jupiter se află Centura de asteroizi' , 'Pământul s-a format acum 4,54 miliarde de ani' ,' Pământul este a 3-a planetă față de Soare, dar este a 4-a cea mai mică planetă ca și mărime sau diametru' , 'Calea Lactee are formă de disc' , 'Calea Lactee are un diametru de 150000-200000 de ani lumină' , 'Galaxia Andromeda este cea mai apropiată galaxie de Calea Lactee']
questions = [('Este cunoscută dimensiunea întregului Univers.',False),('Dimaetrul universului este de 93 de miliarde de ani-lumină.',True),
('Numărul estimat de galaxii este de 10 trilioane.',False),('În prezent, în sistemul nostru solar există 8 planete.',True),
('Între Marte și Jupiter se află Centura de Asteroizi',True),('Cele mai mari planete sunt Uranus și Jupiter.',False),
('Pământul este a 3-a cea mai mică planetă.',False),('Pământul face o rotație completă în jurul soarelui în 365,25 de zile.',True),
('Pământul a fost format acum 2 miliarde de ani.',False),('Galaxia Andromeda este cea mai apropiată de Calea Lactee.',True)]

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
            gui.GUI.arraging_text(Screen.WIN,facts[LessonGame.currentSlide],(30,30),fnt.mainFont)
        picture.display.update()

class QuizGame:
    currentSlide = 0
    score = 0
    scoreText = picture.image.load(os.path.join(Path.quiz , 'scor.png')).convert_alpha()
    scoreText = picture.transform.scale(scoreText , (Screen.resizeMaterial_Width(State.currentWidth,scoreText.get_width()),Screen.resizeMaterial_Height(State.currentHeight,scoreText.get_height())))
    backgroundScore = picture.image.load(os.path.join(Path.quiz , 'backgroundScore.png')).convert_alpha()
    backgroundScore = picture.transform.scale(backgroundScore , (Screen.resizeMaterial_Width(State.currentWidth,backgroundScore.get_width()),Screen.resizeMaterial_Height(State.currentHeight,backgroundScore.get_height())))
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
    random.shuffle(questions)    
    def run():
        Screen.WIN.blit(background_2,(0,0))
        if QuizGame.currentSlide == 10:
            QuizButtons.finalButtonSlideQuestions()
            Screen.WIN.blit(QuizGame.backgroundScore,(Screen.resizeMaterial_Width(State.currentWidth,910),Screen.resizeMaterial_Height(State.currentHeight,430)))
            gui.GUI.arraging_text(Screen.WIN,str(QuizGame.score),(Screen.resizeMaterial_Width(State.currentWidth,934),Screen.resizeMaterial_Height(State.currentHeight,445),Font.scoreFont))
            Screen.WIN.blit(QuizGame.scoreText,(Screen.resizeMaterial_Width(State.currentWidth,810),Screen.resizeMaterial_Height(State.currentHeight,325)))
        else:
            Screen.WIN.blit(backgroundText,(0,0))
            askedQuestion , answear = questions[QuizGame.currentSlide]
            gui.GUI.arraging_text(Screen.WIN,askedQuestion,(20,20),Font.mainFont)
            if State.pressedDecision:
                if State.answearYet == answear:
                    QuizGame.score+=1
                State.pressedDecision = False
                QuizGame.currentSlide+=1
            QuizButtons.resultfromAnwear()
        picture.display.update()
            


        
