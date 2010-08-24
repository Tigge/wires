import pygame, pygame.gfxdraw, pygame.locals

from . import is_inside

class Widget:
    
    def __init__(self):
        self._enabled   = True
        self._position  = (0 , 0)
        self._dimension = (100, 100)
        self._parent    = None
        
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, (210, 210, 210))
        pygame.gfxdraw.rectangle(surface, rect, (60, 60, 60))
        
    def get_widget_at(self, point):
        if is_inside(self._position, self._dimension, point):
            return self
        else:
            return None

