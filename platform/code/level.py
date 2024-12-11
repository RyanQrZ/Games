from settings import *
from entities import *

class Level:

    def __init__( self ):
        self.surface = pg.display.get_surface()

        # Creating groups
        self.platforms_sprites = pg.sprite.Group()

        # Creating first ground
        self.fground = Platform( self.platforms_sprites, 0, 0 )
        self.fground.image = pg.Surface( (SCREEN_W, SCREEN_H - 32) )
        self.fground.image.fill( (0, 0, 0) )
        self.fground.rect = self.fground.image.get_rect( topleft = ( 0, SCREEN_H - 32 ) )

        # Reference height
        self.ref_h = self.fground.rect.y
        
        self.p1 = Player()

    # Creates new platforsm
    def gen_plat( self ):
        while( len(self.platforms_sprites) < MAX_PLAT ):
            plat = Platform( self.platforms_sprites, 0, 0 )
            plat.rect.x  = random.randint(0, SCREEN_H - plat.image.get_width() )
            plat.rect.y = self.ref_h - random.randint(40, 50)
            self.ref_h = plat.rect.y
            
    def game_over( self ):
        if( self.p1.rect.top >= SCREEN_H ):
            return True
        else:
            return False

    def run( self ):

        # Background image
        self.surface.fill( (62, 47, 90) )

        # Scrolling
        delta_scroll = self.p1.move( self.platforms_sprites )
        for plat in self.platforms_sprites:
            plat.update( delta_scroll )
            if( plat.rect.top >= SCREEN_H ): plat.kill()

        self.gen_plat()

        self.platforms_sprites.draw( self.surface )

        flip = pg.transform.flip( self.p1.image, self.p1.flip, False )
        self.surface.blit( flip, self.p1.rect )
