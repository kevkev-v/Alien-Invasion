import pygame
import sys

from settings import Settings
from ship import Ship

def run_game():
    pygame.init()

    # We connect the class Settings from the other file, and store it in ai_settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion") # Renaming the window's title

    # Make a ship
    ship = Ship(screen)

    while True:
        # Watch for keyboard and mouse events, like a click on X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Redraw the screen by using this color during each pass through the loop       
            screen.fill(ai_settings.bg_color)
            ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
