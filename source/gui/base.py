import pygame, pygame.gfxdraw, pygame.locals
import event

def isInside(pos, dim, test):
    if test[0] >= pos[0] and test[0] <= pos[0] + dim[0] \
            and test[1] >= pos[1] and test[1] <= pos[1] + dim[1]:
        return True
    return False

class GUI:
    
    def __init__(self, base):
        self._base   = base
        self._active = None
        pass
    
    def setBase(self, base):
        self._base = base
    
    def update(self, ev):
        if self._base == None:
            return
        if ev.type == pygame.locals.MOUSEBUTTONDOWN:
            comp = self._base.getComponentAt(ev.pos)
            print comp
            if isinstance(comp, event.MouseListener):
                self._active = comp
                self._active.mousePressed(ev.pos)
        elif ev.type == pygame.locals.MOUSEBUTTONUP:
            if isinstance(self._active, event.MouseListener):
                self._active.mouseReleased(ev.pos)
                self._active.mouseClicked(ev.pos)
        elif ev.type == pygame.locals.MOUSEMOTION:
            pos  = ev.pos
            rel  = ev.rel
            bl, bm, br = ev.buttons
            if bl + bm + br > 0:
                if isinstance(self._active, event.MouseListener):
                    self._active.mouseMoved(pos, rel)
        elif isinstance(self._active, event.KeyListener):
            if ev.type == pygame.locals.KEYDOWN:
                self._active.keyPressed(ev.unicode)
            elif ev.type == pygame.locals.KEYUP:
                self._active.keyReleased(ev.key)
                self._active.keyTyped(ev.key)
            else:
                print ev 
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
        self._parent    = None
        
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, (210, 210, 210))
        pygame.gfxdraw.rectangle(surface, rect, (60, 60, 60))
        
    def getComponentAt(self, point):
        if isInside(self._position, self._dimension, point):
            return self
        else:
            return None

