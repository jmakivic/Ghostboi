import pygame, math, random

mokosh1 = "game_images/mokosh3_open_game.png"
mokosh2 = "game_images/mokosh3_close_game.png"

class Mokosh(pygame.sprite.Sprite):
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

    def mokosh_animation(self):
        expression = random.randint(0,2)

        if(expression == 1):
            self.face1()

        if(expression == 2):
            self.face2()

    def move(self, ghostX, ghostY, speed):
        if(self.rect.x < ghostX):
            self.rect.x += speed
        elif(self.rect.x > ghostX):
            self.rect.x -= speed

        if(self.rect.y <  ghostY):
            self.rect.y += speed

        if(self.rect.y > ghostY):
            self.rect.y -= speed
         

        

        
