import pygame
import graphics
import game
from sprite import Sprite

def draw():
    """
    Drawing logic
    """

    # Draw background
    game.screen.fill((0, 0, 255))
    
    # Drawing a sprite called my_sprite
    # my_sprite.draw()
    if game.player.alive:
        game.player.draw()

    if game.player.alive:
        for baddie in game.baddies:
            baddie.draw()
        for coin in game.coins:
            coin.draw()

    # Draw some text
    # graphics.draw_text("Hello World", (255, 255, 255), (50, 50))
    if game.player.alive:
        graphics.draw_text("Score: " + str(game.score), (255,255,255), (10,10))
    else:
        graphics.draw_text("Final Score: " + str(game.score), (255,255,255), (250,275))
        graphics.draw_text("PRESS SPACE TO PLAY AGAIN", (255,255,255), (190,325))

    return

