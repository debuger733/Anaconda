# main.py
# Importing and linking other files needed to run the game
import pygame
import json
from imagelist import ImageList
from mysprite import MySprite
from settings_testfile import*
pygame.init()

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 25)
        
        self.menu_options = [
            {"label": "Play", "command": self.play},
            {"label": "Customize", "command": self.customize},
            {"label": "Info", "command": self.info},
            {"label": "Exit", "command": self.exit_game}
        ]
        self.button_rects = []
    def update_button_positions(self):
        self.button_rects = []
        BUTTON_X = (self.screen.get_width() - button_width) // 2
        button_count = len(self.menu_options)
        button_total_height = button_count * (button_height + button_spacing)
        button_y_offset = (self.screen.get_height() - button_total_height) // 2

        for i in range(button_count):
            button_rect = pygame.Rect(
                BUTTON_X, 
                button_y_offset + i * (button_height + button_spacing), 
                button_width, 
                button_height
            )
            self.button_rects.append(button_rect)

    def show_menu(self):
        self.update_button_positions()


window=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    # set up any sprites we're using
try:
    game_icon=pygame.image.load('snake_icon.png')
    pygame.display.set_icon(game_icon)
except FileNotFoundError:
    print("This file cannot be loaded")
    
def draw_checkerboard(surface):

    for y in range(0,SCREEN_HEIGHT, ts):
        for x in range(0, SCREEN_WIDTH, ts):
            if (x//ts+y//ts)% 2==0:\
                color= green1
            else:
                color=green2
        pygame.draw.rect(surface, color, (x,y,ts,ts)) # Drawing the rectangle


running=True
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
        draw_checkerboard(window)
        pygame.display.flip()
        clock.tick(60) # FPS
pygame.quit()
