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
    
    winning_bg = pygame.image.load('/Users/carinaquijano/Downloads/Pyzo Assignments/Pics for Comsci CPT/Winning Scene.jpg').convert()
    
    screen.blit(winning_bg, [0, 0])
  
    # --- Drawing code should go here
    
    #WINNING SCENE 
    
    #Character Image
    
    #In this next piece of code, I had the help from a website, that had the face's cropped image not have a black background from it's transparency. We borrowed the piece "_alpha". 
    
    #The link to the website is: https://stackoverflow.com/questions/20312032/how-do-i-cut-the-black-things-out-of-an-image-in-pygame
     
    Justin_pic = pygame.image.load('/Users/carinaquijano/Downloads/Pyzo Assignments/Pics for Comsci CPT/Justin Trudeau.png').convert_alpha()
    screen.blit(Justin_pic, [100, 200])
    
    pygame.draw.line(screen, BLACK, [200, 460], [200,600], 10 )
    
    pygame.draw.line(screen, BLACK, [50, 480], [200, 530], 10 )
    
    pygame.draw.line(screen, BLACK, [350, 480], [200, 530], 10 )
    
    #Play again texts
    
    #"Play again"
    
    font = pygame.font.SysFont('Arial', 65, True, False)
    
    text = font.render("Play again?", True, BLUE)
    
    screen.blit(text, [450, 350])
    
    #"Yes"
    
    
    font = pygame.font.SysFont('Arial', 60, True, False)
    
    text = font.render("Yes", True, BLUE)
    
    screen.blit(text, [550, 410])
    
    #"No"
    
    
    font = pygame.font.SysFont('Arial', 60, True, False)
    
    text = font.render("No", True, BLUE)
    
    screen.blit(text, [560, 460])
   
   #"You win !!"
   
    font = pygame.font.SysFont('Arial', 100, True, False)
    
    text = font.render("You win !!", True, BLUE)

    screen.blit(text, [150, 50])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

























