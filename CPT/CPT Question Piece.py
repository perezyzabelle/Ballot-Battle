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
    
    #QUESTION BOX
    
    #Box
    pygame.draw.rect(screen, BLUE, [200, 100, 400, 60], 0)
    
    #"Q:"
    font = pygame.font.SysFont('Arial', 75, True, False)
    
    text = font.render("Q:", True, WHITE)
    
    screen.blit(text, [210, 105])
    
    #Question
    
    font = pygame.font.SysFont('Arial', 30, True, False)
    
    text = font.render("Who is Canada’s", True, WHITE)
    
    screen.blit(text, [300, 105])
    
    font = pygame.font.SysFont('Arial', 30, True, False)
    
    text = font.render("first Prime Minister?", True, WHITE)
    
    screen.blit(text, [300, 130])
    
    #FIRST ANSWER BOX
    
    #Box
    pygame.draw.rect(screen, BLUE, [200, 160, 400, 60], 4)
    
    #"A"
    font = pygame.font.SysFont('Arial', 75, True, False)
    
    text = font.render("A:", True, BLUE)
    
    screen.blit(text, [210, 165])
    
    #Answer
    font = pygame.font.SysFont('Arial', 30, True, False)
    
    text = font.render("John Aaron Macdonald", True, BLUE)
    
    screen.blit(text, [300, 185])
    
    #SECOND ANSWER BOX
    
    #Box
    pygame.draw.rect(screen, BLUE, [200, 220, 400, 60], 4)
    
    #"B"
    font = pygame.font.SysFont('Arial', 75, True, False)
    
    text = font.render("B:", True, BLUE)
    
    screen.blit(text, [210, 225])
    
    #Answer
    font = pygame.font.SysFont('Arial', 30, True, False)
    
    text = font.render("John Alex Macdonald", True, BLUE)
    
    screen.blit(text, [300, 245])
    
    #THIRD ANSWER BOX
    
    #Box
    pygame.draw.rect(screen, BLUE, [200, 280, 400, 60], 4)
    
    #"C"
    font = pygame.font.SysFont('Arial', 75, True, False)
    
    text = font.render("C:", True, BLUE)
    
    screen.blit(text, [210, 285])
    
    #Answer
    font = pygame.font.SysFont('Arial', 30, True, False)
    
    text = font.render("John Alexander Macdonald", True, BLUE)
    
    screen.blit(text, [280, 305])
    
    #FOURTH ANSWER BOX
    
    #Box
    pygame.draw.rect(screen, BLUE, [200, 340, 400, 60], 4)
    
    #"D"
    font = pygame.font.SysFont('Arial', 75, True, False)
    
    text = font.render("D:", True, BLUE)
    
    screen.blit(text, [210, 345])
    
    #Answer
    font = pygame.font.SysFont('Arial', 30, True, False)
    
    text = font.render("John Abraham Macdonald", True, BLUE)
    
    screen.blit(text, [290, 365])
    
    
    for event in pygame.event.get(): 
        if(event.type == pygame.mouse.get_pos()):
            x = pos [0]
            y = pos [1]
            if 200 < x < 600 and 160 < y < 220:
                pygame.draw.rect(screen, RED, [0, 0, 100, 100], 0)
            elif 200 < x < 600 and 220 < y < 280:
                pygame.draw.rect(screen, RED, [0, 0, 100, 100], 0)
        
            elif 200 < x < 600 and 280 < y < 340:
                pygame.draw.rect(screen, BLUE, [0, 0, 100, 100], 0)
        
            elif 200 < x < 600 and 340 < y < 400:
                pygame.draw.rect(screen, RED, [0, 0, 100, 100], 0)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

























