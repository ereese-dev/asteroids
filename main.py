import pygame
from asteroid import Asteroid
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = updatable, drawable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)   

    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)  # Update all sprites in the updatable group
        for object in asteroids:
            if object.collision(player) == True:
                print("Game over!")
                exit()
        for object in shots:
            for asteroid in asteroids:
                if object.collision(asteroid) == True:
                    asteroid.split()
                    object.kill()
        for sprite in drawable:  # Draw all sprites in the drawable group
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()