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

class Sticker():
    
    def __init__ (self):
        
        #Class Attributes
        self.sticker = pygame.image.load('/Users/carinaquijano/Downloads/Pyzo Assignments/Pics for Comsci CPT/Vote Button.png').convert_alpha()
        
        #Moving sticker's original positions
        self.sticker_x = 0
        
        #Change in moving stickers
        self.changesticker_x = 0  
        
        #Class Methods
        
    def draw(self, screen):
        screen.blit(self.sticker, [self.sticker_x, self.sticker_y])
    def move(self):
        
        #if user is right:
        if self.sticker_x < 800:
            self.sticker_x += self.changesticker_x
        elif self.sticker_x > 800:
            self.sticker_x += 0
            
        #if user is wrong:
        
#Class Button Objects / Instance 

sticker1 = Sticker()
sticker1.sticker_x = 200
sticker1.sticker_y = 400
sticker1.changesticker_x = 20

sticker2 = Sticker()
sticker2.sticker_x = 200
sticker2.sticker_y = 466
sticker2.changesticker_x = 15

sticker3 = Sticker()
sticker3.sticker_x = 200
sticker3.sticker_y = 532
sticker3.changesticker_x = 10
 
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
    
    sticker1.draw(screen)
    sticker1.move()
    
    sticker2.draw(screen)
    sticker2.move()
  
    sticker3.draw(screen)
    sticker3.move()
  
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

























