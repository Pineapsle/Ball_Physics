from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.vector import Vector
from kivy.core.window import Window
from config import *
import math

class Ball(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = BALL_RADIUS
        self.pos_vec = Vector(Window.width / 2, Window.height / 2)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, -GRAVITY)
        self.dragging = False
        self.prev_touch = None

        with self.canvas:
            self.color = Color(1, 0.4, 0.4)
            self.circle = Ellipse(pos=(self.pos_vec.x - self.radius, self.pos_vec.y - self.radius), size=(2*self.radius, 2*self.radius))

        self.size = (2*self.radius, 2*self.radius)
        self.center = self.pos_vec

    def update(self, dt):
        self.vel += self.acc * dt
        self.pos_vec += self.vel * dt + 0.5 * self.acc * dt * dt

        # Floor
        if self.pos_vec.y - self.radius <= 0:
            self.pos_vec.y = self.radius
            self.vel.y *= -RESTITUTION

        # Ceiling
        if self.pos_vec.y + self.radius >= Window.height:
            self.pos_vec.y = Window.height - self.radius
            self.vel.y *= -RESTITUTION

        # Left wall
        if self.pos_vec.x - self.radius <= 0:
            self.pos_vec.x = self.radius
            self.vel.x *= -RESTITUTION

        # Right wall
        if self.pos_vec.x + self.radius >= Window.width:
            self.pos_vec.x = Window.width - self.radius
            self.vel.x *= -RESTITUTION

        self.circle.pos = (self.pos_vec.x - self.radius, self.pos_vec.y - self.radius)

    def on_touch_down(self, touch):
        self.vel -= self.vel * 0.5 # Reduce velocity to make it easier to drag
        self.dragging = True
        self.prev_touch = Vector(*touch.pos)

    def on_touch_up(self, touch):
        if self.dragging:
            self.acc = Vector(0, -GRAVITY)
            drag_vector = Vector(*touch.pos) - self.prev_touch
            self.vel = drag_vector * 3
            self.dragging = False

    def boost(self):
        if self.vel.length() > 0:
            self.vel += self.vel.normalize() * 300
        else:
            self.vel = Vector(0, 300)

    def reset(self):
        self.pos_vec = Vector(Window.width / 2, Window.height / 2)
        self.vel = Vector(0, 0)
        