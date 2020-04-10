import pygame, math, random

tower = "game_images/tower_game.png"
ruins = "game_images/ruins_game.png"
board1 ="game_images/leader_board_clear_game.png"
board2 = "game_images/leader_board_game.png"
citadel = "game_images/citadel_game.png"

class Scenery(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_orig = pygame.image.load(tower).convert_alpha()
        self.image = image_orig
        self.rect = self.image.get_rect()
        self.width = int(self.image.get_width())
        self.height = int(self.image.get_height())

    def tower(self):
        image_orig = pygame.image.load(tower).convert_alpha()
        self.image = image_orig

    def ruins(self):
        image_orig = pygame.image.load(ruins).convert_alpha()
        self.image = image_orig

    def citadel(self):
        image_orig = pygame.image.load(citadel).convert_alpha()
        self.image = image_orig

    def board1(self):
        image_orig = pygame.image.load(board1).convert_alpha()
        self.image = image_orig

    def board2(self):
        image_orig =pygame.image.load(board2).convert_alpha()
        self.image = image_orig

    def board_animation(self):
        display = random.randint(0,2)

        if(display ==1):
            self.board1()

        if(display ==2):
            self.board2()
        
