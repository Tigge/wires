import pygame, pygame.gfxdraw
import components.baseio, components.basecomponent
import gui.base, gui.event, gui.container


class ConnectionGUI(gui.base.Component, gui.event.MouseListener):
    def __init__(self, color):
        gui.base.Component.__init__(self)
        self._dimension = (10, 10)
        self._mousedown = False
        self._color     = color
    
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, self._color)
        
        if self._mousedown:
            fx, fy = self._position
            tx, ty = self._wirepos
            pygame.gfxdraw.line(surface, fx, fy, tx, ty, (255, 255, 255))
    def wiredrop(self, comp):
        print "wiredrop", comp
        pass
    
    def wiredrag(self, pos):
        print "wiredrag", pos
        pass
    
    def wiredroplegal(self, comp):
        return True
    
    def mouseMoved(self, pos, rel):
        if self._mousedown:
            self._wirepos = pos
            self.wiredrag(pos)
    def mousePressed(self, pos):
        self._mousedown = True
        self._wirepos   = pos
    def mouseReleased(self, pos):
        self._mousedown = False
        comp = self._parent._parent.getComponentAt(pos)
        if self.wiredroplegal(comp):
            self.wiredrop(comp)

class InputGUI(ConnectionGUI):
    def __init__(self, inpt):
        ConnectionGUI.__init__(self, (255, 0, 0))
        self._input     = inpt
    def wiredrop(self, comp):
        comp._output.connect(self._input)
    def wiredroplegal(self, comp):
        return isinstance(comp, OutputGUI)

class OutputGUI(ConnectionGUI):
    def __init__(self, outp):
        ConnectionGUI.__init__(self, (0, 255, 0))
        self._output = outp
    def wiredrop(self, comp):
        self._output.connect(comp._input)
    def wiredroplegal(self, comp):
        return isinstance(comp, InputGUI)
        
        #if self._connection:
        #    pygame.gfxdraw.line(surface, self._position[0], \
        #                        self._position[1], self._connectionpos[0], \
        #                        self._connectionpos[1], (255, 255, 255))
class ComponentGUI(gui.container.Container, gui.event.MouseListener):

    _mapping      = {}

    _color_base   = 66, 66, 66
    _color_frame  = 150, 150, 150

    def __init__(self, comp):
        gui.container.Container.__init__(self)
        #gui.event.MouseListener.__init__(self)
        self._component = comp
        self._dragging  = False        
        for inpt in comp.inputs:
            ComponentGUI._mapping[inpt] = self
            self.add(InputGUI(inpt))
        for outp in comp.outputs:
            self.add(OutputGUI(outp))

    def layout(self):
        inptcount = 0
        outpcount = 0
        x, y = self._position
        w, h = self._dimension
        for comp in self._components:
            if isinstance(comp, InputGUI):
                comp._position = (x + 5, y + 5 + inptcount * 15)
                inptcount += 1
            if isinstance(comp, OutputGUI):
                comp._position = (x + w - 15, y + 5 + outpcount * 15)
                outpcount += 1
    
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, ComponentGUI._color_base)
        pygame.gfxdraw.rectangle(surface, rect, ComponentGUI._color_frame)
        
        gui.container.Container.paint(self, surface)
        self.paintwires(surface)

    def getComponentAt(self, point):
        res = gui.container.Container.getComponentAt(self, point)
        if res == None:
            return gui.base.Component.getComponentAt(self, point)
        else:
          return res
    
    def paintwires(self, surface):
        for i, outp in enumerate(self._component.outputs):
            if outp == None:
                return
            for i, inpt in enumerate(outp._inputs):
                if inpt in ComponentGUI._mapping:
                    other = ComponentGUI._mapping[inpt]
                    pygame.gfxdraw.line(surface, self._position[0] + self._dimension[0] - 15, self._position[1] + 5 + i * 15, \
                        other._position[0] + 5, other._position[1] + 5 + i * 15, (255, 255, 255))

    def mouseMoved(self, pos, rel):
        if self._dragging:
            self._position = (self._position[0] + rel[0], self._position[1] + rel[1])
            self.layout()
    def mousePressed(self, pos):
        self._dragging = True
    
    def mouseReleased(self, pos):
        self._dragging = False

