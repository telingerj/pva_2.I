import pygame
import random

pygame.init()
clock = pygame.time.Clock()

class AnimatedObject:
    def __init__(self, x, y, sizeX, sizeY, moveX, moveY, color):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.invertedX = 1
        self.invertedY = 1
        self.moveX = moveX
        self.moveY = moveY


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.sizeX, self.sizeY))
        self.bump(screen)

    def move(self):
        self.x += self.moveX * self.invertedX
        self.y += self.moveY * self.invertedY


    def bump(self, screen):
        if self.x >= screen.get_size()[0] - self.sizeX:
            self.invertedX *= -1
        elif self.x <= 0:
            self.invertedX *= -1

        if self.y >= screen.get_size()[1] - self.sizeY:
            self.invertedY *= -1
        elif self.y <= 0:
            self.invertedY *= -1



screen = pygame.display.set_mode((800, 800))


def vytvor_ctverce():
    ctverce = []
    for i in range(100):
        c = AnimatedObject(random.randint(0, 700),
                           random.randint(0, 700),
                           random.randint(0, 100),
                           random.randint(0, 100),
                           random.randint(-10, 10),
                           random.randint(-10, 10),
                            (random.randint(0, 255),
                             random.randint(0, 255),
                            random.randint(0, 255)))
        ctverce.append(c)
    return ctverce


running = True
ctverce = vytvor_ctverce()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    clock.tick(60)
    for c in ctverce:
        c.draw(screen)
        c.move()
    pygame.display.flip()

pygame.quit()
