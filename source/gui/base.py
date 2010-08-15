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
        if event.type in [pygame.locals.MOUSEBUTTONDOWN,
                pygame.locals.MOUSEBUTTONUP, pygame.locals.MOUSEMOTION]:
            pos  = event.pos
            comp = self._base.getComponentAt(pos)
            print event.dict, pos, comp
        print event.type
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
    def mouseMoved(self, pos):
        pass

class KeyListener:
    def keyPressed(self, pos):
        pass
    def keyReleased(self, pos):
        pass
    def keyTyped(self, pos):
        pass


class MovableComponent(Component, MouseListener):
    
    def __init__(self):
        Component.__init__(self)
        MouseListener.__init__(self)
        
    #def 
