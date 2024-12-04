#!/usr/bin/env python3

import pygame as pg, sys, random, time
from pygame.locals import *

pg.init()

# Display screen attributes
color = ( 147, 149, 151 )
SCREEN_W = 400
SCREEN_L = 550
SURF = pg.display.set_mode( (SCREEN_W, SCREEN_L) )
pg.display.set_caption( "car_game" )
background = pg.image.load( "AnimatedStreet.png" )

# Fonts
font_normal = pg.font.SysFont( "Verdana", 60 )
font_small = pg.font.SysFont( "Verdana", 20 )

# Frame rate
#fps = 90
frameRate = pg.time.Clock()

SPEED = 3
SCORE = 0
class Enemy( pg.sprite.Sprite ):
    
    def __init__( self ):
        super().__init__()
        self.image = pg.image.load( "Enemy.png" )
        self.rect = self.image.get_rect()
        self.rect.center = ( random.randint(self.rect.width, SCREEN_W - self.rect.width), 0 )

    def move( self ):
        global SCORE
        self.rect.move_ip( 0, SPEED )

        if( self.rect.bottom > SCREEN_L + 2 * self.rect.height ):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = ( random.randint(self.rect.width, SCREEN_W - self.rect.width), 0 )

class Player( pg.sprite.Sprite ):

    def __init__( self ):
        super().__init__()
        self.image = pg.image.load( "Player.png" )
        self.rect = self.image.get_rect()
        random_w = random.randint( self.rect.width, SCREEN_W - self.rect.width )
        random_l = SCREEN_L - self.rect.height
        self.rect.center = ( random_w, random_l )

    def move( self ):
        key_pressed = pg.key.get_pressed()

        if( self.rect.left > 0 ):
            if( key_pressed[K_LEFT] ):
                self.rect.move_ip( -6, 0 )

        if( self.rect.right < SCREEN_W ):
            if( key_pressed[K_RIGHT] ):
                self.rect.move_ip( 6, 0 )

        if( self.rect.top > 0 ):
            if( key_pressed[K_UP] ):
                self.rect.move_ip( 0, -3 )

        if( self.rect.bottom < SCREEN_L ):
            if( key_pressed[K_DOWN] ):
                self.rect.move_ip( 0, 3 )
            
# Making sprite objects
p1 = Player()
n1 = Enemy()

# Setting up groups
enemies = pg.sprite.Group()
enemies.add( n1 )

all_sprites = pg.sprite.Group()
all_sprites.add( p1 )
all_sprites.add( n1 )

# Custom event for increase difficulty
DIFFICULTY = pg.USEREVENT + 1
pg.time.set_timer( DIFFICULTY, 3000 )
    
running = True
while( running ):

    for event in pg.event.get():
        if( event.type == QUIT ):
            running = False
        elif( event.type == DIFFICULTY and SPEED <= 12 ):
            SPEED += 1

    SURF.fill( color )
    SURF.blit( background, (0, 0) )
    scores = font_small.render( str(SCORE), True, (0,0,0) )
    SURF.blit( scores, (10,10) )

    for object in all_sprites:
        SURF.blit( object.image, object.rect )
        object.move()

    if( pg.sprite.spritecollideany( p1, enemies) ):
        
        SURF.fill( (255, 0, 0) )
        game_over = font_normal.render( "Score: " + str(SCORE), True, (255, 255, 128) )
        SURF.blit( game_over, (30,250) )
        
        pg.mixer.Sound( 'crash.wav' ).play()
        
        pg.display.update()

        for object in all_sprites:
            object.kill()

        time.sleep(2.5)
        running = False

    pg.display.update()
    #frameRate.tick(fps)
    new_frame_rate = frameRate.tick() 
            
pg.quit()
sys.exit()
