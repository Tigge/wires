import pygame, pygame.gfxdraw

class Component:
    
    def __init__(self):
        self._enabled = True
        self._x       = 0
        self._y       = 0
        self._width   = 0
        self._height  = 0
        
    def draw(self, surface):
        pass
        

class MouseListener:
    def mouseClicked(self, pos):
        pass
    def mousePressed(self, pos):
        pass
    def mouseReleased(self, pos):
        pass


