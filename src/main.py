# Import Libraries
import pygame
import random
from particleClass import Particle
# Initialise pygame
pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('arial', 16)
 
WIDTH, HEIGHT = 800, 600 # width and height of simulation window
FPS = 100 # frames per second for simulation

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Life Simulator")

def main():
    clock = pygame.time.Clock()
    running = True

    

    while running:

        # Check for events to end the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # End the game if the mousebutton is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # Display the simulation time
        totalTime = pygame.time.get_ticks() # Total time in milliseconds
        
        elapsedMinutes = totalTime // 60000 # Calculate number of minutes
        elapsedSeconds = (totalTime % 60000) // 1000 # Calculate number of seconds
        elapsedMilliseconds = totalTime % 1000 # Calculate number of milliseconds

        totalTime_string = f'{elapsedMinutes:02}:{elapsedSeconds:02}:{elapsedMilliseconds:02}' # Create a string for total time

        textSurface = my_font.render(totalTime_string, False, WHITE) # Create a surface containing the text

        screen.blit(textSurface, (40,350)) # Attach the text surface to the main screen

        for particle in particles:
            particle.draw(screen)

        print(totalTime_string) # Print the time to terminal

        # Refresh the screen
        pygame.display.update()
        clock.tick(FPS)
    
        screen.fill(BLACK)

if __name__ == "__main__":
    main()