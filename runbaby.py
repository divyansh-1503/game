import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Subway Surfers Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player properties
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 20
player_speed = 10
player = pygame.Rect(player_x, player_y, player_size, player_size)

# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 7
obstacles = []

# Score
score = 0
font = pygame.font.SysFont("Arial", 30)

def draw_player():
    pygame.draw.rect(screen, BLUE, player)

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

def spawn_obstacle():
    x_pos = random.choice([WIDTH // 4, WIDTH // 2, 3 * WIDTH // 4])
    obstacle = pygame.Rect(x_pos, -obstacle_height, obstacle_width, obstacle_height)
    obstacles.append(obstacle)

def move_obstacles():
    global score
    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            score += 1

def check_collision():
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            return True
    return False

# Game loop
running = True
spawn_timer = 0
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed

    # Spawn obstacles
    spawn_timer += 1
    if spawn_timer > 30:  # Adjust frequency
        spawn_obstacle()
        spawn_timer = 0

    # Move obstacles
    move_obstacles()

    # Check collision
    if check_collision():
        print(f"Game Over! Final Score: {score}")
        running = False

    # Draw everything
    draw_player()
    draw_obstacles()

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
