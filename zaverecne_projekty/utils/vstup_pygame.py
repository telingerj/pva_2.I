import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

def vykresli():
    pygame.draw.rect(screen, (255, 0, 0), (200, 100, 100, 100))
    pygame.draw.rect(screen, (0, 255, 0), (400, 500, 150, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("klavesa down")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("klavesa up")


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                print(x, y)


    screen.fill((0, 0, 0))
    clock.tick(60)
    vykresli()
    pygame.display.flip()

pygame.quit()