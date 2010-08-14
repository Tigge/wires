import baseio

"""
Wire IO module.
"""

class WireOutput(baseio.Output):
    """
    Wire output
    """
    def __init__(self):
        baseio.Output.__init__(self)


class WireInput(baseio.Input):
    """
    Wire input
    """
    def __init__(self):
        baseio.Input.__init__(self)

