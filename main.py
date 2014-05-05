#
# Dodge!
# Copyright 2014, Brandon Bench
# 
# Version 1.5
#

import sys, pygame
from source import game
from source.update import update
from source.draw import draw
from source.sprite import Sprite
from source.sound import Sound, Music

def init():
    """
    Perform game-wide initilization, such as setting variables and loading
    resources
    """

    # Simple 8-bit font. Test me out in draw.py
    game.main_font   = pygame.font.Font("resources/main_font.ttf", 18)

    # Example:
    # game.my_sprite = Sprite("filename.png", (50, 50))
    game.player = Sprite("player.png", (290,540))
    game.player.alive = True

    game.coins = []
    game.baddies = []

    game.score = 0
    game.speed = 1
    # Play a sound!
    # game.coin = Sound("coin.wav") <-- make sure your file is supported!
    # game.coin.play()
    game.coin = Sound("coin.wav")
    game.boom = Sound("boom.wav")

    # Drop those jams!
    # game.music = Music("music.ogg") <-- Make sure your file is supported!
    # game.music.play()

    return

def deathscreen():
    game.boom.play()
    for coin in game.coins:
        game.coins.remove(coin)
    for baddie in game.baddies:
        game.baddies.remove(baddie)

    while True:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.QUIT: 
                sys.exit()


# Don't mess with me unless you know what you're doing
def main():
    """
    Main game initialization code
    """

    # Set up pygame
    pygame.init()
    pygame.mixer.init()
    game.screen = pygame.display.set_mode(game.window_size, pygame.DOUBLEBUF)
    keys = set()

    # Set up game
    init()

    # Perform game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: keys.add(event.key)
            if event.type == pygame.KEYUP: keys.discard(event.key)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit()

        if game.player.alive:
            update(keys)        # update.py
            draw()              # draw.py
        else:
            deathscreen()
        
        # Simply flips the display for drawing
        pygame.display.update()
        pygame.display.flip()

    return

# Ignore this, it simply calls the main() function
if __name__ == "__main__":
    main()