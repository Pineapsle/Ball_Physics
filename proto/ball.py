import pygame
from config import *

# Ball class
class Ball:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)                       # Position vector (x, y)
        self.vel = pygame.Vector2(0,0)                        # Velocity vector (vx, vy)   
        self.acc = pygame.Vector2(0, 0)                       # Acceleration vector (ax, ay)   
        self.radius = BALL_RADIUS
        self.dragging = False
        self.prev_mouse_pos = pygame.Vector2(x, y)
    
    def apply_gravity(self):
        self.acc.y = GRAVITY                                  # Applies constant downward acceleration due to gravity

    def update(self, dt):
        if not self.dragging:
            self.vel += self.acc * dt                                 # Velocity changes due to acceleration
            self.pos += self.vel * dt + 0.5 * self.acc * dt * dt      # Position changes due to velocity      Other formula: self.pos += self.vel * dt             

            # Collision with ground
            if self.pos.y + self.radius >= HEIGHT:
                self.pos.y = HEIGHT - self.radius
                self.vel.y *= -RESTITUTION
            
            # Collision with ceiling
            if self.pos.y - self.radius <= 0:
                self.pos.y = self.radius
                self.vel.y *= -RESTITUTION
            
            # Collision with walls
            if self.pos.x - self.radius <= 0:
                self.pos.x = self.radius
                self.vel.x *= -RESTITUTION

            if self.pos.x + self.radius >= WIDTH:
                self.pos.x = WIDTH - self.radius
                self.vel.x *= -RESTITUTION
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 100, 100), (int(self.pos.x), int(self.pos.y)), self.radius)
        if self.dragging:
            pygame.draw.line(screen, (0, 255, 0), self.prev_mouse_pos, pygame.mouse.get_pos(), 2)
    
    def start_drag(self, mouse_pos):
        if (self.pos - mouse_pos).length() <= self.radius:
            self.dragging = True
            self.prev_mouse_pos = mouse_pos
    
    def end_drag(self, mouse_pos):
        if self.dragging:
            drag_vector = mouse_pos - self.prev_mouse_pos
            self.vel = drag_vector * 3 # Scaling throw power when thrown 
            self.dragging = False
    
    def boost(self):
        if self.vel.length() > 0:
            boost_vector = self.vel.normalize() * 300  # Apply a boost of magnitude 300 in the direction of movement
            self.vel += boost_vector
        else:
            self.vel = pygame.Vector2(0, -300)  # If stationary, boost upwards
    
    def reset(self):
        self.vel = pygame.Vector2(0, 0)                       # Reset velocity
        self.acc = pygame.Vector2(0, 0)                       # Reset acceleration
        self.pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)