from pygame.sprite import Group

from ship import Ship
import game_function as gf
import alien_function as af


def run_game():
    # 初始化游戏设置
    screen = gf.init()
    # 创建飞船
    ship = Ship(screen, gf.s.ship_speed)
    # 创建子弹
    bullets = Group()
    # 创建敌人
    aliens = Group()

    while True:
        gf.update_screen(screen, ship, bullets, aliens)

        gf.check_events(ship, bullets)

        bullets.update()
        ship.update_seat()
        aliens.update()
run_game()
