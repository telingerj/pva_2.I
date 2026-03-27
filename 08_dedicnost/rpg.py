#  hra, ve které proti sobě bojují dvě armády
import pygame
import random

pygame.init()

class Armada:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva
        self.postavy = []


    def pridej_postavu(self, postava):
        self.postavy.append(postava)
        postava.pridej_armadu(self)


class Postava:
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost):
        self.jmeno = jmeno
        self.zdravi = zdravi
        self.rychlost = rychlost
        self.armada = None
        self.pozice = pozice
        self.textura_prava = textura_prava
        self.textura_leva = textura_leva


    def pridej_armadu(self, armada):
        self.armada = armada


    def uber_zdravi(self, zdravi):
        self.zdravi -= zdravi


class Bojovnik(Postava):
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni):
        super().__init__(jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost)
        self.poskozeni = poskozeni


    def utok(self, postava):
        pass


class Lukostrelec(Bojovnik):
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni, pocet_sipu, presnost):
        super().__init__(jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni)
        self.pocet_sipu = pocet_sipu
        self.presnost = presnost


    def utok(self, postava):
        if self.pocet_sipu <= 0:
            return
        self.pocet_sipu -= 1
        if random.randint(1, 100) <= self.presnost:
            postava.uber_zdravi(self.poskozeni)


class Sermir(Bojovnik):
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni, ucinnost_stitu):
        super().__init__(jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni)
        self.ucinnost_stitu = ucinnost_stitu


    def utok(self, postava):
        postava.uber_zdravi(self.poskozeni)


    def uber_zdravi(self, zdravi):
        if random.randint(1, 100) <= self.ucinnost_stitu:
            return
        self.zdravi -= zdravi


class Kouzelnik(Postava):
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, sila_magie, ucinnost_lecby):
        super().__init__(jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost)
        self.sila_magie = sila_magie
        self.ucinnost_lecby = ucinnost_lecby


    def lecba(self, postava):
        if random.randint(1, 100) > self.ucinnost_lecby:
            return
        postava.zdravi += self.sila_magie


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.clock.tick(60)
            pygame.display.flip()


game = Game()
game.loop()
