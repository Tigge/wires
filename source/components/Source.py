import Component
import WireOutput

class Source(Component.Component):

    def __init__(self, sourceval):
        Component.Component.__init__(self, inputs = [], outputs = [WireOutput.WireOutput()])
        self._value = sourceval

    def calculate(self):
        self.outputs[0].send(self._value)
