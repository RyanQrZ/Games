import pygame as pg, sys, random
from pygame.locals import *
from os.path import join

# Window
SCREEN_W = 600
SCREEN_H = 600
THRESH = SCREEN_H / 3

# Maximum amount of platforms
MAX_PLAT = 101

# Images
PLAYER_IMG = pg.image.load( join( '..', 'assets', 'player', 'idle', 'idle_0_1.png' ) )

PLATFORM_IMG = [ pg.image.load(join('..', 'assets', 'map', 'Platforms', '1way_plat.png' )),
                 pg.image.load(join('..', 'assets', 'map', 'Platforms', '2way_plat.png')),
                 pg.image.load(join('..', 'assets', 'map', 'Platforms', '3way_plat.png'))]

BG_IMG = [ pg.image.load(join('..', 'assets', 'map', 'Background', 'complete', 'Brick_background.png')) ]
