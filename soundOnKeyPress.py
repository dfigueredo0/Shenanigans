from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pynput.keyboard import KeyCode, Listener

pygame.mixer.init()

sound = pygame.mixer.Sounds('.mp3')
# 26 sounds for alphabet + 10sounds for numbers + 1 for spacebar + 1 for enter + 1 for backspace, total = 39 Sound effects
# 8 chennels on default can increase w/ pygame.mixer.set_num_channel(num)
# do effect = pygame.mixer.Sound('filename.extension') as they use the channels
# for true chaos create 39 channels and create chanel objects (pygame.mixer.Channel(channel#)) and call channel.play(sound)

def on_press(key):
    try:
        if key == KeyCode(char='a'):
            sound.play()
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()