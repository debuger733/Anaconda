"""This is the imagelist file"""


from os.path import exists
import pygame
from settings_testfile import *

class ImageList():
    """Manages loading and retrieving sprite images."""
    def __init__(self, filename, width, height):
        # List to store all loaded and scaled images
        self._images = []
        count = 0
        # Try to load images with the given filename pattern
        while exists(filename + str(count) + '.ong'):
            try:
                # Loading the image file from the disk
                image = pygame.image.load(filename + str(count) + '.png')
                # Scaling the images
                scaled = pygame.transform.smoothscale(image, [width, height])
                # Adding the images to the list
                self._images.append(scaled)
                count += 1
            except pygame.error as e:
                # Printing an error message of the image fails or stops loading
                print(f"Error loading image {filename}{count}.png: {e}")
                break
        
        # If no images found, create a placeholder surface
        if not self._images:
            print(f"Warning: No images found starting with '{filename}'. Creating placeholder.")
            # Creating a grey colored placeholder
            placeholder = pygame.Surface([width, height])
            placeholder.fill((100, 100, 100))
            self._images.append(placeholder)

    def get_images(self):
        """Returning the complete list of images."""
        return self._images
    # This property allows accessing images through ImageList.images
    images = property(get_images, None, None)
    
    def get_image(self, index):
        """Retrieving a single image by its index."""
        if index < len(self._images):
            return self._images[index]
        return self._images[0] if self._images else None

    def load_logo(self, filename):
        """
        Loading the logo image.
        Positioning this image.
        """
        # Loading the logo image
        self.logo = pygame.image.load(filename)
        # Getting the logo image dimensions
        self.logo_width, self.logo_height = self.logo.get_rect().size
        # Calculating to center the logo
        self.logo_x = (SCREEN.get_width() - self.logo_width) // 2
        # Setting the logo position at the top of the screen
        self.logo_y = 0

    # No changes made 22/06/2026
    # No changes made 23/06/2026
    # No changes made 26/06/2026
    # No changes made 29/06/2026
    # No changes made 03/07/2026
    # No changes made 21/07/2026
    
