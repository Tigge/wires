import basecomponent
import wireio

"""
Logic components
"""

class Source(basecomponent.Component):
    """
    Source. Always gives away True or False. This should not need to be used
    in the game but is nice for debugging.
    """
    def __init__(self, sourceval):
        basecomponent.Component.__init__(self, inputs = [], outputs = [wireio.WireOutput()])
        self._value = sourceval

    def calculate(self):
        self.outputs[0].send(self._value)


class AndComponent(basecomponent.Component):
    """
    Logic AND. Outputs True on its single output if both of its inputs also
    are True, otherwise it outputs False.
    """
    def __init__(self):
        basecomponent.Component.__init__(self, \
        [wireio.WireInput(), wireio.WireInput()], \
        [wireio.WireOutput()])

    def calculate(self):
        i1 = self.inputs[0].value()
        i2 = self.inputs[1].value()
        self.outputs[0].send(i1 and i2)

