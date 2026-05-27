# mysprite_vs().py
# Importing and linking other files needed to run the game
import pygame
import time
import sys
import random
from imagelist import ImageList
from settings_testfile import*

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

class Mysprite(pygame.sprite. Sprite)
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
    def move(self):

    def update(self):
    
    def animate(self):

    def collide(self):

    def get_x(self):
    
    def get_y(self):

    def get_w(self):

    def get_h(self):

    def get_rect(self):

class MySprite():
    def __init__(self,x,y,w,h,images,screen):
        self.xd=0
        self.yd=0
        self._images = images
        self._screen = screen
        self._current_frame = 0
        self._start_frame = 0
        self._end_frame = 0
        self._delay = -1
        self._move_delay = 0
        self._next_move = time.time()
        self._repeat= False

        if x>=0 and x<=SCREEN_WIDTH:
            self._x = x
        else:
            print("INVALID")
            exit(0)

        if y>=0 and y<=SCREEN_HEIGHT:
            self._y = y
        else:
            print("INVALID")
            exit(0)

        if w>=0 and w<=SCREEN_WIDTH:
            self._w = w
        else:
            print("INVALID")
            exit(0)

        if h>=0 and h<=SCREEN_HEIGHT:
            self._h = h
        else:
            print("INVALID")
            exit(0)

    def get_rect(self):
        return(self._x,self._y,self._w, self._h)
    
    def get_x(self):
        return self._x
    def set_x(self,x):
        if x>=0 and x< SCREEN_WIDTH:
            self._x= x
        elif x<0:
            self._x=0
        else:
            self._x= SCREEN_WIDTH -1
    def get_y(self):
        return self._y
    def set_y(self,y):
        if y>=0 and y< SCREEN_HEIGHT:
            self._y= y
        elif y<0:
            self._y=0
        else:
            self._x= SCREEN_WIDTH -1
    x=property(get_x,set_x)
    y=property(get_y,set_y)
  
    def set_pos(self,x,y):
        self.set_x(x)
        self.set_y(y)

    def move(self,x_delta=None, y_delta=None, delay=None):
        #changing the vector if required
        if not x_delta is None:
            self.xd= x_delta
        if not y_delta is None:
            self.yd= y_delta
        if not y_delta is None:
            self.yd= y_delta

        if not delay == self._move_delay:
            self._move_delay = delay
        if time.time() > self._next_move:
            self.set_x(self._x+self._xd)
            self.set_y(self._y+self._yd)
            self._next_move = self._next_move + self._move_delay

    def collide (self, x, y, w, h):
        if x>self._x + self._w or\
           y > self._y + self._h or\
           x + w < self._x or \
            y + h < self._y:
            return False
        else:
            return True
    
    
    def get_y(self):
        return self._y

    def set_x(self,y):
        self._y= y
        

    def set_animation(self, start_frame, end_frame=0, delay=0, repeat=1):
        if start_frame >= 0 and start_frame < len(self._images.images):
            self._start_frame = start_frame
            self._current_frame = start_frame  # Initialize to start frame

        if end_frame >= 0 and end_frame < len(self._images.images) and start_frame <= end_frame:
            self._end_frame = end_frame
        else:
            self._end_frame = len(self._images.images) - 1  # Default to last frame

        if delay >= 0:
            self._delay = delay

        if repeat:
            self._repeat = True
        else:
            self._repeat = False

        self._next_frame = time.time() + delay


    def animate(self, reset_animation=False):
        if reset_animation == True:
            self._current_frame = self._start_frame
        else:
            if time.time() > self._next_frame:
                self._current_frame += 1
                # Keep frame within bounds
                if self._current_frame > self._end_frame:
                    if self._repeat:
                        self._current_frame = self._start_frame
                    else:
                        self._current_frame = self._end_frame  # Clamp to last frame
                self._next_frame = self._next_frame + self._delay

    def get_rect(self):
        return pygame.Rect(self._x, self._y, self._h, self._w)

    def draw(self):
        # Safety check: ensure current_frame is valid
        if self._current_frame >= len(self._images.images):
            self._current_frame = len(self._images.images) - 1
        self._screen.blit(self._images.images[self._current_frame], self.get_rect())

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
