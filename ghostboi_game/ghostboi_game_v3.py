import serial, time, pygame, math, random
from pygame.locals import *
import pyaudio
from time import sleep, time
import RPi.GPIO as GPIO
from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from ghostboiClass import Ghostboi
from ghostburger import Ghostburger
from Background import Background
from GloriousLeader import GloriousLeader
from coilClass import Coils
from dessert import Dessert
from Eye import Eye
from mokosh3 import Mokosh
from scenery import Scenery
from vermin import Vermin
from food import Food
from mokosh_level2 import Mokoshlevel2
from ghostboi_narrate import GhostboiIntro
from mokosh_intro import MokoshIntro
from knight import Knight 

pygame.init()


pygame.mouse.set_visible(False)

block_font = "fonts/cubicblock.ttf"
pixel_font = "fonts/PixelTwist.ttf"

SCREENWIDTH = 800
SCREENHEIGHT = 480

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

#uncomment if on actual pi
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

#defining GPIO barriers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

teeth = 4
GPIO.setup(teeth, GPIO.IN)

teethAlreadyPressed = False

channel1 = 17
channel2 = 27

GPIO.setup(channel1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(channel2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

channel1_up = False
channel2_up = False

channel1_already_up = False
channel2_already_up = False

#initializing motor
#uncomment this if on actual pi
#motor = PWMOutputDevice(23)
motor = PWMOutputDevice(14)
motor.value = 0

motor2 = PWMOutputDevice(18)
motor2.value = 0

motor3 = PWMOutputDevice(22)
motor3.value = 0


#initialize all of the sprites

#initialize all of the spitegroups:
common_sprites = pygame.sprite.Group()
all_burger_sprites = pygame.sprite.Group()
coil_sprites = pygame.sprite.Group()
dessert_sprites = pygame.sprite.Group()
eye_sprites = pygame.sprite.Group()

#Background

background1 =Background(1, [0,0])
background2 =Background(2,[0,0])

gov_warning = Background(6, [0,0])
mokosh_bg = Background(7, [0,0])
level2_bg = Background(8, [0,0])
bad_ending_bg = Background(9, [0,0])
good_ending_bg = Background(10, [0,0])

#Ghostboi:

ghostboi = Ghostboi()
ghostboi.rect.x = 10
ghostboi.rect.y = SCREENHEIGHT-200
posX = ghostboi.rect.x
posY = ghostboi.rect.y

common_sprites.add(ghostboi)

def moveGhost():
    channel1_up = not GPIO.input(channel1)
    channel2_up = not GPIO.input(channel2)

    if(channel1_up and not channel1_already_up):
        ghostboi.rect.x +=10

    if(channel2_up and not channel2_already_up):
        ghostboi.rect.y += 10

    if(ghostboi.rect.x > 800):
        ghostboi.rect.x = 700

    if(ghostboi.rect.x < 0):
        ghostboi.rect.x = 5

    if(ghostboi.rect.y >480):
        ghostboi.rect.y= 400

    if(ghostboi.rect.y<0):
        ghostboi.rect.y=1

    ghostboi.rect.x -= 5
    ghostboi.rect.y -= 5

#Ghostburgers:

for i in range(8):
    type = random.randint(0,3)
    color = 0

    if(type == 1):
        color = 1

    if(type == 2):
        color = 2

    if(type == 3):
        color = 3

    burger = Ghostburger(color)
    burger.rect.x = random.randint(100,700)
    burger.rect.y = random.randint(10,280)

    all_burger_sprites.add(burger)

total_burgers = 0
    

#Coils
coil = Coils()

coil.rect.x = 0
coil.rect.y = 0
coil_sprites.add(coil)

#level2 Sprites

#adding level 2 sprites

for i in range(10):
    rand_num = random.randint(0,2)

    if(rand_num == 1):
        dessert = Dessert(1)
        dessert_sprites.add(dessert)
        
        dessert.rect.x = random.randint(220,700)
        dessert.rect.y = random.randint(100,420)

    if(rand_num == 2):
        dessert = Dessert(2)
        dessert_sprites.add(dessert)

        dessert.rect.x = random.randint(220,700)
        dessert.rect.y = random.randint(100,420)

for i in range(3):
    
    eye = Eye()
    eye.rect.x = random.randint(100,700)
    eye.rect.y = random.randint(10,280)
    eye_sprites.add(eye)
    



#Glorious Leader
leader = GloriousLeader()
ending_sprites = pygame.sprite.Group()
ending_sprites.add(leader)

#level3 placeholder sprites
#temporary mokosh sprite, temporary objects - get the coding down
good_ending = False
bad_ending = False


vermin_sprites = pygame.sprite.Group()
level3_sprites = pygame.sprite.Group()
mokosh3_sprites = pygame.sprite.Group()
food_sprites = pygame.sprite.Group()
mokosh_lvl3= Mokosh()
    
mokosh_lvl3.rect.x = 700
mokosh_lvl3.rect.y = 320

scenery_tower = Scenery()
scenery_tower.rect.x = SCREENWIDTH/2-200
#draw new sceneries
scenery_ruins = Scenery()
scenery_ruins.ruins()
scenery_ruins.rect.x = -100

scenery_citadel = Scenery()
scenery_citadel.citadel()
scenery_citadel.rect.x = 620

scenery_board = Scenery()
scenery_board.board1()
scenery_board.rect.x = SCREENWIDTH/2
    

level3_sprites.add(scenery_tower)
level3_sprites.add(scenery_ruins)
level3_sprites.add(scenery_citadel)
level3_sprites.add(scenery_board)
    
mokosh3_sprites.add(mokosh_lvl3)

ghostboi.rect.x =10
ghostboi.rect.y = 10

screen.fill((0,255,125))

level_three_over = False



for i in range(20):
    color = random.randint(0,3)
    food = Food(color)
    food.rect.x = random.randint(100, 700)
    food.rect.y = random.randint(40,420)

    food_sprites.add(food)
    

#Knight functions

knight_sprites = pygame.sprite.Group()
knight = Knight()
knight.rect.x = 20
knight.rect.y =20
knight_sprites.add(knight)
    


#defining for text function

def clear_callback(surf, rect, color):
    surf.fill(color, rect)

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, size, color, font, location):
    largeText = pygame.font.Font(font, size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (location)
    screen.blit(TextSurf, TextRect)

#game functions for now

def ghostboi_expression():

    expression = random.randint(0,2)

    if(expression == 1):
        ghostboi.happy()

    if(expression == 0):
        ghostboi.euphoric()


def ghostboi_sad():
    expression = random.randint(0,2)

    if(expression == 1):
        ghostboi.sad()

    if(expression == 0):
        ghostboi.dejected()

def coil_animate():
    expression = random.randint(0,2)

    if(expression == 1):
        coil.phase1()

    if(expression == 0):
        coil.phase2()


def intro():

    orig_time = pygame.time.get_ticks()

    new_time = pygame.time.get_ticks()

    common_sprites.draw(screen)

    screen.fill((0,0,255))

    ghostboi.rect.x = SCREENWIDTH/2 -100
    ghostboi.rect.y = SCREENHEIGHT-320

    print(orig_time)

    while(new_time - orig_time < 10000):

        new_time = pygame.time.get_ticks()

        screen.fill((125,200,255))

        common_sprites.draw(screen)

        message_display("Ghostboi in the Land of the Dead", 48, (255,0,125),pixel_font,(SCREENWIDTH/2, SCREENHEIGHT/2 -160))

        message_display("touch my body. i feel through you", 36, (255, 10, 100), pixel_font,(SCREENWIDTH/2, (SCREENHEIGHT - 60) +1*random.randint(1,3)))
        

        ghostboi_expression()

        common_sprites.update()

        screen.blit(screen, (0,0))

        print(orig_time)
        print(new_time)
        pygame.display.flip()

    common_sprites.update()

    screen.blit(screen, (0,0))

    pygame.display.flip()

def highscores():

    screen.fill((125,200,255))
    screen.blit(background1.image,background1.rect)

    

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    message_counter = 0
    message = ""
    message_spacing = 80

    while(new_time - orig_time < 15000):

        message_display("HIGH SCORES", 64, (255,0,125), pixel_font, (SCREENWIDTH/2, 60))

        if(pygame.time.get_ticks() -new_time > 1100):

            if(message_counter == 0):
                message = "#1 1,990,457 -- PINK_GHOST -- 2047"

            if(message_counter == 1):
                message = "#2 1,559,453 -- SKULL_GRRL -- 2047"

            if(message_counter == 2):
                message = "#3 1,000,732 -- SKULL_GRRL -- 2046"

            if(message_counter == 3):
                message = "#4 000010001101010010101000"

            if(message_counter ==4):
                message = "#5 #_Z&&*****$%$#010100101000"

            if(message_counter == 5):
                message = "#6 NULL"

            if(message_counter == 6):
                message= "#7 1,000,586 -- PINK_GHOST -- 2047"

            if(message_counter == 7):
                message = "#8 963,421 -- SKULL_GRRL -- 2046"

            if(message_counter == 8):
                message = "#9 VOID"

            if(message_counter == 9):
                message = "#10 LOST"
                
            
            #message_display()            
            new_time = pygame.time.get_ticks()
            message_spacing += 36
            message_counter += 1

            message_display(message, 24, (255,0,125), pixel_font, (SCREENWIDTH/2, message_spacing))
            pygame.display.flip()
        
    screen.blit(screen, (0,0))    
    pygame.display.flip()

def ghostboi_log_1():

    screen.fill((000,000,000))

    screen.blit(screen, (0,0))
    pygame.display.flip()

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    motor.value = 0
    motor2.value =0
    motor3.value = 0

    ghostboi_narrate = GhostboiIntro()
    ghostboi_narrate.rect.x = SCREENWIDTH/2
    ghostboi_narrate.rect.y = 40
    intro_sprites =pygame.sprite.Group()
    intro_sprites.add(ghostboi_narrate)

    while (new_time-orig_time < 5000):
        screen.fill((000,000,000))
        intro_sprites.draw(screen)
        ghostboi_narrate.animation()

        

        message_display("thank you for finding me", 24, (255,0,125), pixel_font, (SCREENWIDTH/2 - 200, SCREENHEIGHT/2))
        message_display("after all of these years", 24, (255,0,125), pixel_font, (SCREENWIDTH/2 - 200, SCREENHEIGHT/2 + 40))
        new_time = pygame.time.get_ticks()

        intro_sprites.update()
        screen.blit(screen, (0,0))
        pygame.display.flip()

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while (new_time-orig_time < 5000):
        screen.fill((000,000,000))
        intro_sprites.draw(screen)

        
        ghostboi_narrate.animation()

        message_display("bend my arms, contort me", 24, (255,0,125), pixel_font, (SCREENWIDTH/2 - 200, SCREENHEIGHT/2))
        message_display("pick me up, rotate me", 24, (255,0,125), pixel_font, (SCREENWIDTH/2 - 200, SCREENHEIGHT/2 + 40))
        new_time = pygame.time.get_ticks()

        intro_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while (new_time - orig_time <5000):

        screen.fill((000,000,000))
        intro_sprites.draw(screen)
        ghostboi_narrate.animation()
        message_display("it makes me feel alive", 24, (255,0,125), pixel_font, (SCREENWIDTH/2-200, SCREENHEIGHT/2))
        new_time = pygame.time.get_ticks()

        motor.value = 1
        motor2.value = 1
        motor3.value = 1

        intro_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()

    motor.value = 0
    motor2.value =0
    motor3.value = 0    

    screen.blit(screen, (0,0))
    pygame.display.flip()

    #turn on the vibration . . . 
    print("Ghostboi log 1")

def mokosh1():
    screen.fill((200,0,50))
    screen.blit(mokosh_bg.image,mokosh_bg.rect)

    motor.value = 0
    motor2.value =0
    motor3.value = 0  

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    mokosh_intro = MokoshIntro()
    mokosh_intro.rect.x = SCREENWIDTH/2 -100
    mokosh_intro.rect.y = 40
    
    intro_sprites = pygame.sprite.Group()
    intro_sprites.add(mokosh_intro)

    while(new_time - orig_time < 5000):
        screen.fill((200,0,50))
        screen.blit(mokosh_bg.image,mokosh_bg.rect)
        intro_sprites.draw(screen)
        mokosh_intro.face2()
        message_display("join me, ghostboi", 30, (217,50,128), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        message_display("in the glowing coils of the afterlife", 30, (217,50,128), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 192+ 1*random.randint(-3,3)))
        new_time = pygame.time.get_ticks()

        intro_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 5000):
        screen.fill((200,0,50))
        screen.blit(mokosh_bg.image,mokosh_bg.rect)
        intro_sprites.draw(screen)
        mokosh_intro.face1()
        message_display("you will no longer feel anything", 24, (217,50,128), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        
        new_time = pygame.time.get_ticks()

        motor.value = 0.7
        motor2.value = 0.7
        motor3.value =0.7

        intro_sprites.update()
        screen.blit(screen, (0,0))
        pygame.display.flip()

    motor.value = 0
    motor2.value =0
    motor3.value = 0  

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    

    screen.blit(screen, (0,0))
    pygame.display.flip()

def coil_drag1():

    coil_drag_true = False
    ghostboi.rect.x = 760
    ghostboi.rect.y = 400

    while(coil_drag_true == False):

      

        orig_time = pygame.time.get_ticks()
        new_time =pygame.time.get_ticks()

        screen.blit(background1.image, background1.rect)

        coil_sprites.draw(screen)
        common_sprites.draw(screen)
        coil_animate()
        ghostboi_sad()

        message_display("oh no mokosh is dragging me to her coils", 30, (0,51,31), pixel_font, (SCREENWIDTH/2,192+ 1*random.randint(-3,3)))
        message_display("i do not want to be numb, i want to feel!!!!!!", 30, (0,51,31), pixel_font, (SCREENWIDTH/2,260+ 1*random.randint(-3,3)))
        

        ghostboi.rect.x -= 8
        ghostboi.rect.y-=4

        if(ghostboi.rect.x <10 and ghostboi.rect.y <10):
            coil_drag_true = True

        screen.blit(screen, (0,0))
        pygame.display.flip()
    

def level1():
    print("level1")

    level1_over = False

    ghostboi.rect.x = 10
    ghostboi.rect.y = 10

    screen.fill((125, 200, 255))
    screen.blit(background1.image, background1.rect)

    #relevant level variables
    burger_count = 0

    
    #declaring value of motor
    motor.value = 0
    while(not level1_over):

        screen.blit(background1.image, background1.rect)

      
        coil_sprites.draw(screen)
        all_burger_sprites.draw(screen)
        common_sprites.draw(screen)

        message_display("bend my arms or rotate me, to move my body",36,(0,51,31),pixel_font,(SCREENWIDTH/2,10+1*random.randint(1,3)))
        message_display("press my eyes to eat the burgers",36,(0,51,31),pixel_font,(SCREENWIDTH/2,50+1*random.randint(1,3)))

        moveGhost()
        ghostboi.neutral()
        coil_animate()

        motor.value =0
        motor2.value = 0
        motor3.value = 0

        teethPressed = not GPIO.input(teeth)
        burger_collision_list = pygame.sprite.spritecollide(ghostboi, all_burger_sprites, False, collided = pygame.sprite.collide_rect_ratio(0.5))
        for burger in burger_collision_list:
            #remove the burger after touching the teeth
            if(teethPressed and not teethAlreadyPressed):
                burger_count += 1
                message_display(burger.phrase,36,(255,0,125),pixel_font,(SCREENWIDTH/2,450+1*random.randint(1,20)))
                burger.rect.y += 1 * random.randint(-2,2)

                ghostboi_expression()

                if(burger_count >= 10):
                    screen.fill((255,255,255))
                    all_burger_sprites.remove(burger)
                    burger_count = 0
                    
            if(len(all_burger_sprites.sprites()) == 0):
                level1_over = True
                print("level over")

        coil_collision_list = pygame.sprite.spritecollide(ghostboi, coil_sprites, False, collided = pygame.sprite.collide_rect_ratio(0.5))
        for coil in coil_collision_list:
            #make a message appear
            message_display("take me away from the coils of the afterlife!", 36, (125,0,125), pixel_font, (SCREENWIDTH/2, 300 +1*random.randint(1,20)))
            ghostboi_sad()
            motor.value=0.5
            motor2.value =0.5
            motor3.value = 0.5

        all_burger_sprites.update()
        common_sprites.update()
        coil_sprites.update()

        
        
        screen.blit(screen, (0,0))
        pygame.display.flip()

    

    screen.blit(screen, (0,0))
    pygame.display.flip()

def level_1_over_transition():
    print("transition")
    
    screen.fill((125,0,255))

    ghostboi.rect.x = 10
    ghostboi.rect.y = 10

    dessert_count = 0
    

    screen.blit(background1.image, background1.rect)

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 6000):

        screen.blit(background1.image, background1.rect)
        
        message_display("i am still empty", 36, (125,0,125), pixel_font, (SCREENWIDTH/2, 200 +1*random.randint(1,20)))
        message_display("but i ate everything", 36, (125,0,125), pixel_font, (SCREENWIDTH/2, 260 +1*random.randint(1,20)))
        new_time = pygame.time.get_ticks()
    
        coil_sprites.draw(screen)
        common_sprites.draw(screen)

        moveGhost()
        ghostboi.neutral()
        coil_animate()

        coil_sprites.update()
        common_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()

def state_sponsored():
    screen.fill((0,0,0))
    

    
    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 10000):

        new_time = pygame.time.get_ticks()

        ending_sprites.draw(screen)

        message_display("This game brought to you by the glorious leader", 28,(206,244,66) ,pixel_font, (SCREENWIDTH/2, 100))
        
        ending_sprites.update()
        pygame.display.flip()

        screen.blit(screen, (0,0))

    
    screen.blit(screen,(0,0))
    pygame.display.flip()

