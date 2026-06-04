import pygame
import sys
from imagelist import ImageList
from mysprite import Mysprite, GameLoop, Food, DifficultyMenu
from settings import *
import json
import os
pygame.init()

# Allowing the user to enter their name 
class PlayerNameInput:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 35)
        self.title_font = pygame.font.Font(None, 45)  
        self.player_name = ""
        self.max_chars = 15
        self.input_rect = pygame.Rect(self.screen.get_width() // 2 - 200, self.screen.get_height() // 2, 400, 50)
        self.button_rect = pygame.Rect(self.screen.get_width() // 2 - 75, self.screen.get_height() // 2 + 100, 150, 50)
        self.hovered = False
    
    def show(self):
        inputting= True

        while inputting:
            mouse_pos = pygame.mouse.get_pos()
            self.hovered = self.button_rect.collidepoint(mouse_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(self.player_name) > 0:
                            inputting = False
                    elif len(self.player_name) < self.max_chars:
                        # Check if the user only enters alphabetic letters and numberics
                        if event.unicode.isalnum() or event.unicode == " ":
                            self.player_name += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.button_rect.collidepoint(event.pos):
                        if len(self.player_name) > 0:
                            inputting = False
                        self.screen.fill((50, 50, 50))

            title_text = self.title_font.render("Enter Your Name", True, white)
            self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 50))
            
            pygame.draw.rect(self.screen, white, self.input_rect, 2)
            name_text = self.font.render(self.player_name, True, white)
            self.screen.blit(name_text, (self.input_rect.x + 10, self.input_rect.y + 12))
            
            button_color = (100, 255, 100) if self.hovered else (100, 100, 100)
            pygame.draw.rect(self.screen, button_color, self.button_rect)
            pygame.draw.rect(self.screen, white, self.button_rect, 2)
            
            button_text = self.font.render("Start", True, black)
            self.screen.blit(button_text, (self.button_rect.x + 40, self.button_rect.y + 10))
            
            pygame.display.flip()
            clock.tick(60)
        
        return self.player_name

# Create the Gameover screen, customize screen, information screen
