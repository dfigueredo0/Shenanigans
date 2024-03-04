import threading
from sound_on_key_press import play_sound_on_key_press
from volume_always_on import set_volume_to_maximum, stop_event

def main():
    volume_thread = threading.Thread(target=set_volume_to_maximum, daemon=True)
    volume_thread.start()

    try:
        play_sound_on_key_press()
    finally:
        stop_event.set()
        volume_thread.join()


if __name__ == "__main__":
    main()