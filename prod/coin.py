from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color, Line
from kivy.vector import Vector
from kivy.core.window import Window
from kivy.clock import Clock
import random
import math

class Coin(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = 15
        self.angle = 0  # used for spin animation
        self.pos_vec = Vector(100, 100)

        with self.canvas:
            self.color = Color(1, 1, 0)
            self.ellipse = Line(circle=(self.pos_vec.x, self.pos_vec.y, self.radius), width=2)

        Clock.schedule_interval(self.animate_spin, 1/60)

    def animate_spin(self, dt):
        # Update angle to simulate spin
        self.angle += dt * 3  # adjust speed here
        scale = abs(math.cos(self.angle))  # oscillate width to simulate spinning

        # Update position and scaled ellipse
        w = self.radius * scale
        h = self.radius

        self.ellipse.circle = (self.pos_vec.x, self.pos_vec.y, w)
        self.ellipse.width = 2

    def relocate(self):
        margin = self.radius + 10
        self.pos_vec = Vector(
            random.randint(margin, Window.width - margin),
            random.randint(margin, Window.height - margin)
        )

    def check_score(self, ball):
        return Vector(*ball.pos_vec).distance(self.pos_vec) < (ball.radius + self.radius)
