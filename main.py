import pygame
import sys

# pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Physics Engine")
clock = pygame.time.Clock()

# Constants
GRAVITY = 980               # pixels per second^2
RESTITUTION = 0.8           # energy loss on bounce
BALL_RADIUS = 20            # Size of the ball
FPS = 60                    # Frames per second

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
    
# Initialize ball
ball = Ball(WIDTH // 2, HEIGHT // 2)

# Main loop
running = True

while running:
    dt = clock.tick(FPS) / 1000.0 # Convert milliseconds to seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball.start_drag(pygame.mouse.get_pos())
        
        elif event.type == pygame.MOUSEBUTTONUP:
            ball.end_drag(pygame.Vector2(pygame.mouse.get_pos()))
    
    screen.fill((30, 30, 30))

    ball.apply_gravity()
    ball.update(dt)
    ball.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()