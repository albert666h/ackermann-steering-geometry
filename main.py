import numpy as np
import pygame

pygame.init()

window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Ackermann Steering Geometry')

running = True

if __name__ == "__main__":
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break
                
        window.fill((33, 33, 33))

        pygame.display.update()

    pygame.quit()
