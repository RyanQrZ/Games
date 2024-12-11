#!/bin/env python3

"""

 A 2D vertical scrolling platformer game.

 CONTROLS
 --------
 left and right arrow keys to move horizontaly.

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
            
            self.isOver = self.level.game_over()
            for event in pg.event.get():
                if( event.type == QUIT or self.isOver ):
                    pg.quit()
                    sys.exit()

            self.level.run()
                                
            pg.display.update()
            self.clock.tick(60)

Game().run()
