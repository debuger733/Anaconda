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
# module testing code
if __name__ == "__main__":
    SPRITE_FILES = "images\\sprite\\sprite"

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Mysprite")

    test_imagelist = ImageList(SPRITE_FILES, TEST_W, TEST_H)
    sprite_list = []
    sprite_list.append(MySprite(TEST_X, TEST_Y, TEST_W, TEST_H, test_imagelist, screen))
    sprite_list[-1].set_animation(0, 3, 0.5)
    
    class Food(MySprite):
        def __init__(self, x, y, w, h, images, screen):
            super().__init__(x, y, w, h, ImageList(images, w, h), screen)
    
        def draw(self):
            self._screen.blit(self._images.images[0], self.get_rect())

    def food_collision(head, food):
        head_rect = head.get_rect()
        food_rect = food.get_rect()
        return head_rect.colliderect(food_rect)

    def grow_snake(segments, SPRITE_FILES, screen):
        last = segments[-1]
        new_segment = MySprite(last.get_x(), last.get_y(), 16, 16, ImageList(SPRITE_FILES, 16, 16), screen)
        segments.append(new_segment)

    food = Food(200, 200, 16, 16, "images\\sprite\\egg.jpg", screen)
    snake_segments = [MySprite(100, 100, 16, 16, test_imagelist, screen)]

    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                if food_collision(snake_segments[0], food):
                    grow_snake(snake_segments, SPRITE_FILES, screen)
                food.set_pos(random.randint(0, 984), random.randint(0, 704))
            
        for sprite in sprite_list:
            sprite.animate()
            sprite.draw()
            
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
