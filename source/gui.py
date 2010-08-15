import sys, pygame, pygame.gfxdraw

import components.logiccomponent
import components.lightcomponent

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
            

pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Wirez")

screen = pygame.display.set_mode(size)

s1 = components.logiccomponent.Source(True)
s2 = components.logiccomponent.Source(True)

ac = components.logiccomponent.AndComponent()

light = components.lightcomponent.Light()

s1.outputs[0].connect(ac.inputs[0])
s2.outputs[0].connect(ac.inputs[1])
ac.outputs[0].connect(light.inputs[0])

comps = [s1, s2, ac, light]

guicomps = [ComponentGUI(s1), ComponentGUI(s2), ComponentGUI(ac), ComponentGUI(light)]


font = pygame.font.Font(pygame.font.get_default_font(), 16)
fps  = pygame.time.Clock()
while 1:
    fps.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    fs = font.render("FPS: " + str(int(fps.get_fps())), True, (255, 255, 255))
    screen.blit(fs, (10, 10))

    for i, guicomp in enumerate(guicomps):
        screen.blit(guicomp._surface, (50 + 100 * i, 100))
    
    pygame.display.flip()

    