def mokosh2_log():
    screen.fill((200,0,50))
    screen.blit(mokosh_bg.image,mokosh_bg.rect)

    motor.value = 0
    motor2.value =0
    motor3.value = 0  

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    mokosh_lvl2 = Mokoshlevel2()
    intro_sprites = pygame.sprite.Group()
    intro_sprites.add(mokosh_lvl2)

    while(new_time - orig_time < 5000):
        screen.fill((200,0,50))
        screen.blit(mokosh_bg.image,mokosh_bg.rect)
        intro_sprites.draw(screen)
        mokosh_lvl2.animation()
        message_display("join me, ghostboi", 30, (217,50,128), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        message_display("in the glowing coils of the afterlife", 30, (217,50,128), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 192+ 1*random.randint(-3,3)))
        new_time = pygame.time.get_ticks()

        intro_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 5000):
        screen.fill((200,0,50))
        screen.blit(mokosh_bg.image,mokosh_bg.rect)
        intro_sprites.draw(screen)
        mokosh_lvl2.rect.y +=random.randint(-3,3)
        mokosh_lvl2.animation()
        message_display("you will no longer feel anything", 24, (217,50,128), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        
        new_time = pygame.time.get_ticks()

        motor.value = 0.7
        motor2.value = 0.7
        motor3.value =0.7

        intro_sprites.update()
        screen.blit(screen, (0,0))
        pygame.display.flip()

    motor.value = 0
    motor2.value =0
    motor3.value = 0  

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    screen.blit(screen, (0,0))
    pygame.display.flip()

def coil_drag_2():
    coil_drag_true = False
    ghostboi.rect.x = 760
    ghostboi.rect.y = 400

    while(coil_drag_true == False):

      

        orig_time = pygame.time.get_ticks()
        new_time =pygame.time.get_ticks()

        screen.blit(level2_bg.image, level2_bg.rect)

        coil_sprites.draw(screen)
        common_sprites.draw(screen)
        coil_animate()
        ghostboi_sad()

        message_display("oh no!!! mokosh has found me", 30, (245,66,144), pixel_font, (SCREENWIDTH/2,192+ 1*random.randint(-3,3)))
        message_display("she is trying to drag me into her coils again !!!", 30, (245,66,144), pixel_font, (SCREENWIDTH/2,260+ 1*random.randint(-3,3)))
        

        ghostboi.rect.x -= 8
        ghostboi.rect.y-=4

        if(ghostboi.rect.x <10 and ghostboi.rect.y <10):
            coil_drag_true = True

        screen.blit(screen, (0,0))
        pygame.display.flip()

def level2():
    level2_over = False
    screen.fill((125,0,255))
    screen.blit(level2_bg.image, level2_bg.rect)

    ghostboi.rect.x = 10
    ghostboi.rect.y = 10

    dessert_count = 0
    eye_collision_count = 0

    screen.blit(background1.image, background1.rect)

    while(not level2_over):
        screen.blit(level2_bg.image, level2_bg.rect)
        coil_sprites.draw(screen)

        message_display("bend my arms or rotate me, to move my body",40,(245,66,144),pixel_font,(SCREENWIDTH/2,10+1*random.randint(1,3)))
        message_display("press my eyes to eat the desserts",40,(245,66,144),pixel_font,(SCREENWIDTH/2,50+1*random.randint(1,3)))
       
        dessert_sprites.draw(screen)
        eye_sprites.draw(screen)
        
        common_sprites.draw(screen)

                        
        motor.value = 0
        motor2.value = 0
        motor3.value =0

        moveGhost()
        ghostboi.neutral()
        coil_animate()

        for eye in eye_sprites:
            eye.eye_animation()

        
        teethPressed = not GPIO.input(teeth)
        dessert_collision_list = pygame.sprite.spritecollide(ghostboi, dessert_sprites, False, collided = pygame.sprite.collide_rect_ratio(0.5))
        for dessert in dessert_collision_list:
            if(teethPressed and not teethAlreadyPressed):
                message_display(dessert.phrase, 36, (255,0,125), pixel_font, (SCREENWIDTH/2, 280))
                dessert_count += 1
                ghostboi_expression()
                dessert.rect.y+=random.randint(-2,2)

                if(dessert_count >=10):
                    dessert_sprites.remove(dessert)
                    screen.fill((255,255,255))
                    dessert_count = 0

                     

            if(len(dessert_sprites.sprites()) == 0):
                level2_over = True
                print("level over")

        coil_collision_list = pygame.sprite.spritecollide(ghostboi, coil_sprites, False, collided = pygame.sprite.collide_rect_ratio(0.5))
        for coil in coil_collision_list:
            #make a message appear
            message_display("take me away from the coils of the afterlife!", 36, (66,155,245), pixel_font, (SCREENWIDTH/2, 300 +1*random.randint(1,20)))
            ghostboi_sad()
            motor.value=0.7
            motor2.value =0.7
            motor3.value = 0.7

    
        #eye_collisiostn
        eye_collision_list = pygame.sprite.spritecollide(ghostboi, eye_sprites, False, collided = pygame.sprite.collide_rect_ratio(0.4))
        for eye in eye_collision_list:
            message_display("I cannot touch the eyes! Mokosh will find me!", 36, (50,189,217), pixel_font, (SCREENWIDTH/2,100+1*random.randint(-5,20)))
            motor.value = 1
            motor2.value = 1
            motor3.value = 1
            ghostboi_sad()
           
        #make the eyes move

        common_sprites.update()
        dessert_sprites.update()
        coil_sprites.update()
        eye_sprites.update()

        screen.blit(screen,(0,0))
        pygame.display.flip()
        
    screen.blit(screen, (0,0))
    pygame.display.flip()

def level_2_over():
    screen.fill((125,0,255))

    ghostboi.rect.x = 10
    ghostboi.rect.y = 10

    dessert_count = 0
    screen.blit(level2_bg.image, level2_bg.rect)
    

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 6000):

        screen.blit(level2_bg.image, level2_bg.rect)
        
       
        eye_sprites.draw(screen)
        coil_sprites.draw(screen)
        common_sprites.draw(screen)

        moveGhost()
        ghostboi.neutral()
        coil_animate()

        message_display("sugar makes me feel warm", 36, (245,66,144), pixel_font, (SCREENWIDTH/2, 200 +1*random.randint(1,20)))
        message_display("i avoided the eyes and the abyss", 36, (245,66,144), pixel_font, (SCREENWIDTH/2, 260 +1*random.randint(1,20)))
    
     
        coil_sprites.update()
        common_sprites.update()

        new_time = pygame.time.get_ticks()

        screen.blit(screen, (0,0))
        pygame.display.flip()

    

