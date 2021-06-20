import pygame
from gameConstants import screen
from gameFunctions import remove_invaders, create_invaders

# This file defines functions that are called once a game over condition has been satisfied

def new_game_user_dead(new_game_button, mouse_position, player_group, invaders_group, game_over, background, player):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if new_game_button.isOver(mouse_position):
                game_over = 0
                background = pygame.image.load("images/background.jpg")
                remove_invaders(invaders_group.sprites())
                create_invaders()
                player.health_remaining = player.health_start
                player_group.add(player)
    
    return player, game_over, background

def new_game_invaders_dead(new_game_button, mouse_position, player, game_over, background):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if new_game_button.isOver(mouse_position):
                game_over = 0
                background = pygame.image.load("images/background.jpg")
                create_invaders()
                player.health_remaining = player.health_start
    
    return player, game_over, background


def check_game_over(game_over, new_game_button, player, player_group, invaders_group, background):
    pos = pygame.mouse.get_pos()

    if game_over == 1:
        game_over = 1
        background = pygame.image.load("images/gameover_background.jpg")
        new_game_button.draw(screen)
        player, game_over, background = new_game_user_dead(new_game_button, pos, player_group, invaders_group, game_over, background, player)
    elif len(invaders_group) == 0:
        game_over = 2
        background = pygame.image.load("images/congratulations.jpg")
        new_game_button.draw(screen)
        player, game_over, background = new_game_invaders_dead(new_game_button, pos, player, game_over, background)
    
    return player, game_over, background 
