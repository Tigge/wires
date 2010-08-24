import sys, pygame, pygame.gfxdraw, pygame.locals

import components.logiccomponent
import components.lightcomponent
import gui.widget, gui.movablewidget, gui.container, componentwidget
            

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Wirez")

screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)

background      = pygame.image.load("resources/background.png").convert()
sidepanel       = pygame.image.load("resources/sidepanel.png").convert()
left_fold_arrow = pygame.image.load("resources/left_fold_arrow.png").convert()
toppanel        = pygame.image.load("resources/toppanel.png").convert()

s1 = components.logiccomponent.Source(True)
s2 = components.logiccomponent.Source(True)

ac = components.logiccomponent.AndComponent()

light = components.lightcomponent.Light()

s1.outputs[0].connect(ac.inputs[0])
s2.outputs[0].connect(ac.inputs[1])
ac.outputs[0].connect(light.inputs[0])

comps = [s1, s2, ac, light]

guicomps = [componentwidget.ComponentWidget(s1), \
            componentwidget.ComponentWidget(s2), \
            componentwidget.ComponentWidget(ac), \
            componentwidget.ComponentWidget(light), \
            gui.movablewidget.MovableWidget()]


font = pygame.font.Font(pygame.font.get_default_font(), 16)
fps  = pygame.time.Clock()
container = gui.container.Container()
for gc in guicomps:
    container.add(gc)
gui  = gui.GUI(container)
while 1:
    fps.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        else: 
            #print event
            gui.update(event)
    #screen.fill(black)
    screen.blit(background, (0, 0))
    screen.blit(toppanel, (0,0))
    screen.blit(sidepanel, (575, 0))
    screen.blit(left_fold_arrow, (580, 250))

    
    fs = font.render("FPS: " + str(int(fps.get_fps())), True, (0, 0, 0))
    screen.blit(fs.convert_alpha(), (10, 10))

    for i, guicomp in enumerate(guicomps):
        guicomp.paint(screen)
    
    gui.paint(screen)
    
    pygame.display.update()

    
