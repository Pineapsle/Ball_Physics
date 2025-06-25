# trail.py

from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from collections import deque

class Trail(Widget):
    def __init__(self, max_length=20, color=(1, 0.4, 0), **kwargs):
        super().__init__(**kwargs)
        self.points = deque(maxlen=max_length)
        self.trail_color = color

    def update(self, pos):
        self.points.append((pos.x, pos.y))
        self.canvas.clear()
        with self.canvas:
            Color(*self.trail_color)
            if len(self.points) >= 2:
                Line(points=[p for pt in self.points for p in pt], width=2)
