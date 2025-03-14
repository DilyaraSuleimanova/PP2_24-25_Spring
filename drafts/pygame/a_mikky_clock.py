import pygame
import math
import time

pygame.init()

# Screen setup
width, height = 500, 500
center = (width // 2, height // 2)

screen = pygame.display.set_mode((width, height))

# Load clock face
img_clock = pygame.image.load("clock.png")
img_clock = pygame.transform.scale(img_clock, (width, height))

# Load hands
img_min_hand = pygame.image.load("min_hand.png")
img_sec_hand = pygame.image.load("sec_hand.png")

# Scale hands (ensure proper sizes)
img_min_hand = pygame.transform.scale(img_min_hand, (150, 20))  # Longer minute hand
img_sec_hand = pygame.transform.scale(img_sec_hand, (180, 15))  # Longer second hand

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(img_clock, (0, 0))  # Draw clock face

    # Get current time
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate angles (6 degrees per unit)
    min_angle = minutes * 6  
    sec_angle = seconds * 6  

    # Rotate hands
    rotate_min_hand = pygame.transform.rotate(img_min_hand, -min_angle)
    rotate_sec_hand = pygame.transform.rotate(img_sec_hand, -sec_angle)

    # Get new hand positions to align rotation around the clock center
    rect_min = rotate_min_hand.get_rect(center=center)
    rect_sec = rotate_sec_hand.get_rect(center=center)

    # Draw hands
    screen.blit(rotate_min_hand, rect_min.topleft)
    screen.blit(rotate_sec_hand, rect_sec.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
