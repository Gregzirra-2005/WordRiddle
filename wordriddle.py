import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set title of the window
pygame.display.set_caption("Word Riddle Game")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the font
font = pygame.font.Font(None, 36)

# Define the riddles and answers
riddles = [
    {"question": "What has keys but can't open locks?", "answer": "A piano"},
    {"question": "What has many keys, but can't even open a single door?", "answer": "A computer keyboard"},
    {"question": "What gets wetter the more it dries?", "answer": "A towel"}
]

# Select a random riddle
current_riddle = random.choice(riddles)

# Define the input box
input_box = pygame.Rect(100, 100, 400, 50)
user_input = ""

# Load the background image
background = pygame.image.load("bg2.jpg")

# Scale the background image to fit the screen
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Check if the answer is correct
                if user_input.lower() == current_riddle["answer"].lower():
                    print("Correct!")
                else:
                    print("Incorrect. Try again!")
                user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    # Clear the screen
    screen.fill(WHITE)

    # Draw the background image
    screen.blit(background, (0, 0))

    # Draw the riddle
    riddle_text = font.render(current_riddle["question"], True, BLACK)
    screen.blit(riddle_text, (100, 50))

    # Draw the input box
    pygame.draw.rect(screen, BLACK, input_box, 2)
    input_box_text = font.render(user_input, True, BLACK)
    screen.blit(input_box_text, (input_box.x + 10, input_box.y + 10))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()