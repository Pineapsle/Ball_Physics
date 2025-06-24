import pygame
import threading

pygame.init()
pygame.mixer.init()

def play_sound_background():
    def play_sound():
        sound = pygame.mixer.Sound("boink_sound.wav")
        sound.play()
        # No need to wait; let the sound play asynchronously

    # Launch the sound playback in a daemon thread
    thread = threading.Thread(target=play_sound, daemon=True)
    thread.start()


# How this works (threading):
# 1. The 'play_sound_background' function creates a new thread that plays the sound.
# 2. The thread is marked as a daemon, meaning it will not block the program from exiting.
# 3. The sound will play in the background while the main program continues to run.
# 4. This allows the sound to be played without interrupting the main game loop or other operations.