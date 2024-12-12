#!/bin/env python3

"""

 A 2D vertical scrolling platformer game.

 CONTROLS
 --------
 left and right arrow keys to move horizontaly.
 space key to continue playing.

"""

from settings import *
from level import Level

class Game:

    def __init__( self ):
        pg.init()
        self.surface = pg.display.set_mode( (SCREEN_W, SCREEN_H) )
        pg.display.set_caption( "PLATFORM" )
        self.clock = pg.time.Clock()

        self.level = Level()

    def run( self ):
        while( True ):

            if( not self.level.isOver ):
                self.level.run()
            else:
                self.level.game_over()

                # Continues the game
                key = pg.key.get_pressed()
                if( key[KEY_CONT] ):
                    del self.level
                    self.level = Level()
            
            for event in pg.event.get():
                if( event.type == QUIT ):
                    pg.quit()
                    sys.exit()
                                
            pg.display.update()
            self.clock.tick(60)

Game().run()
