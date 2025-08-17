import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame (initialize all imported pygame modules)
    pygame.init()
    # Get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Background img
    bg = pygame.image.load("background.jpg")
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # create an object to help track time
    clock = pygame.time.Clock()
    # Use "delta time" to represent the amount of time that has 
    # passed since the last frame was drawn
    # delta time set to 0
    dt = 0

    # Create container that holds and manages multiple game objects
    # all the objects that can be updated
    updatable = pygame.sprite.Group()
    # all the objects that can be drawn
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # add all instances of a Player to two groups 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # middle of screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Game obj
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            # Check if the user has closed the 
            # window and exit the game loop
            # make the window's close button work.
            if event.type == pygame.QUIT:
                return

        # Fill the screen with a solid "black" color
        # screen.fill("black")
        # Fill with a back ground
        screen.blit(bg, (0, 0))

        # Draw obj
        updatable.update(dt)

        # Check collisions
        for asteroid in asteroids:
            # Check game over
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()

            # Check bullet
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)



        # Refresh the screen
        pygame.display.flip()

        # Pause the game loop until 1/60th of a second has passed.
        # Return the amount of time that has passed since the 
        # last time it was called (miliseconds)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
