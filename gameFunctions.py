import random

from spaceInvaderSpriteClasses import Invader, Invader_Bullet
from gameConstants import invaders_group, invader_bullet_group, screen, window_width

# This file contains functions that create and update game elements

rows = 3
columns = 10

def create_invaders():
    for row in range(rows):
        for col in range(columns):
            invader = Invader(100 + col * 65, 80 + row * 50) # Positions gained via trial and error
            invaders_group.add(invader)

def remove_invaders(invaders):
    for invader in invaders:
        invader.kill()

def create_invader_bullet():
    attacking_invader = random.choice(invaders_group.sprites())
    invader_bullet = Invader_Bullet(attacking_invader.rect.centerx, attacking_invader.rect.centery)
    invader_bullet_group.add(invader_bullet)

def update_game(invaders, invader_bullets, player, player_bullet):
    invaders.update()
    invader_bullets.update()
    player.update()
    player_bullet.update()

    invaders.draw(screen)
    invader_bullets.draw(screen)
    player.draw(screen)
    player_bullet.draw(screen)

def check_for_edge(invaders_group, player, edge_hit, game_over):
    for invader in invaders_group.sprites():
            if invader.gameover == 1:
                game_over = 1
                break
            else:
                # Space Invaders automatically move side-to-side
                if invader.rect.left <= 0 or invader.rect.right >= window_width:
                    edge_hit =  True
        
    if edge_hit:
        for invader in invaders_group.sprites():
            invader.move_direction_x *= -1
            if invader.rect.bottom <= player.rect.top:
                invader.rect.y += 3
        edge_hit = False
    
    return game_over
        
