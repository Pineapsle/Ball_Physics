import pygame
import random

class Coin:
    def __init__(self, x, y, radius=10):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 255, 0)  # Yellow
        self.thickness = 5  # Ring thickness

        # Define a pygame.Rect for collision detection (bounding box of the circle)
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.thickness)

    def check_score(self, ball):
        distance = (ball.pos - pygame.Vector2(self.x, self.y)).length()
        if distance <= self.radius + ball.radius:
            return True
        return False

    def relocate(self, screen_width, screen_height):
        margin = self.radius + 10  # To avoid spawning too close to the edge
        self.x = random.randint(margin, screen_width - margin)
        self.y = random.randint(margin, screen_height - margin)
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
