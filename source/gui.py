import sys, pygame
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Wirez")

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    pygame.display.flip()

