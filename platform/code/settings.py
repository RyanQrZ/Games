import pygame as pg, sys, random
from pygame.locals import *
from os.path import join

# Window
SCREEN_W = 600
SCREEN_H = 600
THRESH = SCREEN_H / 3

# Controls
KEY_ML = K_LEFT
KEY_MR = K_RIGHT
KEY_CONT = K_SPACE

# Fonts
pg.font.init()
FONT_BIG = pg.font.SysFont( "Verdana", 60 )
FONT_SMALL = pg.font.SysFont( 'Lucida Sans', 24 )
FONT_ESMALL = pg.font.SysFont( 'Lucida Sans', 30 )

# Maximum amount of platforms
MAX_PLAT = 10

# Images
PLAYER_IMG = pg.image.load( join( '..', 'assets', 'player', 'idle', 'idle_0_1.png' ) )

PLATFORM_IMG = [ pg.image.load(join('..', 'assets', 'map', 'Platforms', '1way_plat.png' )),
                 pg.image.load(join('..', 'assets', 'map', 'Platforms', '2way_plat.png')),
                 pg.image.load(join('..', 'assets', 'map', 'Platforms', '3way_plat.png'))]

BG_IMG = [ pg.image.load(join('..', 'assets', 'map', 'Background', 'complete', 'Brick_background.png')) ]
