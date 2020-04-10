import pygame, math, random

img = "game_images/ghostburger_reg.png"
img_blue = "game_images/ghostburger_blue.png"
img_pink = "game_images/ghostburger_pink.png"

class Food(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(img).convert_alpha()
        self.image = image_orig
        self.rect = self.image.get_rect()
        self.size = image_orig.get_size()
        self.phrase = ""
        self.width = int(self.image.get_width())
        self.height = int(self.image.get_height())

        if(color == 1):
            image_orig = pygame.image.load(img).convert_alpha()
            self.image = image_orig
            self.rect = self.image.get_rect()

        if(color ==2):
            image_orig = pygame.image.load(img_blue).convert_alpha()
            self.image = image_orig
            self.rect = self.image.get_rect()

        if(color ==3):
            image_orig = pygame.image.load(img_pink).convert_alpha()
            self.image = image_orig
            self.rect = self.image.get_rect()
