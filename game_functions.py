import sys
import pygame

def check_keydown_events (event, ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT: # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: # Move the ship to the left
        ship.moving_left = True

def check_keyup_events (event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
        # Watch for keyboard and mouse events, like a click on X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Keypress Ship Movement
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
                # Stop moving the ship when the key is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                    
def update_screen (ai_settings , screen, ship):
    #Redraw the screen by using this color during each pass through the loop       
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
