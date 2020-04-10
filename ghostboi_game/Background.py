import pygame
background1 = "game_images/background1.png"
background2 = "game_images/background2.png"
background3 = "game_images/Background3.png"
background4 = "game_images/desktop_fullsize.png"
path1_bg = "game_images/path1.jpg"
path2_bg = "game_images/path2.jpg"
mokosh_bg = "game_images/mokosh_background.png"
level_2_bg = "game_images/level2_bg.png"
bad_ending = "game_images/bad_ending.png"
good_ending_bg = "game_images/good_ending_bg.png"


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)

        if(image_file ==1):
            
            self.image = pygame.image.load(background1)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file == 2):

            self.image =pygame.image.load(background2)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file == 3):

            self.image = pygame.image.load(background3)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file ==4):
            self.image = pygame.image.load(background4)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file == 5):
            self.image = pygame.image.load(path1_bg)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file == 6):
            self.image = pygame.image.load(path2_bg)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file == 7):
            self.image = pygame.image.load(mokosh_bg)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file == 8):
            self.image = pygame.image.load(level_2_bg)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file == 9):
            self.image = pygame.image.load(bad_ending)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

        if(image_file == 10):
            self.image = pygame.image.load(good_ending_bg)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

