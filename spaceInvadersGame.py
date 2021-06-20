import pygame
from pygame import mixer

from gameOverFunctions import check_game_over
from buttonClasses import Button
from gameMusic import initiate_game_music
from pauseGame import pause_game
from gameFunctions import check_for_edge, create_invaders, create_invader_bullet, update_game
from spaceInvaderSpriteClasses import player_group, player, screen
from gameConstants import invaders_group, invader_bullet_group, player_bullet_group, game_over, edge_hit, background

# This file contains the code that intialises the game and updates the game state

pygame.init()

# Setting up game
clock = pygame.time.Clock()
timer = pygame.time.get_ticks()

pygame.display.set_caption("Space Invaders")
initiate_game_music()

newGameButton = Button((0, 0, 153), 300, 450, 200, 75, 'NEW GAME')

create_invaders()
player_group.add(player)


# Begin game loop
# Updates the game screen whilst game window is open
game = True
while game:

    clock.tick(60) # Add delay to updating movement of aliens so they don't move too fast
    seconds = (pygame.time.get_ticks() - timer) / 1000
    screen.blit(background, (0,0)) # (0,0) is top left corner of screen
    
    # Game is not over
    if game_over == 0:

        update_game(invaders_group, invader_bullet_group, player_group, player_bullet_group)
        game_over = check_for_edge(invaders_group, player, edge_hit, game_over)

        # If player has been killed
        if player.update() == 1:
            game_over = 1

        # Ensures that invaders only fire bullets after a cooldown period
        if seconds > 2:
            create_invader_bullet()
            timer = pygame.time.get_ticks()

    # Checks to see if a game over condition has been met
    player, game_over, background = check_game_over(game_over, newGameButton, player, player_group, invaders_group, background)

    # See if game window has been closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            mixer.music.stop()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause_game()

    pygame.display.update()

pygame.quit()
