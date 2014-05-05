import pygame
import game

class Sprite(pygame.sprite.Sprite):
    def __init__(self, texture, position):
        self.image 	= pygame.image.load(game.rpath + texture)
        self.rect 	= self.image.get_rect()
     	self.rect.x = position[0]
     	self.rect.y = position[1]
        return

    def draw(self):
        game.screen.blit(self.image, self.rect)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def remove(self):
        pass

    def rotate(self, degree):
        pass

    def set_opacity(self, percent):
        pass