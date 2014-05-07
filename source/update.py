import pygame
import game
from sprite import Sprite
from random import randint

def update(keys):
    """
    Update game world here
    """

    # Player movement
    for key in keys:
        if key == pygame.K_LEFT or key == pygame.K_a:
            game.player.move(-3,0)
        if key == pygame.K_RIGHT or key == pygame.K_d:
            game.player.move(3,0)
        if key == pygame.K_UP or key == pygame.K_w:
            game.player.move(0,-3)
        if key == pygame.K_DOWN or key == pygame.K_s:
            game.player.move(0,3)

    # Obstacle spawn       
    if randint(0,25) == 1:
        game.baddies.append(Sprite("obstacle.png",(randint(0,25) * 24,-25), 'x'))

    if randint(0,12) == 1:
        game.baddies.append(Sprite("obstacle.png",(-25, randint(-50,24) * 25), 'y'))
    if randint(0,12) == 1:
        game.baddies.append(Sprite("obstacle.png",(game.window_size[0]+25, randint(0,24) * 30), '-y'))

    # Collectable spawn
    if randint(0,75) == 1:
        game.coins.append(Sprite("coin.png",(randint(0,24) * 25, -25), 'x'))
    if randint(0,200) == 1:
        game.coins.append(Sprite("coin2.png",(randint(0,24) * 25, -25), 'x'))
    if randint(0,1000) == 1:
        game.coins.append(Sprite("coin3.png",(randint(0,24) * 25, -25), 'x'))


    # Keeps player inside of the window
    if game.player.rect.left <= 0:
        game.player.rect.left = 0
    if game.player.rect.right >= game.window_size[0]:
        game.player.rect.right = game.window_size[0]
    if game.player.rect.top <= 0:
        game.player.rect.top = 0
    if game.player.rect.bottom >= game.window_size[1]:
        game.player.rect.bottom = game.window_size[1]

    # Speed is based on score
    if game.score >= 10:
        game.speed = game.score/10

    # Obstacle Logic
    for baddie in game.baddies:
        if baddie.align == "x":
            baddie.rect.y += game.speed
            if baddie.rect.y >= game.window_size[1]:
                game.baddies.remove(baddie)

        if baddie.align == "y":
            baddie.rect.x += game.speed
            baddie.rect.y += game.speed
            if baddie.rect.x >= game.window_size[0]:
                game.baddies.remove(baddie)

        if baddie.align == "-y":
            baddie.rect.x -= game.speed
            baddie.rect.y += game.speed
            if baddie.rect.x <= 0:
                game.baddies.remove(baddie)

        if game.player.rect.colliderect(baddie.rect.inflate(-7,-7)):
            game.boom.play()
            game.player.alive = False


    # Coin Logic
    for coin in game.coins:
        coin.rect.y += 1
        if coin.rect.y >= game.window_size[1]:
            game.coins.remove(coin)

        if game.player.rect.colliderect(coin):
            game.coins.remove(coin)
            game.coin.play()
            if coin.texture == "coin3.png":
                game.score += 10
            elif coin.texture == "coin2.png":
                game.score += 5
            else:
                game.score += 1

    # Keep them backgrounds moving
    game.background.move(0,1)
    game.background2.move(0,1)

    # There is probably a better way to do this...
    if game.background.rect.top >= 600:
        game.background.rect.bottom = 0
    if game.background2.rect.top >= 600:
        game.background2.rect.bottom = 0


    return

