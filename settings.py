import pygame

# settings.py
# Setting up the window
# Initial window size and brightness
SCREEN_WIDTH= 800
SCREEN_HEIGHT=600
DEFAULTS = {"brightness": 100}
MIN_BRIGHTNESS=1
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# Size of each tile
ts=20

# Color codes
green1= (0, 200, 0)
green2= (0, 150, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Initial Sprite size and speed
snake_size= 30
PLAYER_SPEED = 5

# Size of sprites used
TEST_X = 50
TEST_Y = 50
TEST_W = 64
TEST_H = 64

# Properties of the main menu buttons
button_width = 100
button_height = 50
button_spacing = 50
button_color = (200, 200, 200)
button_text_color = (0, 0, 0)

# Image file paths 
SPRITE_FILES = "code/images/sprite/sprite"
IMAGE_PATH = "code/images/sprite/egg.jpg"

# Food
FOOD_W = 30
FOOD_H = 30