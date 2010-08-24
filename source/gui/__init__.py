import pygame, pygame.gfxdraw, pygame.locals

def is_inside(pos, dim, test):
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
            print self._base
            widget = self._base.get_widget_at(ev.pos)
            print widget
            if isinstance(widget, event.MouseListener):
                self._active = widget
                self._active.mouse_pressed(ev.pos)
        elif ev.type == pygame.locals.MOUSEBUTTONUP:
            if isinstance(self._active, event.MouseListener):
                self._active.mouse_released(ev.pos)
                self._active.mouse_clicked(ev.pos)
        elif ev.type == pygame.locals.MOUSEMOTION:
            pos  = ev.pos
            rel  = ev.rel
            bl, bm, br = ev.buttons
            if bl + bm + br > 0:
                if isinstance(self._active, event.MouseListener):
                    self._active.mouse_moved(pos, rel)
        elif isinstance(self._active, event.KeyListener):
            if ev.type == pygame.locals.KEYDOWN:
                self._active.key_pressed(ev.unicode)
            elif ev.type == pygame.locals.KEYUP:
                self._active.key_released(ev.key)
                self._active.key_typed(ev.key)
            else:
                print ev 
        else:
            #print event.type
            pass
    
    def paint(self, surface):
        self._base.paint(surface)
