import random

from settings import Setting
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self):
        super(Alien, self).__init__()
        self.setting = Setting()

        self.image = pygame.image.load('img/alien.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, 600)

    def blitme(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centery += self.setting.alien_speed

    def upset_centerx(self):
        self.rect.centerx = random.randrange(1, 600, 50)

        return self.rect.centerx

