import pygame
from settings import*
import json
import os
pygame.init()

# Allowing the user to enter their name 
class GameOverScreen:
    def __init__(self, screen, score, player_name, difficulty):
        self.screen = screen
        self.score = score
        self.player_name = player_name
        self.difficulty = difficulty
        self.font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 30)
        self.button_font = pygame.font.Font(None, 35) 
        self.button_rects = {}
        self.hovered_button = None
        self.update_button_positions()
        self.save_score()
    
    def update_button_positions(self):
        self.button_rects = {}
        button_y = self.screen.get_height() // 2 + 150
        button_width = 150
        button_height = 50
        button_spacing = 30
        
        try_again_x = self.screen.get_width() // 2 - button_width - button_spacing // 2
        self.button_rects["try_again"] = pygame.Rect(try_again_x, button_y, button_width, button_height)
        
        menu_x = self.screen.get_width() // 2 + button_spacing // 2
        self.button_rects["menu"] = pygame.Rect(menu_x, button_y, button_width, button_height)
    
    def save_score(self):
        history_file = "game_history.json"
        
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
        else:
            history = []
        
        entry = {
            "player_name": self.player_name,
            "score": self.score,
            "difficulty": self.difficulty
        }
        history.append(entry)
        
        with open(history_file, 'w') as f:
            json.dump(history, f, indent=2)
        
        print(f"Score saved: {self.player_name} - Score: {self.score} - Difficulty: {self.difficulty}")
    
    def show(self):
        waiting = True
        clock = pygame.time.Clock()
        
        while waiting:
            mouse_pos = pygame.mouse.get_pos()
            self.hovered_button = None
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.button_rects["try_again"].collidepoint(event.pos):
                            return "try_again"
                        elif self.button_rects["menu"].collidepoint(event.pos):
                            return "menu"
            
            for button_key, button_rect in self.button_rects.items():
                if button_rect.collidepoint(mouse_pos):
                    self.hovered_button = button_key
                    break
            
            self.screen.fill((33, 89, 77))
            
            gameover_text = self.font.render("GAME OVER", True, red)
            self.screen.blit(gameover_text, (self.screen.get_width() // 2 - gameover_text.get_width() // 2, 50))
            
            player_text = self.small_font.render(f"Player: {self.player_name}", True, white)
            self.screen.blit(player_text, (self.screen.get_width() // 2 - player_text.get_width() // 2, 150))
            
            score_text = self.small_font.render(f"Score: {self.score}", True, yellow)
            self.screen.blit(score_text, (self.screen.get_width() // 2 - score_text.get_width() // 2, 200))
            
            difficulty_text = self.small_font.render(f"Difficulty: {self.difficulty}", True, white)
            self.screen.blit(difficulty_text, (self.screen.get_width() // 2 - difficulty_text.get_width() // 2, 250))
            
            for button_key, button_rect in self.button_rects.items():
                is_hovered = self.hovered_button == button_key
                button_color = (100, 205, 100) if is_hovered else (100, 100, 100)
                pygame.draw.rect(self.screen, button_color, button_rect)
                pygame.draw.rect(self.screen, white, button_rect, 2)
                
                button_label = "Try Again" if button_key == "try_again" else "Menu"
                text = self.button_font.render(button_label, True, black)
                self.screen.blit(text, (button_rect.x + 20, button_rect.y + 8))
            
            pygame.display.flip()
            clock.tick(60)

class ExitConfirmDialog:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 35)
        self.title_font = pygame.font.Font(None, 45)
        
        self.button_rects = {}
        self.hovered_button = None
        self.update_button_positions()
    
    def update_button_positions(self):
        self.button_rects = {}
        
        button_y = self.screen.get_height() // 2 + 80
        button_width = 120
        button_height = 50
        button_spacing = 30
        
        yes_x = self.screen.get_width() // 2 - button_width - button_spacing // 2
        self.button_rects["yes"] = pygame.Rect(yes_x, button_y, button_width, button_height)
        
        no_x = self.screen.get_width() // 2 + button_spacing // 2
        self.button_rects["no"] = pygame.Rect(no_x, button_y, button_width, button_height)
    
    def show(self):
        waiting = True
        clock = pygame.time.Clock()
        
        while waiting:
            mouse_pos = pygame.mouse.get_pos()
            self.hovered_button = None
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.button_rects["yes"].collidepoint(event.pos):
                            return True
                        elif self.button_rects["no"].collidepoint(event.pos):
                            return False
            
            for button_key, button_rect in self.button_rects.items():
                if button_rect.collidepoint(mouse_pos):
                    self.hovered_button = button_key
                    break
            
            SCREEN.fill((33, 89, 77))
            
            question_text = self.title_font.render("Are you sure you want to exit?", True, white)
            self.screen.blit(question_text, (self.screen.get_width() // 2 - question_text.get_width() // 2, 100))
            
            for button_key, button_rect in self.button_rects.items():
                is_hovered = self.hovered_button == button_key
                button_color = (100, 255, 100) if is_hovered else (100, 100, 100)
                pygame.draw.rect(self.screen, button_color, button_rect, border_radius= 15)
                pygame.draw.rect(self.screen, white, button_rect, 2, border_radius= 15)
                
                button_label = "Yes" if button_key == "yes" else "No"
                text = self.font.render(button_label, True, black)
                self.screen.blit(text, (button_rect.x + 35, button_rect.y + 10))
            
            pygame.display.flip()
            clock.tick(60)

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
                self.screen.fill((33, 89, 77))

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

class InstructionsScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 40)
        self.small_font = pygame.font.Font(None, 20)
        
        # Instructions for the user
        self.instructions = [
            "HOW TO PLAY",
            "",
            "OBJECTIVE:",
            "Guide your snake to eat food and grow longer.",
            "Avoid hitting the boundaries or yourself!",
            "",
            "CONTROLS:",
            "Arrow Keys - Move the snake (Up, Down, Left, Right)",
            "",
            "GAMEPLAY:",
            "- Eat the red food to grow and gain points",
            "- Each food eaten increases your score by 1",
            "- The snake grows by TWO segments per food",
            "- Hitting boundaries or yourself ends the game",
            "",
            "DIFFICULTY:",
            "Easy: Slower movement speed",
            "Medium: Normal movement speed",
            "Hard: Faster movement speed",
            "",
            "CUSTOMIZATION:",
            "- Choose snake color: Green, Blue, Orange, Red",
            "- Choose background: Grey/White, Green, Black/White",
            "",
            "Press SPACE or Click to return to menu"
        ]
    
    def show(self):
        showing = True
        clock = pygame.time.Clock()
        scroll_offset = 0
        max_scroll = max(0, len(self.instructions) * 25 - self.screen.get_height() + 100)
        
        while showing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        showing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    showing = False
                elif event.type == pygame.MOUSEWHEEL:
                    scroll_offset -= event.y * 10
                    scroll_offset = max(0, min(scroll_offset, max_scroll))
            
            self.screen.fill((50, 50, 50))
            
            y_pos = 30 - scroll_offset
            for line in self.instructions:
                if line == "HOW TO PLAY":
                    text = self.title_font.render(line, True, yellow)
                elif line.isupper() and line:
                    text = self.font.render(line, True, white)
                else:
                    text = self.small_font.render(line, True, (200, 200, 200))
                
                if y_pos > -20 and y_pos < self.screen.get_height():
                    self.screen.blit(text, (40, y_pos))
                y_pos += 25
            
            # Allowing the user to exit this page by either pressing SPACE or CLICK
            hint = self.small_font.render("Press SPACE or Click to return to menu", True, (150, 150, 150))
            self.screen.blit(hint, (self.screen.get_width() - hint.get_width() - 20, self.screen.get_height() - 30))
            
            pygame.display.flip()
            clock.tick(60)
        
        return True
        
class CustomizeScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.title_font = pygame.font.Font(None, 40)
        
        self.snake_colors = ["green", "blue", "orange", "red"]
        self.backgrounds = ["grey_white", "green_dark", "black_white"]
        self.background_labels = ["Grey/White", "Green", "Black/White"]
        
        self.selected_snake_color = "green"
        self.selected_background = "grey_white"
        
        self.button_rects = {}
        self.hovered_button = None
        self.done_rect = None
        self.update_button_positions()
    
    def update_button_positions(self):
        self.button_rects = {}
        
        color_y = 100
        for i, color in enumerate(self.snake_colors):
            x = 100 + i * 150
            self.button_rects[f"snake_{color}"] = pygame.Rect(x, color_y, 120, 50)
        
        bg_y = 250
        for i, bg in enumerate(self.backgrounds):
            x = 100 + i * 200
            self.button_rects[f"bg_{bg}"] = pygame.Rect(x, bg_y, 150, 50)
        
        self.done_rect = pygame.Rect(self.screen.get_width() // 2 - 75, 400, 150, 50)
    
    def show(self):
        customizing = True
        clock = pygame.time.Clock()
        
        while customizing:
            mouse_pos = pygame.mouse.get_pos()
            self.hovered_button = None
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None, None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return None, None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button_key, button_rect in self.button_rects.items():
                            if button_rect.collidepoint(event.pos):
                                if button_key.startswith("snake_"):
                                    self.selected_snake_color = button_key.split("_")[1]
                                elif button_key.startswith("bg_"):
                                    self.selected_background = button_key.split("_", 1)[1]
                        
                        if self.done_rect.collidepoint(event.pos):
                            customizing = False
            
            for button_key, button_rect in self.button_rects.items():
                if button_rect.collidepoint(mouse_pos):
                    self.hovered_button = button_key
                    break
            
            if self.done_rect.collidepoint(mouse_pos):
                self.hovered_button = "done"
            
            self.screen.fill((33, 89, 77))
            
            title = self.title_font.render("Customize Game", True, white)
            self.screen.blit(title, (self.screen.get_width() // 2 - title.get_width() // 2, 20))
            
            color_label = self.font.render("Snake Color:", True, white)
            self.screen.blit(color_label, (20, 70))
            
            for color in self.snake_colors:
                button_key = f"snake_{color}"
                button_rect = self.button_rects[button_key]
                is_selected = color == self.selected_snake_color
                is_hovered = self.hovered_button == button_key
                
                bg_color = (100, 255, 100) if is_selected else ((120, 120, 120) if is_hovered else (100, 100, 100))
                pygame.draw.rect(self.screen, bg_color, button_rect)
                pygame.draw.rect(self.screen, white, button_rect, 2)
                
                text = self.font.render(color.capitalize(), True, black)
                self.screen.blit(text, (button_rect.x + 10, button_rect.y + 12))
            
            bg_label = self.font.render("Background:", True, white)
            self.screen.blit(bg_label, (20, 220))
            
            for i, bg in enumerate(self.backgrounds):
                button_key = f"bg_{bg}"
                button_rect = self.button_rects[button_key]
                is_selected = bg == self.selected_background
                is_hovered = self.hovered_button == button_key
                
                bg_color = (100, 255, 100) if is_selected else ((120, 120, 120) if is_hovered else (100, 100, 100))
                pygame.draw.rect(self.screen, bg_color, button_rect)
                pygame.draw.rect(self.screen, white, button_rect, 2)
                
                text = self.font.render(self.background_labels[i], True, black)
                self.screen.blit(text, (button_rect.x + 15, button_rect.y + 12))
            
            done_color = (100, 255, 100) if self.hovered_button == "done" else (100, 100, 100)
            pygame.draw.rect(self.screen, done_color, self.done_rect)
            pygame.draw.rect(self.screen, white, self.done_rect, 2)
            
            done_text = self.font.render("Done", True, black)
            self.screen.blit(done_text, (self.done_rect.x + 50, self.done_rect.y + 12))
            
            hint = self.font.render("Press ESC to cancel", True, (150, 150, 150))
            self.screen.blit(hint, (20, self.screen.get_height() - 40))
            
            pygame.display.flip()
            clock.tick(60)
        
        return self.selected_snake_color, self.selected_background

            # No changes made 25/06/2026
