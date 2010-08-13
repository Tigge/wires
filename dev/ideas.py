class Component:
    """
    Component class.
    """


    def __init__(self, i, o):
        self.inputs = i
        self.outputs = o
        

    def update(self):
        return
        
    def calculate(self):
        return
    
    
    def get_output_count(self):
        return len(self.outputs)
    
    def get_input_count(self):
        return len(self.inputs)
    
====================

class AndComponents(Component):

    def __init__(self):
        Component.__init__(self, [None, None], [[]])

    def calculate(self):
        ...
