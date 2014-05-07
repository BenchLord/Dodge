import pygame
import game

class Sprite(pygame.sprite.Sprite):
    def __init__(self, texture, position, align):
<<<<<<< HEAD
        self.texture = texture
        self.image 	 = pygame.image.load(game.rpath + texture)
        self.rect 	 = self.image.get_rect()
     	self.rect.x  = position[0]
     	self.rect.y  = position[1]
        self.alive   = False
        self.align   = align
=======
        self.image 	= pygame.image.load(game.rpath + texture)
        self.rect 	= self.image.get_rect()
     	self.rect.x = position[0]
     	self.rect.y = position[1]
        self.alive  = False
        self.align  = align
>>>>>>> e912b0e9c048cf12b05069addab8840d86a91706
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