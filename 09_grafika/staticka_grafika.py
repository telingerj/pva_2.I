import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

def draw_shapes():
    """
    pygame.draw.line(screen, (255, 0, 0), (200, 100), (300, 100), 5)
    pygame.draw.line(screen, (255, 0, 0), (300, 100), (300, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (300, 200), (200, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (200, 200), (200, 100), 5)
    pygame.draw.line(screen, (255, 0, 0), (200, 100), (300, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (200, 200), (300, 100), 5)
    pygame.draw.line(screen, (255, 0, 0), (200, 100), (250, 50), 5)
    pygame.draw.line(screen, (255, 0, 0), (250, 50), (300, 100), 5)
    """
    pygame.draw.rect(screen, (0, 255, 0), (200, 200, 150, 50), 1)
    pygame.draw.circle(screen, (0, 0, 255), (400, 400), 50, 5)
    pygame.draw.polygon(screen, (255, 0, 0),
        [(300, 100), (400, 50), (450, 150), (300, 200)])
    #TODO: nakreslit strom


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_shapes()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
