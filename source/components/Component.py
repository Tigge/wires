import Input
import Output

class Component:

    def __init__(self, inputs, outputs):
        self.inputs  = inputs
        self.outputs = outputs

    def update(self):
        return
        
    def calculate(self):
        return
    
    def ready(self):
        print "readycheck", self.__class__, self
        for inpt in self.inputs:
            print "  ", inpt
            if inpt not in Input.Input.readylist:
                print "     - not in"
                return False
        return True
    
    def getoutputs(self):
        return self.outputs
    
    def getinputs(self):
        return self.inputs
