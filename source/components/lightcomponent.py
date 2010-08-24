import basecomponent
import wireio

"""
Light components
"""

class Light(basecomponent.Component):
    
    def __init__(self):
        basecomponent.Component.__init__(self, [wireio.WireInput(self)], [None])

    def calculate(self):
        pass
        
    def gotlight(self):
        pass

