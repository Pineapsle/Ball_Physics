# sound.py

from kivy.core.audio import SoundLoader

def load_sounds():
    return {
        "coin": SoundLoader.load("boink_sound.wav"),
        #"boost": SoundLoader.load("boost.wav"),
    }

def play(sound_obj):
    if sound_obj:
        sound_obj.stop()
        sound_obj.play()
