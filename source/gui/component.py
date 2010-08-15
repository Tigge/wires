import pygame, pygame.gfxdraw
import base

class ComponentGUI:

    _color_base   = 66, 66, 66
    _color_frame  = 150, 150, 150
    _color_input  = 255, 0, 0
    _color_output = 0, 255, 0

    def __init__(self, comp):
        self._surface = pygame.Surface((64, 64))
        self._surface.fill(ComponentGUI._color_base)
        pygame.gfxdraw.rectangle(self._surface, \
            pygame.Rect((0, 0), (64, 64)), ComponentGUI._color_frame)
        for i, inpt in enumerate(comp.inputs):
            pygame.gfxdraw.box(self._surface, \
                pygame.Rect((5, 5 + i * 15), (10, 10)), \
                ComponentGUI._color_input)
        for i, outp in enumerate(comp.outputs):
            pygame.gfxdraw.box(self._surface, \
                pygame.Rect((49, 5 + i * 15), (10, 10)), \
                ComponentGUI._color_output)

