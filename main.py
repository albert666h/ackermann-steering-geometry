import numpy as np
import pygame
from rover import Rover, Wheel

pygame.init()

window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Ackermann Steering Geometry')

running = True

# Set up a clock to control FPS
FPS = 60
clock = pygame.time.Clock()

rover = Rover(pos=np.array([540, 360], dtype='float'), 
        wheels=[
            Wheel(np.array([-100, 150], dtype='float'), 0),
            Wheel(np.array([-100, 50], dtype='float'), 0),
            Wheel(np.array([-100, -150], dtype='float'), 0),
            Wheel(np.array([100, 150], dtype='float'), 0),
            Wheel(np.array([100, 50], dtype='float'), 0),
            Wheel(np.array([100, -150], dtype='float'), 0)
        ], 
        max_turn_angle=45)

keys_pressed = {
    'a': False,
    'd': False
}

if __name__ == "__main__":
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    keys_pressed['a'] = True
                elif e.key == pygame.K_d:
                    keys_pressed['d'] = True

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_a:
                    keys_pressed['a'] = False
                elif e.key == pygame.K_d:
                    keys_pressed['d'] = False
                
        window.fill((33, 33, 33))
        clock.tick(FPS)

        if keys_pressed['a']:
            rover.turn(1)
        elif keys_pressed['d']:
            rover.turn(-1)

        # display the wheels
        for wheel in rover.wheels:
            # Rotate the rectangle surface
            rotated_surface = pygame.transform.rotate(wheel, wheel.angle)
            rotated_rect = rotated_surface.get_rect(center=(wheel.pos[0] + rover.pos[0], -wheel.pos[1] + rover.pos[1]))  # Center the rotated rect

            # Draw the rotated rectangle on the screen
            window.blit(rotated_surface, rotated_rect.topleft)

        pygame.display.update()

    pygame.quit()
