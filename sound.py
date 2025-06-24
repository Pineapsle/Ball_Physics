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

# Example usage in your game loop:
# play_sound_background()  # Call this whenever you want to play the sound
