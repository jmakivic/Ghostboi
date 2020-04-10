import pygame,math, random

cake = 'game_images/cake.png'
donut = 'game_images/donut.png'

class Dessert(pygame.sprite.Sprite):
    def __init__(self, taste):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(cake).convert_alpha()
        self.image = image_orig
        self.rect = self.image.get_rect()
        self.size = image_orig.get_size()
        self.phrase =""
        self.width = int(self.image.get_width())
        self.height = int(self.image.get_height())

        if(taste == 1):
            image_orig = pygame.image.load(cake).convert_alpha()
            self.image =image_orig
            self.rect = self.image.get_rect()

        if(taste == 2):
            image_orig = pygame.image.load(donut).convert_alpha()
            self.image = image_orig
            self.rect = self.image.get_rect()

        statement = random.randint(0,6)

        if (statement == 0):
            self.phrase = "so saccharine and so sad"

        if(statement == 1):
            self.phrase = "so fleeting and euphoric"

        if(statement == 2):
            self.phrase = "do not let Mokosh eat me"

        if(statement == 3):
            self.phrase = "i do not want to be immortal"

        if(statement == 4):
            self.phrase = "i do not want to live forever without tasting anything"

        if(statement == 5):
            self.phrase = "sugar makes me remember what it is like to be alive"

        if(statement == 6):
            self.phrase = "if i don't eat i will forget"
