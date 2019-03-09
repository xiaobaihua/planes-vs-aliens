def update_bullet(bullets):
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 删除屏幕外的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
