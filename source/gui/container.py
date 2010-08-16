import base

class Container(base.Component):

    def __init__(self):
        base.Component.__init__(self)
        self._components = []
        
    def add(self, comp):
        self._components.append(comp)
        
    def paint(self, surface):
        for comp in reversed(self._components):
            comp.paint(surface)
    
    def getComponentAt(self, point):
        for comp in self._components:
            res = comp.getComponentAt(point)
            if res != None:
                return res
        return None
