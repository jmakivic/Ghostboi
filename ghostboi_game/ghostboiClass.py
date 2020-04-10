import pygame
img = 'game_images/ghostboi_sprite.png'

class Ghostboi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(img).convert_alpha()
        self.image = image_orig

        self.rect = self.image.get_rect()
        self.width = int(self.image.get_width())
        self.height = int(self.image.get_height())

        self.animate = False
        self.animation_speed = 3
        #self.speed = speed

    def moveRight(self, pixels):
        self.rect.x+=pixels

    def moveLeft(self, pixels):
        self.rect.x-= pixels

    def moveForward(self, pixels):
        self.rect.y += pixels

    def moveBackward(self, pixels):
        self.rect.y -=pixels

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color,[0,0,self.width, self.height])

    def scaleGhost(self, new_width, new_height):
        center = self.rect.center
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center = center

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

    def scale_animation(self, new_width, new_height):
        self.animate = True
        self.animation_target_width = new_width
        self.animation_target_height = new_height
        self.original_image = self.image

    def neutral(self):
        image_orig = pygame.image.load(img).convert_alpha()
        self.image = image_orig
        


    def happy(self):
        image_orig = pygame.image.load("game_images/ghostboi_euphoric.png").convert_alpha()
        self.image = image_orig
        

    def euphoric(self):
        image_orig = pygame.image.load("game_images/ghostboi_euphoric_2.png").convert_alpha()
        self.image = image_orig
        

    def sad(self):
        image_orig = pygame.image.load("game_images/ghostboi_sad.png").convert_alpha()
        self.image = image_orig
        

        

    def dejected(self):
        image_orig = pygame.image.load("game_images/ghostboi_dejected.png").convert_alpha()
        self.image = image_orig
        

        

    
        
