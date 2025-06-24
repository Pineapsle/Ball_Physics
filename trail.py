import pygame
import math

class Trail:
    def __init__(self, max_length=50, color=(255, 100, 0)):
        self.points = []
        self.max_length = max_length
        self.color = color

    def update(self, pos, velocity):
        speed = math.hypot(*velocity)
        size = max(5, min(30, int(speed * 2)))
        self.points.append({'pos': pos, 'size': size})
        if len(self.points) > self.max_length:
            self.points.pop(0)

    def draw(self, surface):
        for i, point in enumerate(self.points):
            alpha = int(255 * (i + 1) / len(self.points))
            trail_color = (*self.color, alpha)
            s = pygame.Surface((point['size']*2, point['size']*2), pygame.SRCALPHA)
            pygame.draw.circle(s, trail_color, (point['size'], point['size']), point['size'])
            surface.blit(s, (point['pos'][0] - point['size'], point['pos'][1] - point['size']))

