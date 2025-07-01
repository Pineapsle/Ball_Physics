# trail.py

import random
import time
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from collections import deque

class Trail(Widget):
    def __init__(self, max_length=10, **kwargs):
        super().__init__(**kwargs)
        self.points = deque(maxlen=max_length)
        self.trail_color = self.random_color()
        self.last_color_change = time.time()  # Timestamp of last color change

    def random_color(self):
        return (random.random(), random.random(), random.random(), 0.20)    # 0.2 is the opacity

    def update(self, pos):
        self.points.append((pos.x, pos.y))

        # Check if 1.3 seconds have passed
        if time.time() - self.last_color_change > 1.3:
            self.trail_color = self.random_color()
            self.last_color_change = time.time()

        self.canvas.clear()

        # Draw the trail
        with self.canvas:
            Color(*self.trail_color)
            if len(self.points) >= 2:
                flattened_points = []
                for pt in self.points:
                    flattened_points.extend(pt)
                # Draw a line connecting all points in the deque
                Line(points=flattened_points, width=2)
