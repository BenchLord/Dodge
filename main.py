#
# Dodge!
# Copyright 2014, Brandon Bench
# 
# Version 0.9
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
    game.player = Sprite("player.png", (0,540))

    game.coins = []
    game.baddies = []

    game.score = 0
    game.speed = 1
    # Play a sound!
    # game.coin = Sound("coin.wav") <-- make sure your file is supported!
    # game.coin.play()

    # Drop those jams!
    # game.music = Music("music.ogg") <-- Make sure your file is supported!
    # game.music.play()

    return

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

        update(keys)        # update.py
        draw()              # draw.py
        
        # Simply flips the display for drawing
        pygame.display.update()
        pygame.display.flip()

    return

# Ignore this, it simply calls the main() function
if __name__ == "__main__":
    main()