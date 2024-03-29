"""
Base IO module
"""

class Output:
    """
    Base output
    """
    def __init__(self, component):
        self._component = component
        self._inputs    = []
    
    def connect(self, inpt):
        if inpt not in self._inputs and inpt._output == None:
            self._inputs.append(inpt)
            inpt._output = self
            print "connected", self, "to", inpt
        else:
            raise Exception("Input " + str(inpt) + " already in use")
    
    def send(self, value):
        for i in self._inputs:
            i.recieve(value)
            


class Input:
    """
    Base input
    """
    readylist = {}

    def __init__(self, component):
        self._component = component
        self._output = None
        pass
        
    def recieve(self, value):
        if self not in Input.readylist:
            Input.readylist[self] = value
        else:
            raise Exception("Already recieved input")

    def value(self):
        if self in Input.readylist:
            return Input.readylist[self]
        else:
            return None
    
