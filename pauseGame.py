import pygame
from gameConstants import window_width, window_height, screen

def pause_game():

    font = pygame.font.SysFont("lucidaconsole",115)
    text = font.render("PAUSED", 1, (255,255,255))
    screen.blit(text, ( (window_width/2 - text.get_width()/2), (window_width/2 - text.get_height()/2)))

    pause = True
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = False
                
        pygame.display.update()