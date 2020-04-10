import pygame, math, random

knight1 = "game_images/knight_closeup2_game.png"
knight2 = "game_images/knight_closeup_game.png"

class Knight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(knight1).convert_alpha()
        self.image = image_orig
        self.rect = self.image.get_rect()
        self.width = int(self.image.get_width())
        self.height = int(self.image.get_height())

    def face1(self):
        image_orig = pygame.image.load(knight1).convert_alpha()
        self.image = image_orig

    def face2(self):
        image_orig = pygame.image.load(knight2).convert_alpha()
        self.image = image_orig

    def animation(self):
        display = random.randint(0,2)

        if(display ==1):
            self.face1()

        if(display ==2):
            self.face2()
