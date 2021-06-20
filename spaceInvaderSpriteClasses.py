import pygame
from gameConstants import player_group, player_bullet_group, invaders_group, screen, window_width, window_height

# This file contains the main classes used during the space invaders game

class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/spaceInvaders.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_direction_x = 1
        self.gameover = 0
    
    def update(self):
        # Get the invaders to move horizontally
        self.rect.x += self.move_direction_x

        # Checks if invaders have reached the user on the screen
        if self.rect.bottom > (player.rect.top + 10):
            self.gameover = 1

class Invader_Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/invader_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def update(self):
        # Bullets move vertically
        self.rect.y += 2

        # Removes user health when a bullet strikes them
        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            player.health_remaining -= 10

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/user.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.last_shot = pygame.time.get_ticks()
        self.health_start = 50
        self.health_remaining = 50
    
    def update(self):
        speed = 3
        cooldown = 200
        gameover = 0
        current_time = pygame.time.get_ticks()
        key = pygame.key.get_pressed()

        # Draw player health bar
        pygame.draw.rect(screen, (0,0,0), (self.rect.x, self.rect.bottom, self.rect.width, 10))

        if self.health_remaining >  0:
            # Draw remaining heallth if player still alive
            pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, self.rect.bottom, int(self.rect.width * (self.health_remaining/self.health_start)), 10))
        elif self.health_remaining == 0:
            # User is dead when they run out of health
            self.kill()
            gameover = 1

        # Keys are used to control the user
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        
        elif key[pygame.K_RIGHT] and self.rect.right < window_width:
            self.rect.x += speed
        
        elif key[pygame.K_SPACE] and current_time - self.last_shot > cooldown:
            bullet = Player_Bullet(self.rect.centerx, self.rect.top)
            player_bullet_group.add(bullet)
            self.last_shot = pygame.time.get_ticks()
        
        return gameover

class Player_Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/user_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def update(self):
        # User shoots bullets upwards
        self.rect.y -= 5

        # An invader is killed when hit by a bullet
        if pygame.sprite.spritecollide(self, invaders_group, True):
            self.kill()

# Create player at centre of the screen
player = Player(int(window_width/2), window_height - 100) # Positions gained via trial and error
