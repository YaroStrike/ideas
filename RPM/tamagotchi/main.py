import pygame
import sys
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Load images
pet_images = {
    'happy': pygame.image.load('redd-normal.png'),
    'hungry': pygame.image.load('redd-hungry.png'),
    'sleeping': pygame.image.load('redd-sleep.png')
}

# Initial pet stats
happiness = 100
hunger = 100
energy = 100

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tamagotchi')

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Example interactions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pet the Tamagotchi
                happiness = min(happiness + 10, 100)
            elif event.key == pygame.K_f:  # Feed the Tamagotchi
                hunger = min(hunger + 20, 100)
            elif event.key == pygame.K_s:  # Sleep the Tamagotchi
                energy = min(energy + 30, 100)
            elif event.key == pygame.K_w:  # Wake the Tamagotchi
                happiness = max(happiness - 5, 0)

    # Update screen
    screen.fill(WHITE)
    if energy < 20:
        pet_state = 'sleeping'
    elif hunger < 50:
        pet_state = 'hungry'
    else:
        pet_state = 'happy'
    
    screen.blit(pet_images[pet_state], (WIDTH // 2 - pet_images[pet_state].get_width() // 2, HEIGHT // 2 - pet_images[pet_state].get_height() // 2))
    
    pygame.display.flip()
    clock.tick(FPS)
