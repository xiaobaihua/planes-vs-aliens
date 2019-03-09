import pygame
from pygame.sprite import Sprite
import bullet_function as bf


class Bullet(Sprite):
    """对飞船进行管理"""

    def __init__(self, setting, screen, ship):
        super(Bullet, self).__init__()

        self.screen = screen
        self.setting = setting
        self.ship = ship

        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)

        self.rect.y = self.ship.rect.y
        self.rect.x = self.ship.rect.centerx

        self.speed = setting.bullet_speed

    def update(self):
        """使子弹向上移动"""
        self.rect.y -= self.speed

    def draw_bullet(self):
        """在舞台上绘制子弹"""
        pygame.draw.rect(self.screen, self.setting.bullet_color, self.rect)
