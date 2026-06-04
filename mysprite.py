# mysprite_vs().py
# Importing and linking other files needed to run the game
import pygame
import time
import sys
import random
from imagelist import ImageList
from settings import*

class Food:
    def __init__(self, x, y, width, height, image_path, SCREEN):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.SCREEN = SCREEN
        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.smoothscale(self.image, [width, height])
        except pygame.error as e:
            print(f"Error loading food image: {e}. Using colored rectangle instead.")
            self.image =pygame.Surface([width, height])
            self.image.fill(red)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.SCREEN.blit(self.images, (self.x, self.y))

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect

class Mysprite(pygame.sprite. Sprite):
    def __init__(self, x, y, width, height, sprite_imagelist, SCREEN, speed=5):
        super().__init__()
        self.image = sprite_imagelist.get_image(0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._w = width
        self._h = height
        self.SCREEN = SCREEN
        self.speed = speed
        self.direction = (0, 0)
        self.prev_x = x
        self.prev_y = y
        
    def move(self, dx, dy):
        if (dx, dy) != (0, 0):
            if not (self.direction[0] == -dx and self.direction[1] == -dy):
                self.direction = (dx, dy)

    def update(self):

        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        
        dx, dy = self.direction
        self.rect.x += dx * self.tile_size
        self.rect.y += dy * self.tile_size

    def animate(self, sprite_imagelist):
        self.image = sprite_imagelist.get_image(0)

    def collide(self, other_rect):
        return self.rect.colliderect(other_rect)

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_w(self):
        return self._w

    def get_h(self):
        return self._h

    def get_rect(self):
        return self.rect

class DifficultyMenu:
    # Menu to select the difficulty of the game
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 35)
        self.title_font = pygame.font.Font(None, 50)
        
        self.difficulties = [
            {"label": "Easy", "speed": 3},
            {"label": "Medium", "speed": 5},
            {"label": "Hard", "speed": 7}
        ]
        
        self.button_rects = []
        self.selected_difficulty = None
        self.hovered_button = None
        self.update_button_positions()

    def update_button_positions(self):
        # Position of the buttons
        BUTTON_X = (self.screen.get_wdith()-150//2)
        button_count =  len(self.difficulties)
        button_total_height = button_count * (60 + 30)
        button_y_offset = (self.screen.get_height() - button_total_height) // 2

        for i in range(button_count):
            button_rect = pygame.Rect(
                BUTTON_X, 
                button_y_offset + i * 90, 
                150, 
                60
            )
            self.button_rects.append(button_rect)
    
    def show(self):
        selecting= True
        while selecting:
            mouse_pos = pygame.mouse.get_pos()
            self.hovered_button = None
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i, button_rect in enumerate(self.button_rects):
                            if button_rect.collidepoint(event.pos):
                                self.selected_difficulty = self.difficulties[i]["speed"]
                                selecting = False
                                break
            
            for i, button_rect in enumerate(self.button_rects):
                if button_rect.collidepoint(mouse_pos):
                    self.hovered_button = i
                    break
            
            self.screen.fill((50, 50, 50))
            
            title = self.title_font.render("Select Difficulty", True, white)
            title_rect = title.get_rect(center=(self.screen.get_width() // 2, 50))
            self.screen.blit(title, title_rect)

            for i, button_rect in enumerate(self.button_rects):
                button_color = (120, 120, 120) if i == self.hovered_button else (100, 100, 100)
                pygame.draw.rect(self.screen, button_color, button_rect)
                pygame.draw.rect(self.screen, white, button_rect, 3)
                
                text = self.font.render(self.difficulties[i]["label"], True, white)
                text_rect = text.get_rect(center=button_rect.center)
                self.screen.blit(text, text_rect)
            
                pygame.display.flip()
                clock.tick(60)
            return self.selected_difficulty
class GameLoop:
    def __init__(self, snake_segments, food, SCREEN, sprite_imagelist, difficulty_speed, snake_color="green", background_mode="grey_white"):
        self.snake_segments = snake_segments
        self.food = food
        self.SCREEN = SCREEN
        self.sprite_imagelist = sprite_imagelist
        self.clock = pygame.time.Clock()
        self.difficulty_speed = difficulty_speed
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.snake_color = snake_color
        self.background_mode = background_mode

        self.position_history = [(snake_segments[0].rect.x, snake_segments[0].rect.y)]

        for segment in self.snake_segments:
            segment.speed = difficulty_speed
            segment.snake_color= SNAKE_COLORS.get(snake_color, green1)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit() # To do: test the gameloop fixing errors on the main
