import pygame

img = 'game_images/glorious_leader.png'

class GloriousLeader(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(img).convert_alpha()
        self.image = image_orig
        self.rect = self.image.get_rect()
        
