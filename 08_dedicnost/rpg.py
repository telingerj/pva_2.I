#  hra, ve které proti sobě bojují dvě armády
import pygame
import random

pygame.init()
pygame.font.init()

class Armada:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva
        self.postavy = []


    def pridej_postavu(self, postava):
        self.postavy.append(postava)
        postava.pridej_armadu(self)


class Postava:
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, font):
        self.jmeno = jmeno
        self.zdravi = zdravi
        self.max_zdravi = zdravi
        self.rychlost = rychlost
        self.armada = None
        self.pozice = pozice
        self.textura_prava = textura_prava
        self.textura_leva = textura_leva
        self.otoceni = True  # výchozí hodnota - otočení doprava
        self.font = font
        self.textura_jmeno = None



    def pridej_armadu(self, armada):
        self.armada = armada
        self.textura_jmeno = self.font.render(self.jmeno, False, self.armada.barva)


    def uber_zdravi(self, zdravi):
        self.zdravi -= zdravi


    def vykresli(self, screen):
        if self.otoceni:
            screen.blit(self.textura_prava, self.pozice)
        else:
            screen.blit(self.textura_leva, self.pozice)

        pomer_zdravi = self.zdravi / self.max_zdravi

        pygame.draw.rect(
            screen, (150, 150, 150), (self.pozice[0] - 5, self.pozice[1] - 15, 35, 5))
        pygame.draw.rect(
            screen, self.armada.barva, (self.pozice[0] - 5, self.pozice[1] - 15, pomer_zdravi * 35, 5))

        x = self.pozice[0] + 12 - self.textura_jmeno.get_width() / 2
        screen.blit(self.textura_jmeno, (x, self.pozice[1] - 35))


    def pohyb(self):
        posun = self.rychlost / 100
        if self.otoceni:
            self.pozice = (self.pozice[0] + posun, self.pozice[1])
        else:
            self.pozice = (self.pozice[0] - posun, self.pozice[1])

        #TODO: na konci okna se postava otočí a jde zpátky





class Bojovnik(Postava):
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni, font):
        super().__init__(jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, font)
        self.poskozeni = poskozeni


    def utok(self, postava):
        pass


class Lukostrelec(Bojovnik):
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni, pocet_sipu, presnost, font):
        super().__init__(jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni, font)
        self.pocet_sipu = pocet_sipu
        self.presnost = presnost


    def utok(self, postava):
        if self.pocet_sipu <= 0:
            return
        self.pocet_sipu -= 1
        if random.randint(1, 100) <= self.presnost:
            postava.uber_zdravi(self.poskozeni)


class Sermir(Bojovnik):
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni, ucinnost_stitu, font):
        super().__init__(jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, poskozeni, font)
        self.ucinnost_stitu = ucinnost_stitu


    def utok(self, postava):
        postava.uber_zdravi(self.poskozeni)


    def uber_zdravi(self, zdravi):
        if random.randint(1, 100) <= self.ucinnost_stitu:
            return
        self.zdravi -= zdravi


class Kouzelnik(Postava):
    def __init__(self, jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, sila_magie, ucinnost_lecby, font):
        super().__init__(jmeno, zdravi, pozice, textura_prava, textura_leva, rychlost, font)
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
        self.font = pygame.font.SysFont("Calibri", 20)
        self.textury = self.nacti_textury()
        self.vytvor_armady()


    def nacti_textury(self):
        #pygame.image.load("images/archer_left.png")
        textury = []
        for postava in ["archer", "magician", "swordsman"]:
            for otoceni in ["left", "right"]:
                t = pygame.image.load("images/" + postava + "_" + otoceni + ".png")
                textury.append(t)

        return textury


    def vytvor_armady(self):
        self.a1 = Armada("hodni", (0, 0, 255))
        self.a2 = Armada("zli", (255, 0, 0))

        s1 = Sermir("Pepa", 100, (100, 100), self.textury[5], self.textury[4], 100, 10, 10, self.font)
        l1 = Lukostrelec("Franta", 80, (100, 250), self.textury[1], self.textury[0], 100, 15, 10, 90, self.font)
        k1 = Kouzelnik("David", 80, (120, 350), self.textury[3], self.textury[2], 100, 10, 90, self.font)

        s2 = Sermir("Honza", 100, (600, 100), self.textury[5], self.textury[4], 100, 10, 10, self.font)
        l2 = Lukostrelec("Kuba", 80, (600, 250), self.textury[1], self.textury[0], 100, 15, 10, 90, self.font)
        k2 = Kouzelnik("Martin", 80, (580, 350), self.textury[3], self.textury[2], 100, 10, 90, self.font)

        self.a1.pridej_postavu(s1)
        self.a1.pridej_postavu(l1)
        self.a1.pridej_postavu(k1)

        self.a2.pridej_postavu(s2)
        self.a2.pridej_postavu(l2)
        self.a2.pridej_postavu(k2)

        for postava in self.a2.postavy:
            postava.otoceni = False


    def vykresli(self):
        for a in [self.a1, self.a2]:
            for postava in a.postavy:
                postava.vykresli(self.screen)
                postava.pohyb()


    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.vykresli()
            self.clock.tick(60)
            pygame.display.flip()


game = Game()
game.loop()
