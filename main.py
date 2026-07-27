"""This is the main file."""

# Importing and linking other files needed to run the game
import pygame
from imagelist import ImageList
from mysprite import Food, Mysprite, DifficultyMenu, GameLoop
from button_info import (
    PlayerNameInput,
    GameOverScreen,
    InstructionsScreen,
    CustomizeScreen,
    ExitConfirmDialog,
)
from settings import *


class Menu:
    """This class creates the Main menu."""

    def __init__(self, screen):
        """This section initializes the Main menu elements."""
        self.screen = screen
        self.font = pygame.font.Font(None, 25)
        self.logo_loaded = False
        self.logo = None
        self.logo_rect = None
        
        # Loading the logo
        try:
            self.logo = pygame.image.load(LOGO_PATH)
            self.logo = pygame.transform.smoothscale(self.logo, (LOGO_W, LOGO_H))
            # Position the logo at the top center of the screen
            self.logo_rect = self.logo.get_rect(center=(self.screen.get_width() // 2, 110))
            self.logo_loaded = True
        except Exception as exc:
            print(f"Error loading logo: {exc}")
            self.logo_loaded = False

        # Buttons of the Main menu
        self.menu_options = [
            {"label": "Play", "command": self.play},
            {"label": "Customize", "command": self.customize},
            {"label": "Info", "command": self.info},
            {"label": "Exit", "command": self.exit_game},
        ]

        # Initializing button tracking variables
        self.button_rects = []
        self.hovered_button = None

        # Initializing snake color and background
        self.selected_snake_color = "green"
        self.selected_background = "grey_white"

    def update_button_positions(self):
        """Updating the position of the buttons."""
        # Calculate and updating the positions of the buttons
        self.button_rects = []
        button_x = (self.screen.get_width() - button_width) // 2
        button_count = len(self.menu_options)
        button_total_height = button_count * (button_height + button_spacing)
        button_y_offset = (self.screen.get_height() - button_total_height) // 2 + 100

        # Creating the rectangular shape for the buttons
        for i in range(button_count):
            button_rect = pygame.Rect(
                button_x,
                button_y_offset + i * (button_height + button_spacing),
                button_width,
                button_height,
            )
            self.button_rects.append(button_rect)

    def show_menu(self):
        """Updating button positions."""
        self.update_button_positions()

    def play(self, player_name=None):
        """This section controls the play button."""
        # If no name is entered show the input dialog
        if player_name is None:
            name_input = PlayerNameInput(SCREEN)
            player_name = name_input.show()

        # Exit if player canceled name input
        if player_name is None:
            return

        # Difficulty selection
        difficulty_menu = DifficultyMenu(SCREEN)
        selected_speed = difficulty_menu.show()

        # Exit if player cancelled difficulty selection
        if selected_speed is None:
            return

        # Speed label depending on difficulty
        difficulty_map = {3: "Easy", 5: "Medium", 7: "Hard"}
        difficulty_label = difficulty_map.get(selected_speed, "Medium")

        try:
            # Initializing the food image and positioning
            food = Food(200, 200, FOOD_W, FOOD_H, IMAGE_PATH, SCREEN)
            test_imagelist = ImageList(SPRITE_FILES, TEST_W, TEST_H)
            start_x = (SCREEN_WIDTH // 2 // 60) * 60
            start_y = (SCREEN_HEIGHT // 2 // 60) * 60
            snake_segments = [Mysprite(start_x, start_y, TEST_W, TEST_H, test_imagelist, SCREEN, selected_speed, self.selected_snake_color)]
            game_loop = GameLoop(snake_segments, food, SCREEN, test_imagelist, selected_speed, self.selected_snake_color, self.selected_background)
            game_loop.run()
            game_over = GameOverScreen(SCREEN, game_loop.score, player_name, difficulty_label)
            result = game_over.show()

            # If player chose to try again, restart the game with the same player name
            if result == "try_again":
                self.play(player_name)

        except Exception as exc:
            print(f"Error starting game: {exc}")

    def customize(self):
        """This sections controls the Customization button."""
        customize_screen = CustomizeScreen(SCREEN)
        snake_color, background = customize_screen.show()

        # Checking if the player did customizing
        # Saving them to start the game with
        if snake_color and background:
            self.selected_snake_color = snake_color
            self.selected_background = background
            # Printing the customization done by the player
            print(f"Settings updated - Snake: {snake_color}, Background: {background}")

    def info(self):
        """This section controls the Information button."""
        instructions = InstructionsScreen(SCREEN)
        instructions.show()

    def exit_game(self):
        """This section controls the Exit button"""
        confirm_dialog = ExitConfirmDialog(SCREEN)
        should_exit = confirm_dialog.show()
        if should_exit:
            return "exit"

def main():
    """Main function"""
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Snake Core")

    # Initialize the main menu
    menu = Menu(SCREEN)
    menu.show_menu()

    game_running = True

    # Main event loop
    # This runs the game untill the user exists
    while game_running:

        # Getting current mouse position to hover the buttons
        mouse_pos = pygame.mouse.get_pos()
        menu.hovered_button = None

        # Processing all pygame events
        for event in pygame.event.get():
            # Closing the game if user clicks close
            if event.type == pygame.QUIT:
                game_running = False
            # Handling mouse clicks on buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Checking if the mouse is clicked on any button
                    for i, button_rect in enumerate(menu.button_rects):
                        if button_rect.collidepoint(event.pos):
                            # Proceeding based on the button clicked on
                            result = menu.menu_options[i]["command"]()
                            # Exit the game if exit comman was triggered
                            if result == "exit":
                                game_running = False
                            break
            # Resizing of the window
            elif event.type == pygame.VIDEORESIZE:
                # Repositioning if the window was resized
                menu.update_button_positions()
        # Checking which button the mouse pointer is currently hovering over
        for i, button_rect in enumerate(menu.button_rects):
            if button_rect.collidepoint(mouse_pos):
                menu.hovered_button = i
                break

        # The background color of the main menu window
        SCREEN.fill((33, 89, 77))

        if menu.logo_loaded:
            SCREEN.blit(menu.logo, menu.logo_rect)

        # Drawing all Main menu buttons
        for i, button_rect in enumerate(menu.button_rects):
            # Checking if the button is being hovered
            is_hovered = menu.hovered_button == i
            button_col = button_hover_color if is_hovered else button_color

            pygame.draw.rect(SCREEN, button_col, button_rect, border_radius=15)
            pygame.draw.rect(SCREEN, (0, 0, 0), button_rect, 2, border_radius=15)

            text = menu.font.render(menu.menu_options[i]["label"], True, button_text_color)
            text_rect = text.get_rect(center=button_rect.center)
            # Drawing the text on the screen
            SCREEN.blit(text, text_rect)

        # Updating the display with all drawn elements
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
    # No changes made 22/06/2026
    # No changes made 23/06/2026
    # No changes made 29/06/2026
    # No changes made 02/07/2026
    