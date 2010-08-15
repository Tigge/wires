import sys, pygame, pygame.gfxdraw

import components.logiccomponent
import components.lightcomponent
import gui.base
import gui.component
            

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

guicomps = [gui.component.ComponentGUI(s1), gui.component.ComponentGUI(s2), \
            gui.component.ComponentGUI(ac), gui.component.ComponentGUI(light)]


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

    
