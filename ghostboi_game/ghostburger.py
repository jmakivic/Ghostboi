import pygame, math, random

img = 'game_images/ghostburger_reg.png'
img_blue = 'game_images/ghostburger_blue.png'
img_pink = 'game_images/ghostburger_pink.png'
img_big = 'game_images/ghostburger.png'

class Ghostburger(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(img).convert_alpha()
        self.image = image_orig
        self.rect = self.image.get_rect()
        self.size = image_orig.get_size()
        self.phrase =""
        self.width = int(self.image.get_width())
        self.height = int(self.image.get_height())

        self.animate = False
        self.animation_speed = 3
        
        if(color == 1):
            image_orig = pygame.image.load(img).convert_alpha()
            self.image = image_orig
            self.rect = self.image.get_rect()

        
        if(color == 2):
            image_orig = pygame.image.load(img_blue).convert_alpha()
            self.image = image_orig
            self.rect = self.image.get_rect()

        if(color == 3):
            image_orig = pygame.image.load(img_pink).convert_alpha()
            self.image = image_orig
            self.rect = self.image.get_rect()

        if(color == 4):
            image_orig = pygame.image.load(img_big).convert_alpha()
            self.image = image_orig
            self.rect = self.image.get_rect()

        

        statement = random.randint(0,7)
    
                
        if (statement == 0):
            self.phrase="i remember the taste of real burgers"

        elif (statement == 1):
            self.phrase="taste is ephemeral"

        elif (statement == 2):
            self.phrase="ghostburgers taste like nothing"

        elif (statement == 3):
            self.phrase="feed my soul"


        elif (statement == 4):
            self.phrase="i live in the void"

        elif (statement == 5):
            self.phrase="i left my body on earth, please feed it"

        elif (statement == 6):
            self.phrase="this world exists next to real life"

        elif (statement == 7):
            self.phrase="afterlife brought to you by the glorious leader"

    def update(self):
        if self.animate:
            if self.animation_target_width > self.rect.width or self.animation_target_height > self.rect.height:
                center_location = selg.rect.center
                self.image = pygame.transform.scale(self.original_image, (self.rect.width+self.animation_speed, self.rect.height+self.animation_speed))
                self.rect = self.image.get_rect()
                self.rect.center = center_location

            if self.animation_target_width < self.rect.width or self.animation_target_height < self.rect.height:
                center_location = self.rect.center
                self.image = pygame.transform.scale(self.original_image, (self.rect.width-self.animation_speed, self.rect.height-self.animation_speed))
                self.rect = self.image.get_rect()
                self.rect.center = center_location


    

        
    
