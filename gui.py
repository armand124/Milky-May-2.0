import pygame as picture
from Paths import *
import os

class GUI:
 def arraging_text(max_width,surface, text, pos, font, color=picture.Color('black')):
    words = [word.split(' ') for word in text.splitlines()] 
    space = font.size(' ')[0]  
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0] 
                y += word_height 
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  
        y += word_height 
    
