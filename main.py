import pygame
import sys
from config import *
from ball import Ball
from coin import Coin
from trail import Trail

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Physics Engine")
clock = pygame.time.Clock()


# Initialize ball and coin
ball = Ball(WIDTH // 2, HEIGHT // 2)
coin = Coin(70, 45) 
trail = Trail(50, (255, 100, 0))  


last_relocate_time = pygame.time.get_ticks()


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
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:                                # Reset the ball when 'R' is pressed
                ball.reset()
    
    screen.fill((30, 30, 30))

    ball.apply_gravity()
    ball.update(dt)
    ball.draw(screen)

    # Draw the basket from the Coin class
    coin.draw(screen)

    # Relocate the coin every 5 seconds
    current_time = pygame.time.get_ticks()
    if current_time - last_relocate_time > 5000:  # 10,000 milliseconds = 10 seconds
        coin.relocate(WIDTH, HEIGHT)
        last_relocate_time = current_time

    # Check if the ball has scored
    if coin.check_score(ball): 
        print("Coin Collected!")
        ball.boost()
        coin.relocate(WIDTH, HEIGHT)
    
    #trail.update(ball.pos, ball.velocity)
    #trail.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()