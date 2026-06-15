import pygame
# settings.py
# Setting up the window
# Initial window size and brightness
SCREEN_WIDTH= 800
SCREEN_HEIGHT=600
DEFAULTS = {"brightness": 100, "snake_color": "green", "background": "grey_white"}
MIN_BRIGHTNESS=1
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# Menu screen background color
mixed_color=pygame.color.Color(100,100,100)

# Logo dimensions
LOGO_W = 350
LOGO_H = 100
LOGO_PATH= "images/logo.png"

# Color codes
green1= (0, 200, 0)
green2= (0, 150, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grey=  (128, 128, 128)
black= (0, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
grey = (128, 128, 128)
dark_grey = (64, 64, 64)

# Background checkerboard colors
CHECKERBOARD_TILE_SIZE = 50
BACKGROUND_MODES = {
    "grey_white": {"color1": grey, "color2": white},
    "green_dark": {"color1": green1, "color2": green2},
    "black_white": {"color1": black, "color2": white}
}

# Initial Sprite size and speed
snake_size= 30
PLAYER_SPEED = 5

# Snake color mapping
SNAKE_COLORS = {
    "green": green1,
    "blue": blue,
    "orange": orange,
    "red": red
}

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
button_hover_color = (220, 220, 220)

# Image file paths 
SPRITE_FILES = "images/sprite/sprite"
IMAGE_PATH = "images/sprite/egg.jpg"

# Food
FOOD_W = 50
FOOD_H = 50

# Clock
clock = pygame.time.Clock()