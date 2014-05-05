import pygame
import game

class Sound():
    """
    Represents a sound effect
    """

    def __init__(self, filename):
        self.sound = pygame.mixer.Sound(game.rpath + filename)

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()

class Music():
    """
    Represents a song
    """
    
    def __init__(self, filename):
        pygame.mixer.music.load(game.rpath + filename)

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()
