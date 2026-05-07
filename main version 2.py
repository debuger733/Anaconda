import pygame
import json
from imagelist import ImageList
from mysprite import MySprite
pygame.init()

#Setup window
SCREEN_WIDTH=1000
SCREEN_HEIGHT=720
TEST_X = 50
TEST_Y = 50
TEST_W = 64
TEST_H = 64
TEST_FILES = "images\\test\\test"

snake_size=3
window=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

test_imagelist = ImageList(TEST_FILES, TEST_W, TEST_H)
    # set up any sprites we're using
sprite_list = []
sprite_list.append(MySprite(TEST_X, TEST_Y, TEST_W, TEST_H, test_imagelist, window))
sprite_list[-1].set_animation( 0 , 3, 0.5)

try:
    game_icon=pygame.image.load('snake_icon.png')
    pygame.display.set_icon(game_icon)
except FileNotFoundError:
    print("This file cannot be loaded")
    
def draw_checkerboard(surface):
    green1= (0, 200, 0)
    green2= (0, 150, 0)
    ts= 20  #This is the tile size

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
        for sprite in sprite_list:
            sprite.draw()
        pygame.display.flip()
        clock.tick(60) # FPS
pygame.quit()
