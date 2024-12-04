from settings import *
from entities import *

class Level:

    def __init__( self ):
        self.surface = pg.display.get_surface()

        # Creating groups
        self.platforms_sprites = pg.sprite.Group()

        # Creating first ground
        self.fground = Platform( self.platforms_sprites, 0, 0 )
        self.fground.surf = pg.Surface( (SCREEN_W, 32) )
        self.fground.surf.fill( (255, 255, 0) )
        self.fground.rect = self.fground.surf.get_rect( topleft = (0, SCREEN_H - TILE_SIZE ) )
        
        self.p1 = Player()

        # Random platforms
        self.plat1 = Platform( self.platforms_sprites, 350, 445 )

        self.h_dist = self.plat1.rect[1] - TILE_SIZE * 5
        
        for plats in range( random.randint(4, 5) ):
            self.plat = Platform( self.platforms_sprites, self.h_dist - 95, self.h_dist )
            self.h_dist = self.plat.rect[1] - TILE_SIZE * 5

    def jump_event( self ):
        self.p1.jump( self.platforms_sprites )

    def game_over( self ):
        if( self.p1.rect.top >= SCREEN_H ):
            return True
        else:
            return False

    def gen_plats( self ):

        while( len(self.platforms_sprites) < 7 ):
            plat = Platform( self.platforms_sprites, self.h_dist - 95, self.h_dist )
            self.h_dist = self.plat.rect[1] - TILE_SIZE * 5

    def run( self ):

        self.surface.fill( 'purple' )

        for tiles in self.platforms_sprites:
            self.surface.blit( tiles.surf, tiles.rect )

        self.p1.update( self.platforms_sprites )
        self.surface.blit( self.p1.surf, self.p1.rect )

        # Scrolling
        if( self.p1.rect.top < SCREEN_H ):
            for plat in self.platforms_sprites:
                plat.rect.top += 1
                if( plat.rect.top >= SCREEN_H ): plat.kill()
        
        """if self.p1.rect.top <= SCREEN_H / 3:
            self.p1.pos.y += abs( self.p1.vel.y )
            for plat in self.platforms_sprites:
                plat.rect.y += abs( self.p1.vel.y )
                if( plat.rect.top >= SCREEN_H ): plat.kill()"""

        self.gen_plats()
