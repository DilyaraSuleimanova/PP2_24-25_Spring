import pygame
import math
import time

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load and scale images
img_clock = pygame.image.load("clock.png")
img_clock = pygame.transform.scale(img_clock, (WIDTH, HEIGHT))

img_min_hand = pygame.image.load("min_hand.png")
img_min_hand = pygame.transform.scale(img_min_hand, (450, 250))  # Adjusted size

img_sec_hand = pygame.image.load("sec_hand.png")
img_sec_hand = pygame.transform.scale(img_sec_hand, (300, 250))  # Thinner second hand

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw clock face
    screen.blit(img_clock, (0, 0))

    # Get current time
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate angles
    min_angle = (minutes % 60) * 6  # Each minute moves 6 degrees
    sec_angle = (seconds % 60) * 6  # Each second moves 6 degrees

    # Rotate and position minute hand
    rotate_min_hand = pygame.transform.rotate(img_min_hand, -min_angle)
    rect_min = rotate_min_hand.get_rect(center=CENTER)

    # Rotate and position second hand
    rotate_sec_hand = pygame.transform.rotate(img_sec_hand, -sec_angle)
    rect_sec = rotate_sec_hand.get_rect(center=CENTER)

    # Draw hands
    screen.blit(rotate_min_hand, rect_min.topleft)
    screen.blit(rotate_sec_hand, rect_sec.topleft)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
