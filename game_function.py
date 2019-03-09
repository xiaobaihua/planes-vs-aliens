import sys

import pygame
import pygame as pg

from bullet import Bullet
from bullet_function import update_bullet
from settings import Setting
import alien_function as af

s = Setting()


def init():
    # 初始化pygame
    pg.init()
    # 初始化screen设

    # 获得一个屏幕对象
    screen = pg.display.set_mode((s.screen_width, s.screen_height))

    # 设置舞台(screen)标题
    pg.display.set_caption('飞机大战')

    if screen:
        return screen


def event_key_down(event, ship, bullets):
    if event.key == pg.K_RIGHT:
        ship.rect.centerx += ship.ship_speed
        ship.flag_right = True
    elif event.key == pg.K_LEFT:
        ship.rect.centerx -= ship.ship_speed
        ship.flag_left = True
    elif event.key == pg.K_UP:
        ship.rect.centery -= ship.ship_speed
        ship.flag_up = True
    elif event.key == pg.K_DOWN:
        ship.rect.centery += ship.ship_speed
        ship.flag_down = True
    if event.key == pg.K_SPACE:
        bullets.add(Bullet(s, ship.screen, ship))


def event_key_up(event, ship):
    if event.key == pg.K_RIGHT:
        ship.flag_right = False
    elif event.key == pg.K_LEFT:
        ship.flag_left = False
    elif event.key == pg.K_UP:
        ship.flag_up = False
    elif event.key == pg.K_DOWN:
        ship.flag_down = False


def check_events(ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            event_key_down(event, ship, bullets)
        elif event.type == pg.KEYUP:
            event_key_up(event, ship)


def collide(ship, bullets, aliens):
    for a in aliens.sprites():
        for b in bullets.sprites():
            if pygame.sprite.collide_rect(b, a):
                bullets.remove(b)
                aliens.remove(a)

            if ship.rect.colliderect(a.rect):
                sys.exit()


def update_screen(screen, ship, bullets, aliens):
    # 帧率
    pg.time.Clock().tick(30)
    # 利用背景填充来重绘舞台
    screen.fill(s.bg_color)

    # 绘制并删除子弹
    update_bullet(bullets)

    # 绘制敌人并删除敌人
    af.update_alien(screen, aliens)

    # 绘制玩家飞船
    ship.blitme()

    # 攻击
    collide(ship, bullets, aliens)

    # 设置最近绘制的图形可见
    pg.display.flip()
