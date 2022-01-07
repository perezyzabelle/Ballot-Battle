#
#FOR ANY GRAPHICS FOUND ONLINE, REFER TO ROSTERS---
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =  (0, 93, 155)

#CLASSES 

#Class for winner 

class Winner:
    pos = []
    colour = (0, 0, 0)
    
    #Subprogram to draw Winner 
    def draw(self):
        pygame.draw.line(scree, BLACK, [], [], 3)

#Class for loser
 
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
   
    losing_bg = pygame.image.load('/Users/carinaquijano/Downloads/Pyzo Assignments/Pics for Comsci CPT/Losing Scene.jpg').convert()
    
    screen.blit(losing_bg, [0, 0])
 
    # --- Drawing code should go here
    
    #LOSING SCENE 
    
    #Character Image
    
    Justin_pic = pygame.image.load('/Users/carinaquijano/Downloads/Pyzo Assignments/Pics for Comsci CPT/JT Sad.png').convert_alpha()
    screen.blit(Justin_pic, [600, 320])

    pygame.draw.line(screen, WHITE, [650, 420], [650, 480], 8 )
    
    pygame.draw.line(screen, WHITE, [650, 480], [620, 540], 8 )
 
    pygame.draw.line(screen, WHITE, [650, 480], [680,540], 8 )    
    
    pygame.draw.polygon(screen, WHITE, [(650, 440), (700, 460), (650, 480), (600, 460)], 8 )
  
    #Play again texts
    
    #"Play again"
    
    font = pygame.font.SysFont('Arial', 65, True, False)
    
    text = font.render("Play again?", True, WHITE)
    
    screen.blit(text, [150, 350])

    #"Yes"
    
    
    font = pygame.font.SysFont('Arial', 60, True, False)
    
    text = font.render("Yes", True, WHITE)
    
    screen.blit(text, [250, 410])

    #"No"
    
    
    font = pygame.font.SysFont('Arial', 60, True, False)
    
    text = font.render("No", True, WHITE)

    screen.blit(text, [260, 460])
    
    #"You lose !!"
    
    font = pygame.font.SysFont('Arial', 100, True, False)
    
    text = font.render("You lose !!", True, WHITE)

    screen.blit(text, [150, 50])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

























