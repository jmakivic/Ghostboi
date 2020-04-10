import pygame, math, random

mokosh1 = "game_images/mokosh_intro_game.png"
mokosh2 = "game_images/mokosh_intro2_game.png"

class MokoshIntro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(mokosh1).convert_alpha()
        self.image = image_orig
        self.rect = self.image.get_rect()
        self.width = int(self.image.get_width())
        self.height = int(self.image.get_height())

    def face1(self):
        image_orig = pygame.image.load(mokosh1).convert_alpha()
        self.image = image_orig

    def face2(self):
        image_orig = pygame.image.load(mokosh2).convert_alpha()
        self.image = image_orig
