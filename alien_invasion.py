import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()

    # We connect the class Settings from the other file, and store it in ai_settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion") # Renaming the window's title

    # Make a ship
    ship = Ship(ai_settings , screen)

    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        ship.update()

run_game()
