import pygame as pg, sys, random
from pygame.locals import *
from os.path import join
from pygame.math import Vector2 as vec

# Window
SCREEN_W = 600
SCREEN_H = 600

# Tiles
TILE_SIZE = 32

# Images
PLAYER_IMG = join( '..', 'assets', 'player', 'idle', 'idle_0_1.png' )
