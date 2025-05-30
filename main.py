# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)



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

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Konec")
                exit()

            for bullet in shots:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()


        # TOO MANY LOOPING
        # for asteroid in asteroids:
        #     for bullet in shots:
        #         if bullet.collision(asteroid):
        #             asteroid.kill()
        #             bullet.kill()

        pygame.display.flip()
        clock.tick(60)

        # limitation of FPS to 60fps
        dt = clock.tick(60)/1000





if __name__ == "__main__":
    main()
