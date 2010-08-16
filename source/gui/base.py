import pygame, pygame.gfxdraw, pygame.locals


def isInside(pos, dim, test):
    if test[0] >= pos[0] and test[0] <= pos[0] + dim[0] \
            and test[1] >= pos[1] and test[1] <= pos[1] + dim[1]:
        return True
    return False

class GUI:
    
    def __init__(self, base):
        self._base = base
        pass
    
    def setBase(self, base):
        self._base = base
    
    def update(self, event):
        if self._base == None:
            return
        if event.type in [pygame.locals.MOUSEBUTTONDOWN, pygame.locals.MOUSEBUTTONUP]:
            pos  = event.pos
            but  = event.button
            comp = self._base.getComponentAt(pos)
            
            if isinstance(comp, MouseListener):
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    comp.mousePressed(pos)
                else:
                    comp.mouseReleased(pos)
                    comp.mouseClicked(pos)
            #print event.dict, pos, comp
        elif event.type == pygame.locals.MOUSEMOTION:
            pos  = event.pos
            rel  = event.rel
            buts = event.buttons
            comp = self._base.getComponentAt(pos)
            if isinstance(comp, MouseListener):
                comp.mouseMoved(pos, rel)
        else:
            #print event.type
            pass
    
    def paint(self, surface):
        self._base.paint(surface)
    

class Component:
    
    def __init__(self):
        self._enabled   = True
        self._position  = (0 , 0)
        self._dimension = (100, 100)
        
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, (210, 210, 210))
        pygame.gfxdraw.rectangle(surface, rect, (60, 60, 60))
        
    def getComponentAt(self, point):
        if isInside(self._position, self._dimension, point):
            return self
        else:
            return None

class Container(Component):

    def __init__(self):
        Component.__init__(self)
        
    def add(self, component):
        pass

class MouseListener:
    def mouseClicked(self, pos):
        pass
    def mousePressed(self, pos):
        pass
    def mouseReleased(self, pos):
        pass
    def mouseMoved(self, pos, rel):
        pass

class KeyListener:
    def keyPressed(self, pos):
        pass
    def keyReleased(self, pos):
        pass
    def keyTyped(self, pos):
        pass


class MovableComponent(Component, MouseListener):
    
    _color_normal = (255, 255, 255)
    _color_press  = (200, 255, 200)
    
    def __init__(self):
        Component.__init__(self)
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
