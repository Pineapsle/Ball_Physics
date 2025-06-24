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


# Home Screen with two buttons: Classic and Coin
def home_screen():
    font = pygame.font.Font(None, 74)
    title_text = font.render("Ball Physics Engine", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))

    button_font = pygame.font.Font(None, 56)
    classic_text = button_font.render("Classic Mode", True, (0, 0, 0))
    coin_text = button_font.render("Coin Mode", True, (0, 0, 0))

    # Button rectangles
    classic_rect = pygame.Rect(WIDTH // 2 - 170, HEIGHT // 2, 340, 70)
    coin_rect = pygame.Rect(WIDTH // 2 - 170, HEIGHT // 2 + 100, 340, 70)

    global mode

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if classic_rect.collidepoint(mouse_pos):
                    mode = "classic"
                    return
                elif coin_rect.collidepoint(mouse_pos):
                    mode = "coin"
                    return

        screen.fill((30, 30, 30))
        screen.blit(title_text, title_rect)

        # Draw buttons
        pygame.draw.rect(screen, (200, 200, 200), classic_rect)
        pygame.draw.rect(screen, (200, 200, 0), coin_rect)

        # Draw button text centered
        screen.blit(classic_text, classic_text.get_rect(center=classic_rect.center))
        screen.blit(coin_text, coin_text.get_rect(center=coin_rect.center))

        pygame.display.flip()

home_screen()  # Show the home screen before starting the game

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

    if mode == "coin":
        # Draw the basket from the Coin class
        coin.draw(screen)

        # Relocate the coin every 5 seconds
        current_time = pygame.time.get_ticks()
        if current_time - last_relocate_time > 7000:  # 10,000 milliseconds = 10 seconds
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