from settings import *
from entities import *

class Level:

    def __init__( self ):
        self.surface = pg.display.get_surface()
        self.isOver = False
        self.score = 0

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

    def run( self ):

        # Background image
        #self.surface.fill( (62, 47, 90) )
        self.surface.fill( 'light yellow' )

        # Scrolling
        delta_scroll = self.p1.move( self.platforms_sprites )
        for plat in self.platforms_sprites:
            plat.update( delta_scroll )
            if( plat.rect.top >= SCREEN_H ):
                plat.kill()
                self.score += 1

        self.gen_plat()

        self.platforms_sprites.draw( self.surface )

        flip = pg.transform.flip( self.p1.image, self.p1.flip, False )
        self.surface.blit( flip, self.p1.rect )

        # Score string
        self.write_text( str(self.score), FONT_ESMALL, (255,0,0), SCREEN_W // 2, 1 )

        if( self.p1.rect.top >= SCREEN_H ):
            self.isOver = True

    def game_over( self ):
        self.surface.fill( (0,0,0) )
        
        str1 = "SCORE: " + str(self.score)
        str2 = "PRESS SPACE TO CONTINUE"
        self.write_text( str1, FONT_BIG, (255,0,0), 150 , SCREEN_H // 2 )
        self.write_text( str2, FONT_SMALL, (255,0,0), 150, SCREEN_H // 2 + 100 )

    def write_text( self, text, font, color, x_pos, y_pos ):
        image = font.render( text, True, color )
        self.surface.blit( image, (x_pos, y_pos) )
