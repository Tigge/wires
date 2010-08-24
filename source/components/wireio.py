import baseio

"""
Wire IO module.
"""

class WireOutput(baseio.Output):
    """
    Wire output
    """
    def __init__(self, component):
        baseio.Output.__init__(self, component)


class WireInput(baseio.Input):
    """
    Wire input
    """
    def __init__(self, component):
        baseio.Input.__init__(self, component)

