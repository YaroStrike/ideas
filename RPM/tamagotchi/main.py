# Pet Position
import pygame
import sys
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
background_image = pygame.image.load('room.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
pet_images = {
    'happy': pygame.image.load('redd-normal.png'),
    'hungry': pygame.image.load('redd-hungry.png'),
    'sleeping': pygame.image.load('redd-sleep.png'),
    'food': pygame.image.load('food.png'),
    'food2': pygame.image.load('food2.png'),
    'sad': pygame.image.load('redd-sad.png')
}

# Scale pet images
for key in pet_images:
    pet_images[key] = pygame.transform.scale(pet_images[key], (560, 446))

# Initial pet stats
happiness = 100
hunger = 100
energy = 100
pet_state = 'happy'
pet_position = (WIDTH // 2 - 280, HEIGHT // 2 - 223)  # Initial pet position

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tamagotchi')

# Food position
food_position = (WIDTH // 2 - 50, HEIGHT - 200)
food_visible = True

dragging_food = False

# Font for displaying stats
font = pygame.font.Font(None, 48)

# Button positions
sleep_button = pygame.Rect(WIDTH - 200, HEIGHT // 2 - 50, 180, 40)
wake_button = pygame.Rect(WIDTH - 200, HEIGHT // 2 + 10, 180, 40)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if sleep_button.collidepoint(event.pos):
                    pet_state = 'sleeping'
                elif wake_button.collidepoint(event.pos):
                    happiness = max(happiness - 5, 0)
                elif food_visible and food_position[0] <= event.pos[0] <= food_position[0] + 100 and food_position[1] <= event.pos[1] <= food_position[1] + 100:
                    hunger = min(hunger + 20, 100)
                    food_visible = False
                elif food_visible and food_position[0] <= event.pos[0] <= food_position[0] + 100 and food_position[1] <= event.pos[1] <= food_position[1] + 100:
                    dragging_food = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging_food = False
                if not food_visible:
                    food_visible = True
                    food_position = (WIDTH // 2 - 50, HEIGHT - 200)

        if dragging_food:
            food_position = event.pos  # Move food with cursor

    # Decrease stats over time
    happiness = max(happiness - 3 / FPS, 0)
    hunger = max(hunger - 2 / FPS, 0)
    if pet_state == 'sleeping':
        energy = max(energy + 3 / FPS, 100)
    energy = max(energy - 1 / FPS, 0)

    # Update screen
    if energy < 20:
        pet_state = 'sleeping'
    elif hunger < 50:
        pet_state = 'hungry'
    elif happiness < 50:
        pet_state = 'sad'
    else:
        pet_state = 'happy'

    screen.blit(background_image, (0, 0))
    screen.blit(pet_images[pet_state], pet_position)  # Use pet_position here
    
    # Draw food
    if food_visible:
        screen.blit(pet_images['food'], food_position)
    else:
        screen.blit(pet_images['food2'], food_position)

    # Draw buttons
    pygame.draw.rect(screen, WHITE, sleep_button)
    pygame.draw.rect(screen, WHITE, wake_button)
    screen.blit(font.render('Sleep', True, BLACK), (sleep_button.x + 50, sleep_button.y + 5))
    screen.blit(font.render('Wake', True, BLACK), (wake_button.x + 50, wake_button.y + 5))
    
    # Display stats with black outline
    def draw_text_with_outline(text, font, color, outline_color, position):
        text_surface = font.render(text, True, color)
        outline_surface = font.render(text, True, outline_color)
        screen.blit(outline_surface, (position[0] - 2, position[1] - 2))
        screen.blit(outline_surface, (position[0] + 2, position[1] - 2))
        screen.blit(outline_surface, (position[0] - 2, position[1] + 2))
        screen.blit(outline_surface, (position[0] + 2, position[1] + 2))
        screen.blit(text_surface, position)

    draw_text_with_outline(f'Happiness: {int(happiness)}', font, WHITE, BLACK, (10, 130))
    draw_text_with_outline(f'Hunger: {int(hunger)}', font, WHITE, BLACK, (10, 170))
    draw_text_with_outline(f'Energy: {int(energy)}', font, WHITE, BLACK, (10, 210))
    
    pygame.display.flip()
    clock.tick(FPS)
