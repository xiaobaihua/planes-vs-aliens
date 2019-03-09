from alien import Alien
from settings import Setting as S
import pygame


s = S()


def get_aliens(aliens, number):
    for n in range(number):
        if len(aliens) <= s.alien_sum:
            aliens.add(Alien())


def draw_aliens(screen, aliens):
    for a in aliens.sprites():
        a.blitme(screen)


def destroy(aliens):
    for alien in aliens.copy():
        if alien.rect.centery >= s.screen_height:
            aliens.remove(alien)
            print(len(aliens))


def blitme(alien):
    alien.blitme(alien.image, alien.rect)


def update_alien(screen, aliens):
    get_aliens(aliens, s.alien_lot)
    draw_aliens(screen, aliens)
    collide(aliens)
    destroy(aliens)


def collide(aliens):
    aliens_c = aliens.copy()
    for alien in aliens.sprites():
        aliens_c.remove(alien)
        for a in aliens_c:
            if pygame.sprite.collide_rect(alien, a):
                aliens.remove(alien)
