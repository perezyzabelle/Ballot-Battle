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
BLUE =  (0, 93, 155)

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

#CLASSES

#Class for Button

class Poster():
    
    def __init__ (self):
        
        #Class Attributes
        self.poster = pygame.image.load('/Users/carinaquijano/Downloads/Pyzo Assignments/Pics for Comsci CPT/Poster Image.jpg').convert_alpha()
        
        #Moving sticker's original positions
        self.poster_x = 0
        
        #Change in moving stickers
        self.changeposter_x = 0  
        
        #Class Methods
        
    def draw(self, screen):
        screen.blit(self.poster, [self.poster_x, self.poster_y])
    def move(self):
        
        #if user is right:
        if self.poster_x < 800:
            self.poster_x += self.changeposter_x
        elif self.poster_x > 800:
            self.poster_x += 0
            
        #if user is wrong:
        
#Class Button Objects / Instance 

poster1 = Poster()
poster1.poster_x = 200
poster1.poster_y = 400
poster1.changeposter_x = 20

poster2 = Poster()
poster2.poster_x = 200
poster2.poster_y = 466
poster2.changeposter_x = 15

poster3 = Poster()
poster3.poster_x = 200
poster3.poster_y = 532
poster3.changeposter_x = 10
 
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
    
    poster1.draw(screen)
    poster1.move()
    
    poster2.draw(screen)
    poster2.move()
  
    poster3.draw(screen)
    poster3.move()
  
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

























