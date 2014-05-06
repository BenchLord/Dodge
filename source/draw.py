import pygame
import graphics
import game
from sprite import Sprite

def draw():
    """
    Drawing logic
    """

    # Draw background
    game.background.draw()
    game.background2.draw()

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
        graphics.draw_text("Final Score: " + str(game.score), (255,255,255), (210,275))
        graphics.draw_text("PRESS SPACE TO PLAY AGAIN", (255,255,255), (100,325))

    return

