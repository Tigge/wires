import Component
import WireInput
import WireOutput

class AndComponent(Component.Component):

    def __init__(self):
        Component.Component.__init__(self, \
        [WireInput.WireInput(), WireInput.WireInput()], \
        [WireOutput.WireOutput()])

    def calculate(self):
        i1 = self.inputs[0].value()
        i2 = self.inputs[1].value()
        self.outputs[0].send(i1 and i2)
