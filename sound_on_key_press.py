from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pynput.keyboard import Listener
from sound_mapping import key_sounds

def play_sound_on_key_press():
    pygame.mixer.init()

    sounds = {key : pygame.mixer.Sound(path) for key, path in key_sounds.items()}
    def on_press(key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                sound = sounds.get(key.char)
                if sound:
                    sound.play()
            if key in sounds:
                sounds[key].play()
        except Exception as e:
            print(f"Error: {e}")

    def on_release(key):
        pass

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()