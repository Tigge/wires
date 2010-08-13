


class Input:

    readylist = {}

    def __init__(self):
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
    
