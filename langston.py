import pygame
width, height = 800, 600
display = pygame.display.set_mode((width,height))
pygame.init()
qg = 4
x, y = 400, 300
display.fill((255,255,255))
directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
direction = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # update position
    dx, dy = directions[direction]
    x += dx * qg
    y += dy * qg

    try:
        a = display.get_at((x, y))
    except:
        break

    if a == (255, 255, 255, 255):
        # White square
        pygame.draw.rect(display,(255,0,0),(x,y,qg,qg)) # paint red
        direction = (direction + 1) % 4                 # turn left
    else:
        # Red square
        pygame.draw.rect(display,(255,255,255),(x,y,qg,qg)) # paint white
        direction = (direction - 1) % 4                     # turn right
    pygame.display.update()
print("end")
