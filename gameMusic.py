from pygame import mixer

# This file contains code that allows background music to play

def initiate_game_music():
    mixer.init()

    mixer.music.load("images/game.wav")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)