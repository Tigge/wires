import pygame, pygame.gfxdraw
import widget, event

class MovableWidget(widget.Widget, event.MouseListener, event.KeyListener):
    
    _color_normal = (255, 255, 255)
    _color_press  = (200, 255, 200)
    
    def __init__(self):
        widget.Widget.__init__(self)
        self._color = MovableWidget._color_normal
    
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, self._color)
        pygame.gfxdraw.rectangle(surface, rect, (60, 60, 60))
    
    def mouse_pressed(self, pos):
        self._color = MovableWidget._color_press
    
    def mouse_released(self, pos):
        self._color = MovableWidget._color_normal
    
    def mouse_moved(self, pos, rel):
        if self._color == MovableWidget._color_press:
            self._position = (self._position[0] + rel[0], self._position[1] + rel[1])


