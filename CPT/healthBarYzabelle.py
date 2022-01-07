import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 93, 155)
GRAY = (128,128,128)

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
# --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
# --- Game logic should go here
# --- Screen-clearing code goes here
# Here, we clear the screen to white. Don't put other drawing commands
# above this, or they will be erased with this command.
# If you want a background image, replace this clear with blit'ing the
# background image.
    screen.fill(WHITE)
# --- Drawing code should go here
    #USER HEALTH BAR
    #Top bar
    pygame.draw.polygon(screen, BLACK, [(0, 0), (305, 0), (325, 45), (0, 45)], 0)
    pygame.draw.polygon(screen, RED, [(5, 5), (300, 5), (315, 40), (5, 40)], 0)
    #Bottom bar
    pygame.draw.polygon(screen, GRAY, [(0, 45), (205, 45), (220, 77), (0, 77)], 0)
    font = pygame.font.SysFont('Arial', 35, True, False)
    text = font.render("You", True, BLACK)
    screen.blit(text, [5, 50])
    #COMPUTER HEALTH BAR
    #Top bar
    pygame.draw.polygon(screen, BLACK, [(800, 0), (800, 45), (490, 45), (510, 0)], 0)
    pygame.draw.polygon(screen, RED,[(795, 5), (795, 40), (500, 40), (515, 5)], 0)
    
    #Bottom bar
    pygame.draw.polygon(screen, GRAY, [(800, 45), (800, 77), (580, 77), (595, 45)], 0)
    font = pygame.font.SysFont('Arial', 35, True, False)
    text = font.render("Opponent", True, BLACK)
    screen.blit(text, [660, 50])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()



