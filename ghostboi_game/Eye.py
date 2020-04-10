import pygame, math, random

eye_open = "game_images/eye_open_game.png"
eye_half = "game_images/eye_half_game.png"
eye_closed = "game_images/eye_closed_game.png"

class Eye(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(eye_open).convert_alpha()
        self.image = image_orig
        self.rect = self.image.get_rect()
        self.width =int(self.image.get_width())
        self.height = int(self.image.get_height())

    def moveRight(self, pixels):
        self.rect.x+=pixels

    def moveLeft(self, pixels):
        self.rect.x-=pixels

    def moveForward(self, pixels):
        self.rect.y+=pixels

    def moveBackward(self, pixels):
        self.rect.y-=pixels

    def wide(self):
        image_orig = pygame.image.load(eye_open).convert_alpha()
        self.image = image_orig

    def half(self):
        image_orig = pygame.image.load(eye_half).convert_alpha()
        self.image = image_orig

    def closed(self):
        image_orig = pygame.image.load(eye_closed).convert_alpha()
        self.image = image_orig

    def eye_animation(self):
        expression = random.randint(0,3)
        y_move = random.randint(-10,10)
        x_move = random.randint(-10,10)

        if(expression ==1):
            self.wide()
            

        if(expression ==2):
            self.half()

        if(expression ==3):
            self.closed()

        

        self.rect.x+=x_move
        self.rect.y +=y_move

        if(self.rect.x <0):
            self.rect.x = 5

        if(self.rect.x >800):
            self.rect.x = 780

        if(self.rect.y<0):
            self.rect.y = 5

        if(self.rect.y > 480):
            self.rect.y =440
