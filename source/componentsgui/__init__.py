import pygame, pygame.gfxdraw, pygame.locals
import gui.container

__all__ = ["componentwidget"]

class ComponentGUI(gui.container.Container):
    
    def __init__(self, components):
        gui.container.Container.__init__(self)
        self._components = components
        
        for component in components:
            print component
            widget = componentwidget.ComponentWidget(component)
            self.add(widget)
            
    def paint(self, surface):
       for widget in reversed(self._widgets):
        
            widget.paint(surface)
            for widget2 in widget._widgets:

                if isinstance(widget2, componentwidget.OutputWidget):
                    if widget2._output != None:
                        fx, fy = widget2._position

                        for j, inpt in enumerate(widget2._output._inputs):
                            tx, ty = componentwidget.ComponentWidget._mapping[inpt]._position

                            xdiff = max((tx - fx) / 1.5, 50)
                            pygame.gfxdraw.bezier(surface, [(fx, fy), \
                                    (fx + xdiff, fy), (tx - xdiff, ty), \
                                    (tx, ty)], 3, (255, 255, 255))

