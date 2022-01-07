#
# Pygame base template for opening a window
#
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
#
# Explanation video: http://youtu.be/vRB_983kUMc
import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 93, 155)
GRAY = (128,128,128)

pygame.init()

class Health():
    
    def __init__ (self):
        
        #Bar's original position
        self.userhb_x = 0
        self.comhb_x = 0
        
        #Change in health bars
        self.difference_x = 0
        
        #Class Methods
        
    def draw(self, screen):
#USER HEALTH BAR
    #Top bar
        pygame.draw.polygon(screen, BLACK, [(0, 0), (305, 0), (325, 45), (0, 45)], 0)
        pygame.draw.polygon(screen, RED, [(5, 5), (self.health1_x, 5), (self.health2_x, 40), (5, 40)], 0)
#Bottom bar
        pygame.draw.polygon(screen, GRAY, [(0, 45), (205, 45), (220, 70), (0, 70)], 0)
    
        font = pygame.font.SysFont('Arial', 35, True, False)
        text = font.render("You", True, BLACK)
        screen.blit(text, [5, 45])
        
#COMPUTER HEALTH BAR
#Top bar
        pygame.draw.polygon(screen, BLACK, [(800, 0), (800, 45), (490, 45), (510, 0)], 0)
        pygame.draw.polygon(screen, RED,[(795, 5), (795, 40), (500, 40), (515, 5)], 0)

#Bottom bar
        pygame.draw.polygon(screen, GRAY, [(800, 45), (800, 70), (self.health11_x, 70), (self.health22_x, 45)], 0)
        
        font = pygame.font.SysFont('Arial', 35, True, False)
        text = font.render("Opponent", True, BLACK)
        screen.blit(text, [660, 45])
        
    def move(self):
        
        if (answer == 1):
            self.health1_x -= self.difference_x
            self.health2_x -= self.difference_x
        elif (answer == 2):
            self.health11_x += self.difference_x
            self.health22_x += self.difference_x
            
#Class Button Objects / Instance 

userhb1 = Health()
userhb1.health1_x = 300
userhb1.difference_x = 30

userhb2 = Health()
userhb2.health2_x = 315
userhb2.difference_x = 30

comhb1 = Health()
comhb1.health11_x = 580
comhb1.difference_x = 30

comhb2 = Health()
comhb2.health22_x = 595
comhb2.difference1_x = 30

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
    
    answer = int(input("number"))
    
    userhb1.draw(screen)
    userhb1.move()
    
    comhb1.draw(screen)
    comhb2.move()

# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
# --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()






























