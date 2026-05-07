import pygame
import json
pygame.init()

#Setup window
SCREEN_WIDTH=1000
SCREEN_HEIGHT=720

snake_size=3
window=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
try:
    game_icon=pygame.image.load('snake_icon.png')
    pygame.display.set_icon(game_icon)
except FileNotFoundError:
    print("This file cannot be loaded")
    
def draw_checkerboard(surface):
    green1= (0, 200, 0)
    green2= (0, 150, 0)
    ts= 50 #This is the tile size

    for y in range(0,SCREEN_HEIGHT, ts):
        for x in range(0, SCREEN_WIDTH, ts):
            if (x//ts+y//ts)% 2==0:
                color= green1
            else:
                color=green2
            pygame.draw.rect(surface, color, (x,y,ts,ts)) # Drawing the rectangle

running=True
clock=pygame.time.Clock
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
            
    draw_checkerboard(window)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
