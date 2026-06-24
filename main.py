# main.py
# Importing and linking other files needed to run the game
import pygame
from imagelist import ImageList
from mysprite import Food, Mysprite, DifficultyMenu, GameLoop
from button_info import PlayerNameInput, GameOverScreen, InstructionsScreen, CustomizeScreen, ExitConfirmDialog
from settings import*
pygame.init()

# Creating the menu screen
pygame.init()
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 25)
        self.logo_loaded = False
        self.logo = None
        self.logo_rect = None
        
        try:
            self.logo = pygame.image.load(LOGO_PATH)
            self.logo = pygame.transform.smoothscale(self.logo, (LOGO_W, LOGO_H))
            self.logo_rect = self.logo.get_rect(center=(self.screen.get_width() // 2, 100))
            self.logo_loaded = True
        except Exception as e:
            print(f"Error loading logo: {e}")
            self.logo_loaded = False
        
        self.menu_options = [
            {"label": "Play", "command": self.play},
            {"label": "Customize", "command": self.customize},
            {"label": "Info", "command": self.info},
            {"label": "Exit", "command": self.exit_game}
        ]
        
        self.button_rects = []
        self.hovered_button = None
        self.selected_snake_color = "green"
        self.selected_background = "grey_white"

    def update_button_positions(self):
        self.button_rects = []
        BUTTON_X = (self.screen.get_width() - button_width) // 2
        button_count = len(self.menu_options)
        button_total_height = button_count * (button_height + button_spacing)
        button_y_offset = (self.screen.get_height() - button_total_height) // 2 + 100

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
        name_input = PlayerNameInput(SCREEN)
        player_name = name_input.show()
        
        if player_name is None:
            return
        
        difficulty_menu = DifficultyMenu(SCREEN)
        selected_speed = difficulty_menu.show()
        
        if selected_speed is None:
            return
        
        # Speed of the snake depending on the difficulty
        difficulty_map = {3: "Easy", 5: "Medium", 7: "Hard"}
        difficulty_label = difficulty_map.get(selected_speed, "Medium")
        
        try:
            food = Food(200, 200, FOOD_W, FOOD_H, IMAGE_PATH, SCREEN)
            test_imagelist = ImageList(SPRITE_FILES, TEST_W, TEST_H)
            start_x = (SCREEN_WIDTH // 2 // 60) * 60
            start_y = (SCREEN_HEIGHT // 2 // 60) * 60
            snake_segments = [Mysprite(start_x, start_y, TEST_W, TEST_H, test_imagelist, SCREEN, selected_speed, self.selected_snake_color)]
            game_loop = GameLoop(snake_segments, food, SCREEN, test_imagelist, selected_speed, self.selected_snake_color, self.selected_background)
            game_loop.run()
            game_over = GameOverScreen(SCREEN, game_loop.score, player_name, difficulty_label)
            result = game_over.show()
            
            if result == "try_again":
                self.play()
            
        except Exception as e:
            print(f"Error starting game: {e}")

    def customize(self):
        customize_screen = CustomizeScreen(SCREEN)
        snake_color, background = customize_screen.show()
        
        if snake_color and background:
            self.selected_snake_color = snake_color
            self.selected_background = background
            print(f"Settings updated - Snake: {snake_color}, Background: {background}")

    def info(self):
        instructions = InstructionsScreen(SCREEN)
        instructions.show()

    def exit_game(self):
        confirm_dialog = ExitConfirmDialog(SCREEN)
        should_exit = confirm_dialog.show()
        if should_exit:
            return "exit"

def main():
    pygame.init()
    pygame.display.set_caption("Snake Core")
    
    menu = Menu(SCREEN)
    menu.show_menu()

    game_running = True

    while game_running:
        mouse_pos = pygame.mouse.get_pos()
        menu.hovered_button = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, button_rect in enumerate(menu.button_rects):
                        if button_rect.collidepoint(event.pos):
                            result = menu.menu_options[i]["command"]()
                            if result == "exit":
                                game_running = False
                            break
            elif event.type == pygame.VIDEORESIZE:
                menu.update_button_positions()

        for i, button_rect in enumerate(menu.button_rects):
            if button_rect.collidepoint(mouse_pos):
                menu.hovered_button = i
                break

        SCREEN.fill((33, 89, 77))

        if menu.logo_loaded:
            SCREEN.blit(menu.logo, menu.logo_rect)
        
        for i, button_rect in enumerate(menu.button_rects):
            is_hovered = menu.hovered_button == i
            button_col = button_hover_color if is_hovered else button_color
            
            pygame.draw.rect(SCREEN, button_col, button_rect, border_radius= 15)
            pygame.draw.rect(SCREEN, (0, 0, 0), button_rect, 2, border_radius= 15)
            
            text = menu.font.render(menu.menu_options[i]["label"], True, button_text_color)
            text_rect = text.get_rect(center=button_rect.center)
            SCREEN.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    # No changes made 22/06/2026
    # No changes made 23/06/2026