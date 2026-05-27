# main.py
# Importing and linking other files needed to run the game
import pygame
import json
from imagelist import ImageList
from mysprite_vs2 import MySprite
from settings import*
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
    def play(self):
        difficulty_menu = DifficultyMenu(SCREEN)
        selected_speed = difficulty_menu.show()
        
        if selected_speed is None:
            return

        try:
            food = Food(200, 200, FOOD_W, FOOD_H, IMAGE_PATH, SCREEN)
            test_imagelist = ImageList(SPRITE_FILES, TEST_W, TEST_H)
            snake_segments = [MySprite(100, 100, TEST_W, TEST_H, test_imagelist, SCREEN)]
            game_loop = GameLoop(snake_segments, food, SCREEN, test_imagelist, selected_speed)
            game_loop.run()
        except Exception as e:
            print(f"Error starting game: {e}")

    def customize(self):
        print("Customize button clicked")

    def info(self):
        print("This is a simple snake game")
        print(f"Sprite files location: {SPRITE_FILES}")
        print(f"Image path: {IMAGE_PATH}")

    def exit_game(self):

        return "exit"

        pygame.display.flip()
        clock.tick(60) # FPS
pygame.quit()
