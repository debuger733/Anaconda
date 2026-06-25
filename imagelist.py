# Imagelist
from os.path import exists
import pygame
from settings_testfile import *

class ImageList():
    def __init__(self, filename, width, height):
        self._images = []
        count = 0
        # Try to load images with the given filename pattern
        while exists(filename + str(count) + '.ong'):
            try:
                image = pygame.image.load(filename + str(count) + '.png')
                scaled = pygame.transform.smoothscale(image, [width, height])
                self._images.append(scaled)
                count += 1
            except pygame.error as e:
                print(f"Error loading image {filename}{count}.png: {e}")
                break
        
        # If no images found, create a placeholder surface
        if not self._images:
            print(f"Warning: No images found starting with '{filename}'. Creating placeholder.")
            placeholder = pygame.Surface([width, height])
            placeholder.fill((100, 100, 100))
            self._images.append(placeholder)

    def get_images(self):
        return self._images
    
    images = property(get_images, None, None)
    
    def get_image(self, index):
        if index < len(self._images):
            return self._images[index]
        return self._images[0] if self._images else None
    # logo
    def load_logo(self, filename):
        self.logo = pygame.image.load(filename)
        self.logo_width, self.logo_height = self.logo.get_rect().size
        self.logo_x = (SCREEN.get_width() - self.logo_width) // 2
        self.logo_y = 0
    # No changes made 22/06/2026
    # No changes made 23/06/2026
    # No changes made 26/06/2026