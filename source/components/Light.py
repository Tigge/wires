
import Component
import WireInput

class Light(Component.Component):
    
    def __init__(self):
        Component.Component.__init__(self, [WireInput.WireInput()], [None])

    def calculate(self):
        pass
        
    def gotlight(self):
        pass
        
