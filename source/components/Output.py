

class Output:
    def __init__(self):
        self._inputs = []
    
    def connect(self, inpt):
        if inpt not in self._inputs:
            self._inputs.append(inpt)
            print "connected", self, "to", inpt
        else:
            raise Exception("Input " + str(inpt) + " already in use")
    
    def send(self, value):
        for i in self._inputs:
            i.recieve(value)
