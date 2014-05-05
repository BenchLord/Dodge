import pygame
import game

def draw_rect(size, color, position):
    """
    Draws a rectangle with style

    eg:
        size (width, height)
        color (255, 255, 255) rgb
        positon (x, y)
    """

    pygame.draw.rect(game.screen, color, (position, size), 0)

    return

def draw_text(text, color, position):
    """
    Draws text to the screen

    eg:
        text ("hello")
        color (255, 255, 255) rgb
        position (x, y)
    """
    
    label = game.main_font.render(text, 1, color)
    game.screen.blit(label, position)

def draw_circle():
    pass