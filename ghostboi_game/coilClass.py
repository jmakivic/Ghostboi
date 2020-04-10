import pygame
img = 'game_images/tentacles_1.png'

class Coils(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(img).convert_alpha()
        self.image= image_orig

        self.rect = self.image.get_rect()
        self.width = int(self.image.get_width())
        self.height = int(self.image.get_height())

        self.animate = False
        self.animation_speed = 3

    def phase1(self):
        image_orig = pygame.image.load("game_images/tentacles_1.png")
        self.image = image_orig

    def phase2(self):
        image_orig = pygame.image.load("game_images/tentacles_2.png")
        self.image = image_orig
