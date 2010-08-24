import pygame, pygame.gfxdraw
import components.baseio, components.basecomponent
import gui.widget, gui.event, gui.container

class ConnectionWidget(gui.widget.Widget, gui.event.MouseListener):
    def __init__(self, color):
        gui.widget.Widget.__init__(self)
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

class InputWidget(ConnectionWidget):
    def __init__(self, inpt):
        ConnectionWidget.__init__(self, (255, 0, 0))
        self._input     = inpt
    def wiredrop(self, comp):
        comp._output.connect(self._input)
    def wiredroplegal(self, comp):
        return isinstance(comp, OutputWidgetI)

class OutputWidget(ConnectionWidget):
    def __init__(self, outp):
        ConnectionWidget.__init__(self, (0, 255, 0))
        self._output = outp
    def wiredrop(self, comp):
        self._output.connect(comp._input)
    def wiredroplegal(self, comp):
        return isinstance(comp, InputWidget)
        
        #if self._connection:
        #    pygame.gfxdraw.line(surface, self._position[0], \
        #                        self._position[1], self._connectionpos[0], \
        #                        self._connectionpos[1], (255, 255, 255))
class ComponentWidget(gui.container.Container, gui.event.MouseListener):

    _mapping      = {}

    _color_base   = 66, 66, 66
    _color_frame  = 150, 150, 150

    def __init__(self, comp):
        gui.container.Container.__init__(self)
        #gui.event.MouseListener.__init__(self)
        self._component = comp
        self._dragging  = False        
        for inpt in comp.inputs:
            ComponentWidget._mapping[inpt] = self
            self.add(InputWidget(inpt))
        for outp in comp.outputs:
            self.add(OutputWidget(outp))

#    def add(self, widget):
#        if isinstance(widget,

    def guifor(self, component):
        for widget in self._widgets:
            res = widget.guifor(component)
            if res != None:
                return res
        return None

    def layout(self):
        inptcount = 0
        outpcount = 0
        x, y = self._position
        w, h = self._dimension
        for widget in self._widgets:
            if isinstance(widget, InputWidget):
                widget._position = (x + 5, y + 5 + inptcount * 15)
                inptcount += 1
            if isinstance(widget, OutputWidget):
                widget._position = (x + w - 15, y + 5 + outpcount * 15)
                outpcount += 1
    
    def paint(self, surface):
        rect = pygame.Rect(self._position, self._dimension)
        pygame.gfxdraw.box(surface, rect, ComponentWidget._color_base)
        pygame.gfxdraw.rectangle(surface, rect, ComponentWidget._color_frame)
        
        gui.container.Container.paint(self, surface)
        self.paintwires(surface)

    def get_widget_at(self, point):
        res = gui.container.Container.get_widget_at(self, point)
        if res == None:
            return gui.widget.Widget.get_widget_at(self, point)
        else:
          return res
    
    def paintwires(self, surface):
        for i, widget in enumerate(self._widgets):
            if isinstance(widget, OutputWidget):
                fx, fy = widget._position
                #for i, inpt in enumerate(outp._output._inputs):
                #    tx, ty = inpt._position
                #    pygame.gfxdraw.line(surface, fx, fy, tx, ty, (255, 255, 255))

    def mouse_moved(self, pos, rel):
        if self._dragging:
            self._position = (self._position[0] + rel[0], self._position[1] + rel[1])
            self.layout()
    def mouse_pressed(self, pos):
        self._dragging = True
    
    def mouse_released(self, pos):
        self._dragging = False

