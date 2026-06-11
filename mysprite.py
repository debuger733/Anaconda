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
        self.SCREEN.blit(self.image, (self.x, self.y))

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
        BUTTON_X = (self.screen.get_width()-150//2)
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
            segment.snake_color = SNAKE_COLORS.get(snake_color, green1)

    def draw_checkerboard(self):
        bg_config = BACKGROUND_MODES.get(self.background_mode, BACKGROUND_MODES["grey_white"])
        color1 = bg_config["color1"]
        color2 = bg_config["color2"]
        
        tile_size = CHECKERBOARD_TILE_SIZE
        for x in range(0, self.SCREEN.get_width(), tile_size):
            for y in range(0, self.SCREEN.get_height(), tile_size):
                rect = pygame.Rect(x, y, tile_size, tile_size)
                if ((x // tile_size) + (y // tile_size)) % 2 == 0:
                    pygame.draw.rect(self.SCREEN, color1, rect)
                else:
                    pygame.draw.rect(self.SCREEN, color2, rect)

    def run(self):
        game_running = True
        movement_counter = 0
        
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake_segments[0].move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake_segments[0].move(1, 0)
                    elif event.key == pygame.K_UP:
                        self.snake_segments[0].move(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.snake_segments[0].move(0, 1)

            movement_counter += 1
            if movement_counter >= (10 - self.difficulty_speed):
                movement_counter = 0
                
                self.snake_segments[0].update()
                
                self.position_history.insert(0, (self.snake_segments[0].rect.x, self.snake_segments[0].rect.y))
                
                for i in range(1, len(self.snake_segments)):
                    if i < len(self.position_history):
                        self.snake_segments[i].rect.x, self.snake_segments[i].rect.y = self.position_history[i]
                
                if len(self.position_history) > len(self.snake_segments) + 5:
                    self.position_history.pop()
            
            for segment in self.snake_segments:
                segment.animate(self.sprite_imagelist)

            if self.food_collision():
                self.score += 1
                print(f"Food eaten! Score: {self.score}")
                self.add_segment()
                self.add_segment()
                new_x = (random.randint(0, (SCREEN_WIDTH // TEST_W) - 1)) * TEST_W
                new_y = (random.randint(0, (SCREEN_HEIGHT // TEST_H) - 1)) * TEST_H
                self.food.set_pos(new_x, new_y)

            if self.snake_collision():
                print(f"Game Over! Snake hit itself. Score: {self.score}")
                game_running = False

            if self.check_bounds():
                print(f"Game Over! Out of bounds. Score: {self.score}")
                game_running = False

            self.draw_checkerboard()
            self.food.draw()
            
            for segment in self.snake_segments:
                colored_image = pygame.Surface((segment.get_w(), segment.get_h()))
                colored_image.fill(segment.snake_color)
                self.SCREEN.blit(colored_image, (segment.rect.x, segment.rect.y))
            
            score_text = f"Score: {self.score} | Size: {len(self.snake_segments)}"
            score_surface = self.font.render(score_text, True, black)
            
            scoreboard_bg = pygame.Surface((score_surface.get_width() + 20, score_surface.get_height() + 10))
            scoreboard_bg.set_alpha(200)
            scoreboard_bg.fill(white)
            
            self.SCREEN.blit(scoreboard_bg, (10, 10))
            self.SCREEN.blit(score_surface, (20, 15))

            pygame.display.flip()
            self.clock.tick(60)

    def add_segment(self):
        if len(self.snake_segments) > 0:
            last_segment = self.snake_segments[-1]
            new_segment = Mysprite(
                last_segment.get_x(),
                last_segment.get_y(),
                last_segment.get_w(),
                last_segment.get_h(),
                self.sprite_imagelist,
                self.SCREEN,
                self.difficulty_speed,
                self.snake_color
            )
            
            self.snake_segments.append(new_segment)
            print(f"Snake grew! New length: {len(self.snake_segments)}")

    def food_collision(self):

        head_rect = self.snake_segments[0].get_rect()
        food_rect = self.food.get_rect()
        
        return head_rect.colliderect(food_rect)

    def snake_collision(self):
        head_x = self.snake_segments[0].rect.x
        head_y = self.snake_segments[0].rect.y
        
        min_collision_index = min(8, max(4, len(self.snake_segments) // 2))
        
        for i in range(min_collision_index, len(self.snake_segments)):
            segment = self.snake_segments[i]
            segment_x = segment.rect.x
            segment_y = segment.rect.y
            
            if head_x == segment_x and head_y == segment_y:
                print(f"Self collision detected: Head at ({head_x}, {head_y}) hit segment {i}")
                return True
        
        return False

    def check_bounds(self):
        head = self.snake_segments[0]
        if (head.get_x() < 0 or 
            head.get_x() + head.get_w() > SCREEN_WIDTH or
            head.get_y() < 0 or 
            head.get_y() + head.get_h() > SCREEN_HEIGHT):
            return True
        return False