import sys
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from logger import log_state, log_event
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astroid_field = AsteroidField()

    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for _asteroid in asteroids:
            for _shot in shots:
                if _asteroid.collides_with(_shot):
                    log_event("asteroid_shot")
                    _shot.kill()
                    _asteroid.split()

            if _asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for _drawable in drawable:
            _drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