def mokosh3():
    print("Mokosh threatens Ghostboi")
    screen.fill((200,0,50))
    screen.blit(mokosh_bg.image, mokosh_bg.rect)

    motor.value = 0
    motor2.value =0
    motor3.value = 0  

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    mokosh_lvl2 = Mokoshlevel2()
    mokosh_lvl2.rect.x = SCREENWIDTH/2 -100
    mokosh_lvl2.rect.y = 10
    intro_sprites = pygame.sprite.Group()
    intro_sprites.add(mokosh_lvl2)

    while(new_time - orig_time < 5000):
        screen.fill((230,103,152))
        screen.blit(mokosh_bg.image, mokosh_bg.rect)
        intro_sprites.draw(screen)
        mokosh_lvl2.animation()
        message_display("you have evaded me once again", 30, (255, 100, 200), pixel_font, (SCREENWIDTH/2+80,  SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        message_display("but why would you feel pain", 30, (255, 100, 200), pixel_font, (SCREENWIDTH/2+80, SCREENHEIGHT/2 + 192+ 1*random.randint(-3,3)))
        new_time = pygame.time.get_ticks()

        intro_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 5000):
        screen.fill((230,103,152))
        screen.blit(mokosh_bg.image, mokosh_bg.rect)
        intro_sprites.draw(screen)
        mokosh_lvl2.animation()
        message_display("when you can feel nothing", 30, (255, 100, 200), pixel_font, (SCREENWIDTH/2+80, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        
        new_time = pygame.time.get_ticks()

        motor.value = 0.7
        motor2.value = 0.7
        motor3.value =0.7

        intro_sprites.update()
        screen.blit(screen, (0,0))
        pygame.display.flip()

    motor.value = 0
    motor2.value =0
    motor3.value = 0  

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    screen.blit(screen, (0,0))
    pygame.display.flip()

def government_warning():
    screen.fill((200,0,50))
    screen.blit(gov_warning.image, gov_warning.rect)

    motor.value = 0
    motor2.value =0
    motor3.value = 0

    
    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()


    while(new_time - orig_time < 5000):
        screen.fill((200,0,50))
        screen.blit(gov_warning.image, gov_warning.rect)

       
        message_display("the end is imminent", 30, (7, 28, 59), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        message_display("surveillance tendrils detect a threat", 30, (7, 28, 59), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 192+ 1*random.randint(-3,3)))
        new_time = pygame.time.get_ticks()

      
        screen.blit(screen, (0,0))
        pygame.display.flip()

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 5000):
        screen.fill((200,0,50))
        screen.blit(gov_warning.image, gov_warning.rect)
        
       
        message_display("you will no longer feel anything", 30, (7, 28, 59), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
      
        new_time = pygame.time.get_ticks()

      
        screen.blit(screen, (0,0))
        pygame.display.flip()


    screen.blit(screen, (0,0))
    pygame.display.flip()


def advertisement():
    screen.fill((0,0,0))
    screen.blit(background1.image, background1.rect)
    
    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 5000):
        screen.fill((200,0,50))
        screen.blit(background1.image, background1.rect)
        
        knight_sprites.draw(screen)
        knight.animation()
        message_display("Come see the holographic knight", 36, (83,50,217), pixel_font, (SCREENWIDTH/2-100, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        message_display("i'm just data", 30, (255, 100, 200), pixel_font, (SCREENWIDTH/2+160, 192+ 1*random.randint(-3,3)))
      
        new_time = pygame.time.get_ticks()

        knight_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    while(new_time - orig_time < 5000):
        screen.fill((200,0,50))
        knight_sprites.draw(screen)
        screen.blit(background1.image, background1.rect)
        knight_sprites.draw(screen)
        knight.animation()
      
        message_display("i  don't even have a face", 24, (255, 100, 200), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 215+ 1*random.randint(-3,3)))
       
        
        new_time = pygame.time.get_ticks()
        knight_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()

    motor.value = 0
    motor2.value =0
    motor3.value = 0  

    orig_time = pygame.time.get_ticks()
    new_time =pygame.time.get_ticks()

    screen.blit(screen, (0,0))
    pygame.display.flip()


def level3_transition():
    print("Transition to Level3")

    orig_time = pygame.time.get_ticks()
    new_time = pygame.time.get_ticks()

    while(new_time - orig_time <6000):

        new_time = pygame.time.get_ticks()

        screen.fill((0,255,125))
        level3_sprites.draw(screen)
        common_sprites.draw(screen)
        
        mokosh3_sprites.draw(screen)
        
        moveGhost()
        ghostboi.neutral()
        mokosh_lvl3.rect.y += random.randint(-3,3)
        mokosh_lvl3.mokosh_animation()
        scenery_board.board_animation()

        message_display("if i want to feel alive i need to eat everything ", 24, (7, 7, 59), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 160+ 1*random.randint(-3,3)))
        message_display("if mokosh touches me she will fill the world with vermin ", 24, (7, 7, 59), pixel_font, (SCREENWIDTH/2, SCREENHEIGHT/2 + 220+ 1*random.randint(-3,3)))
        
        
        level3_sprites.update()
        common_sprites.update()
        
        mokosh3_sprites.update()
        

        screen.blit(screen, (0,0))
        pygame.display.flip()
        

      



def level3():
    print("level3")

    food_count = 0
    mokosh_count = 0
    level_three_over = False

    

    while(not level_three_over):

        
        screen.fill((0,255,125))
        level3_sprites.draw(screen)
        common_sprites.draw(screen)
        vermin_sprites.draw(screen)
        mokosh3_sprites.draw(screen)
        food_sprites.draw(screen)
        moveGhost()
        ghostboi.neutral()
        mokosh_lvl3.move(ghostboi.rect.x, ghostboi.rect.y,1)
        mokosh_lvl3.mokosh_animation()
        scenery_board.board_animation()

        motor.value =0
        motor2.value = 0
        motor3.value = 0

        message_display("bend my arms or rotate me, to move my body",40,(0,51,31),pixel_font,(SCREENWIDTH/2,10+1*random.randint(1,3)))
        message_display("press my eyes to eat the desserts",40,(0,51,31),pixel_font,(SCREENWIDTH/2,50+1*random.randint(1,3)))
        

        teethPressed = not GPIO.input(teeth)
        
        food_collision_list = pygame.sprite.spritecollide(ghostboi, food_sprites, False, collided = pygame.sprite.collide_rect_ratio(0.5))
        for food in food_collision_list:
            if(teethPressed and not teethAlreadyPressed):
                message_display("i am alive", 36, (255,0,125), pixel_font, (SCREENWIDTH/2, 280))
                food_count += 1
                food.rect.y+= random.randint(-2,2)
                ghostboi_expression()

                if(food_count >=10):
                    food_sprites.remove(food)
                    screen.fill((255,255,255))
                    food_count = 0                    

            if(len(food_sprites.sprites()) == 0):
                
                print("level over")

        mokosh_collision_list = pygame.sprite.spritecollide(ghostboi, mokosh3_sprites, False, collided = pygame.sprite.collide_rect_ratio(0.5))
        for mokosh in mokosh_collision_list:
            #make a message appear
            message_display("the vermin are eating me!", 36, (125,0,125), pixel_font, (SCREENWIDTH/2, 300 +1*random.randint(1,20)))
            ghostboi_sad()
            motor.value=0.7
            motor2.value = 0.7
            motor3.value = 0.7
            mokosh_count += 1

            if(mokosh_count >=5):

                vermin = Vermin(2)
                vermin.rect.x = random.randint(100,700)
                vermin.rect.y = random.randint(10,470)

                vermin_sprites.add(vermin)

                mokosh_count =0


        if(len(vermin_sprites.sprites()) >= 120):
              

                orig_time = pygame.time.get_ticks()
                new_time =pygame.time.get_ticks()

                while(new_time - orig_time < 6000):

                    screen.blit(bad_ending_bg.image, bad_ending_bg.rect)
                
                    common_sprites.draw(screen)

                    ghostboi.neutral()
                    coil_animate()

                    print("ending_bad")

                    message_display("mokosh buried me in her vermin", 36, (125,0,125), pixel_font, (SCREENWIDTH/2, 200 +1*random.randint(1,20)))
                    message_display("i am numb", 36, (125,0,125), pixel_font, (SCREENWIDTH/2, 260 +1*random.randint(1,20)))
                
                    common_sprites.update()
                    new_time =pygame.time.get_ticks()

                    screen.blit(screen, (0,0))
                    pygame.display.flip()

                level_three_over = True
                bad_ending =True
                print("bad")

        if(len(food_sprites.sprites()) == 0):
                
                print("good")

                orig_time = pygame.time.get_ticks()
                new_time =pygame.time.get_ticks()

                while(new_time - orig_time < 6000):

                        screen.blit(good_ending_bg.image, good_ending_bg.rect)
                        
                        common_sprites.draw(screen)

                        ghostboi.neutral()
                        coil_animate()
                        print("ending good")
                        message_display("i ate everything", 36, (125,0,125), pixel_font, (SCREENWIDTH/2, 200 +1*random.randint(1,20)))
                        message_display("i am truly alive", 36, (125,0,125), pixel_font, (SCREENWIDTH/2, 260 +1*random.randint(1,20)))
                     
                    
                        common_sprites.update()
                        new_time =pygame.time.get_ticks()

                        screen.blit(screen, (0,0))
                        pygame.display.flip()

                level_three_over = True
                good_ending = True

                

        
        

        level3_sprites.update()
        common_sprites.update()
        vermin_sprites.update()
        mokosh3_sprites.update()
        food_sprites.update()

        screen.blit(screen, (0,0))
        pygame.display.flip()


    screen.blit(screen, (0,0))
    pygame.display.flip()



    

intro()
ghostboi_log_1()
mokosh1()
coil_drag1()
level1()
level_1_over_transition()
government_warning()
mokosh2_log()
coil_drag_2()
level2()
level_2_over()
state_sponsored()
advertisement()
level3_transition()
level3()
highscores()

pygame.quit()

    
    
