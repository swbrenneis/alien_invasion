import pygame
from pygame.sprite import Sprite

class GameSprite(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        super().__init__()