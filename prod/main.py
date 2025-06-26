# main.py

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from ball import Ball
from coin import Coin
from config import *
from trail import Trail
from sound import load_sounds, play

class GameScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball = Ball()
        self.coin = Coin()
        self.trail = Trail()
        self.add_widget(self.trail)
        self.add_widget(self.coin)
        self.add_widget(self.ball)

        self.sounds = load_sounds()
        self.last_coin_time = 0

        Clock.schedule_interval(self.update, 1.0 / FPS)

    def update(self, dt):
        self.ball.update(dt)
        self.trail.update(self.ball.pos_vec)

        # Relocate every 10 seconds
        if self.last_coin_time > 10:
            self.coin.relocate()
            self.last_coin_time = 0
        self.last_coin_time += dt

        if self.coin.check_score(self.ball):
            play(self.sounds["coin"])
            self.ball.boost()
            self.coin.relocate()
            self.last_coin_time = 0

    def on_touch_down(self, touch):
        self.ball.on_touch_down(touch)

    def on_touch_up(self, touch):
        self.ball.on_touch_up(touch)

class BallApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    BallApp().run()
