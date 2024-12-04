from settings import *

class Player( pg.sprite.Sprite ):

    def __init__( self ):
        super().__init__()
        self.surf = pg.image.load( PLAYER_IMG )
        self.rect = self.surf.get_rect()

        # Movement values
        self.acc_val = 0.5
        self.fric = -0.16
        self.jumping = False
        self.jump_val = -13

        # Vectors
        self.x_pos = random.randint( 0, SCREEN_W - 16)
        self.pos = vec( (self.x_pos, SCREEN_H - TILE_SIZE) )
        self.vel = vec(0, 0)

    def move( self ):
        self.acc = vec( 0, 0.6 )
        key_pressed = pg.key.get_pressed()

        if( key_pressed[K_LEFT] ):
            self.acc.x = -self.acc_val
        if( key_pressed[K_RIGHT] ):
            self.acc.x = self.acc_val

        # Physic formulas
        self.acc.x += self.vel.x * self.fric
        self.vel += self.acc
        self.pos += self.vel + self.acc * 0.5

        # Boundaries
        if self.pos.x > SCREEN_W:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_W

        self.rect.midbottom = self.pos

    def jump( self, ground ):
            hits = pg.sprite.spritecollide( self, ground, False )
            
            if( hits and not self.jumping ):
                self.jumping = True
                self.vel.y = self.jump_val
                
            if( self.jumping and not hits ):
                self.vel.y = self.jump_val
                self.jumping = False

    def update( self, platforms ):
        
        # Collision detection
        hits = pg.sprite.spritecollide( self, platforms, False )

        if( self.vel.y > 0 ):
            if( hits ):
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
                self.jumping = False
            
        self.move()
        
class Platform( pg.sprite.Sprite ):

    def __init__( self, group, initial_h, final_h ):
        super().__init__( group )

        # Dimensions
        self.surf_w = random.randint(2, 8) * TILE_SIZE
        self.surf = pg.Surface( (self.surf_w, TILE_SIZE) )
        
        self.surf.fill( (0, 0, 0) )

        # Position
        self.coord_x = random.randint( 0, SCREEN_W - self.surf.get_width() )
        self.coord_y = random.randint( initial_h, final_h )
        self.rect = self.surf.get_rect( topleft = (self.coord_x, self.coord_y) )
