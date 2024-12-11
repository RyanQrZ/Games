from settings import *

class Player( pg.sprite.Sprite ):

    def __init__( self ):
        super().__init__()
        self.image = PLAYER_IMG
        self.rect = self.image.get_rect( midbottom = (100, SCREEN_H - 32) )
        self.flip = False

        # Movement values
        self.vel_y = 0
        self.grav_acc = 0.6
        self.jump_val = -15
        self.horizontal_dist = 5

    def move( self, platforms ):
        key_pressed = pg.key.get_pressed()
        delta_x, delta_y, scroll = 0, 0, 0
        
        if( key_pressed[K_LEFT] ):
            delta_x = -self.horizontal_dist
            self.flip = True
        if( key_pressed[K_RIGHT] ):
            delta_x = self.horizontal_dist
            self.flip = False

        # Gravity mechanic
        self.vel_y += self.grav_acc
        delta_y += self.vel_y

        # Collision detection
        for platform in platforms:
            # Check if there is an overlap
            hit = platform.rect.colliderect( self.rect.x,
                                             self.rect.y + delta_y,
                                             self.image.get_width(),
                                             self.image.get_height() ) 
            if( hit ):
                # Check if if comming from top
                if( self.rect.bottom < platform.rect.centery ):
                    if( self.vel_y > 0 ):
                        self.rect.bottom = platform.rect.top
                        self.delta_y = 0
                        self.jump()

        # Boundaries
        if self.rect.left > SCREEN_W:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = SCREEN_W

        # Check if player bounced threshold
        if( self.rect.top <= THRESH ):
            # Check if jumping
            if( self.vel_y < 0 ):
                scroll = -delta_y

        # Update position
        self.rect.y += delta_y + scroll
        self.rect.x += delta_x

        return scroll

    def jump( self ):
        self.vel_y = self.jump_val
#--------------------------------------------------------------------
class Platform( pg.sprite.Sprite ):

    def __init__( self, group, pos_x, pos_y ):
        super().__init__( group )
        random_plat = random.randint(0, 2)
        self.image = pg.transform.scale_by( PLATFORM_IMG[random_plat], 1.25 )
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    # Update vertical position
    def update( self, scroll ):
        self.rect.y += scroll
