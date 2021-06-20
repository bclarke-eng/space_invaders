import pygame

# This file contains constants for game set-up and display

# Creating Sprite groups
invaders_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
invader_bullet_group = pygame.sprite.Group()


# Sets up the screen for the game to be played in
game_over = 0
edge_hit = False
window_height = 600
window_width = 800

screen = pygame.display.set_mode((window_width, window_height))
background = pygame.image.load("images/background.jpg")