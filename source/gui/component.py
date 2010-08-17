import pygame, pygame.gfxdraw
import base, event

class MovableComponent(base.Component, event.MouseListener):
    
    _color_normal = (255, 255, 255)
    _color_press  = (200, 255, 200)
    
    def __init__(self):
        base.Component.__init__(self)
        self._color = MovableComponent._color_normal
    
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, self._color)
        pygame.gfxdraw.rectangle(surface, rect, (60, 60, 60))
    
    def mousePressed(self, pos):
        self._color = MovableComponent._color_press
        
    def mouseReleased(self, pos):
        self._color = MovableComponent._color_normal
    def mouseMoved(self, pos, rel):
        if self._color == MovableComponent._color_press:
            self._position = (self._position[0] + rel[0], self._position[1] + rel[1])


class ComponentGUI(MovableComponent):

    _mapping      = {}

    _color_base   = 66, 66, 66
    _color_frame  = 150, 150, 150
    _color_input  = 255, 0, 0
    _color_output = 0, 255, 0

    def __init__(self, comp):
        MovableComponent.__init__(self)
        self._component = comp
        for inpt in comp.inputs:
            ComponentGUI._mapping[inpt] = self
        
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, ComponentGUI._color_base)
        pygame.gfxdraw.rectangle(surface, rect, ComponentGUI._color_frame)
        x, y = self._position
        w, h = self._dimension
        for i, inpt in enumerate(self._component.inputs):
            rect = pygame.Rect((x + 5, y + 5 + i * 15), (10, 10))
            pygame.gfxdraw.box(surface, rect, ComponentGUI._color_input)
        for i, outp in enumerate(self._component.outputs):
            rect = pygame.Rect((x + w - 15, y + 5 + i * 15), (10, 10))
            pygame.gfxdraw.box(surface, rect, ComponentGUI._color_output)
        self.paintwires(surface)
    
    def paintwires(self, surface):
        for i, outp in enumerate(self._component.outputs):
            if outp == None:
                return
            for inpt in outp._inputs:
                if inpt in ComponentGUI._mapping:
                    other = ComponentGUI._mapping[inpt]
                    pygame.gfxdraw.line(surface, self._position[0], self._position[1], \
                        other._position[0], other._position[1], (255, 255, 255))
                    
                    
                
