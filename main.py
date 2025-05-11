# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)

        # limitation of FPS to 60fps
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
