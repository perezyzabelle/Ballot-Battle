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

class Cupcake():
    
    def __init__ (self):
        
        #Class Attributes
        self.cupcake = pygame.image.load("cupcake.jpg")
        
        #Moving sticker's original positions
        self.cupcake_x = 0
        
        #Change in moving stickers
        self.changecupcake_x = 0  
        
        #Class Methods
        
    def draw(self, screen):
        screen.blit(self.cupcake, [self.cupcake_x, self.cupcake_y])
    def move(self):
        
        #if user is right:
        if self.cupcake_x < 800:
            self.cupcake_x += self.changecupcake_x
        elif self.cupcake_x > 800:
            self.cupcake_x += 0
            
        #if user is wrong:
        
#Class Button Objects / Instance 

cupcake1 = Cupcake()
cupcake1.cupcake_x = 200
cupcake1.cupcake_y = 400
cupcake1.changecupcake_x = 20

cupcake2 = Cupcake()
cupcake2.cupcake_x = 200
cupcake2.cupcake_y = 466
cupcake2.changecupcake_x = 15

cupcake3 = Cupcake()
cupcake3.cupcake_x = 200
cupcake3.cupcake_y = 532
cupcake3.changecupcake_x = 10
 
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
    
    cupcake1.draw(screen)
    cupcake1.move()
    
    cupcake2.draw(screen)
    cupcake2.move()
  
    cupcake3.draw(screen)
    cupcake3.move()
  
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

























