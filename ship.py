import pygame


class Ship:

    def __init__(self, screen, ship_speed):
        # 初始化飞船及其设置
        self.screen = screen

        # 加载图片
        self.img = pygame.image.load('img/ship.png')
        # 获取飞船矩形对象
        self.rect = self.img.get_rect()
        # 获取舞台矩形对象
        self.screen_rect = self.screen.get_rect()

        # 设置飞船在舞台的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 飞船移动速度
        self.ship_speed = ship_speed

        self.flag_right = False
        self.flag_left = False
        self.flag_up = False
        self.flag_down = False

    def blitme(self):
        # 在指定的位置绘制飞船
        self.screen.blit(self.img, self.rect)

    def update_seat(self):
        if self.flag_right and self.screen_rect.right > self.rect.right:
            self.rect.centerx += self.ship_speed
        if self.flag_left and self.screen_rect.left < self.rect.left:
            self.rect.centerx -= self.ship_speed
        if self.flag_up and self.screen_rect.top < self.rect.top:
            self.rect.centery -= self.ship_speed
        if self.flag_down and self.screen_rect.bottom > self.rect.bottom:
            self.rect.centery += self.ship_speed

