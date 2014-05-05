import pygame
import game
from sprite import Sprite
from random import randint


def update(keys):
    """
    Update game world here
    """

    for key in keys:
        if key == pygame.K_LEFT:
            game.player.move(-3,0)
        if key == pygame.K_RIGHT:
            game.player.move(3,0)
        if key == pygame.K_UP:
            game.player.move(0,-3)
        if key == pygame.K_DOWN:
            game.player.move(0,3)

    if randint(0,25) == 1:
        game.baddies.append(Sprite("baddie.png",(randint(0,24) * 25,-50)))

    if randint(0,100) == 1:
        game.coins.append(Sprite("coin.png",(randint(0,24) * 25, -25)))

    # Keeps player inside of the window
    if game.player.rect.left <= 0:
        game.player.rect.left = 0
    if game.player.rect.right >= game.window_size[0]:
        game.player.rect.right = game.window_size[0]
    if game.player.rect.top <= 0:
        game.player.rect.top = 0
    if game.player.rect.bottom >= game.window_size[1]:
        game.player.rect.bottom = game.window_size[1]

    if game.score >= 10:
        game.speed = game.score/10

    # Baddie Logic
    for baddie in game.baddies:
        baddie.rect.y += game.speed
        if baddie.rect.y >= game.window_size[1]:
            game.baddies.remove(baddie)
        if game.player.rect.colliderect(baddie):
            raise SystemExit, "Final Score: " + str(game.score)
            # Use a deathscreen


    # Coin Logic
    for coin in game.coins:
        coin.rect.y += 1
        if coin.rect.y >= game.window_size[1]:
            game.coins.remove(coin)
        if game.player.rect.colliderect(coin):
            game.coins.remove(coin)
            game.score += 1

    return
