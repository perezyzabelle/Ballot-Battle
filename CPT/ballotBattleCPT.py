import pygame
import os

print(os.getcwd())
pygame.init()
#screen scenes
scene = 0


#Because the questions code did not work, the acting with weapons did not work as well
#classes to attack
class Cupcake():
    
    def __init__ (self):
        
        #Class Attributes
        self.cupcake = pygame.image.load("cupcake.jpg")
        #Moving sticker's original positions
        self.cupcake_x = 0
        self.cupcake_y = 0
        #Change in moving stickers
        self.changecupcake_x = 0  
        
        self.changecupcakeWrong_x = 0
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
        if self.cupcake_x < 800:
            self.cupcake_x += self.changecupcakeWrong_x
        elif self.cupcake_x > 800:
            self.cupcake_x += 0
        
            
        
        
#Class cupcake Objects / Instance      
cupcake1 = Cupcake()
cupcake1.cupcake_x = 200
cupcake1.cupcake_y = 400
cupcake1.changecupcake_x = 20
cupcake1.changecupcakeWrong_x = -20

cupcake2 = Cupcake()
cupcake2.cupcake_x = 200
cupcake2.cupcake_y = 466
cupcake2.changecupcake_x = 15
cupcake2.changecupcakeWrong_x = -15


cupcake3 = Cupcake()
cupcake3.cupcake_x = 200
cupcake3.cupcake_y = 532
cupcake3.changecupcake_x = 10
cupcake3.changecupcakeWrong_x = -10


class Sticker():
    
    def __init__ (self):
        
        #Class Attributes
        self.sticker = pygame.image.load("voteSticker.png")
        
        #Moving sticker's original positions
        self.sticker_x = 0
        self.sticker_y = 0
        
        #Change in moving stickers
        self.changesticker_x = 0  
        self.changeposterWrong_x = 0
        
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
        if self.sticker_x < 800:
            self.sticker_x += self.changestickerWrong_x
        elif self.sticker_x > 800:
            self.sticker_x += 0
        
#Class sticker Objects / Instance 

sticker1 = Sticker()
sticker1.sticker_x = 200
sticker1.sticker_y = 400
sticker1.changesticker_x = 20
sticker1.changestickerWrong_x =-20

sticker2 = Sticker()
sticker2.sticker_x = 200
sticker2.sticker_y = 466
sticker2.changesticker_x = 15
sticker2.changestickerWrong_x =-15

sticker3 = Sticker()
sticker3.sticker_x = 200
sticker3.sticker_y = 532
sticker3.changesticker_x = 10
sticker3.changestickerWrong_x =-10

class Poster():
    
    def __init__ (self):
        
        #Class Attributes
        self.poster = pygame.image.load("poster.jpg")
        
        #Moving sticker's original positions
        self.poster_x = 0
        self.poster_y = 0
        #Change in moving stickers
        self.changeposter_x = 0  
        self.changeposterWrong_x = 0
        
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
        if self.poster_x < 800:
            self.poster_x += self.changeposterWrong_x
        elif self.poster_x > 800:
            self.poster_x += 0
        
#Class Button Objects / Instance 

poster1 = Poster()
poster1.poster_x = 200
poster1.poster_y = 400
poster1.changeposter_x = 20
poster1.changeposterWrong_x = -20

poster2 = Poster()
poster2.poster_x = 200
poster2.poster_y = 466
poster2.changeposter_x = 15
poster2.changeposterWrong_x = -15

poster3 = Poster()
poster3.poster_x = 200
poster3.poster_y = 532
poster3.changeposter_x = 10
poster3.changeposterWrong_x = -10
 


#subprograms to draw each scene
#home screen
def homeScene():
    background1 = pygame.image.load("startingBackground1.jpg")
    playButton = pygame.image.load("playButton.gif")
    screen.blit(background1,[0, 0])
    screen.blit(playButton,[225, 300])
    
#scenes to select character,weapon and background
def selectCharScene():
    background1 = pygame.image.load("startingBackground1.jpg")
    screen.blit(background1,[0, 0])
   
    font = pygame.font.Font(None,60)
    text = font.render("Choose a Character", True, WHITE)
    screen.blit(text, [100,100])
   
    andrewScheer1 = pygame.image.load("andrewScheer1.jpg")
    screen.blit(andrewScheer1,[125, 300])
    justinTrudeau1 = pygame.image.load("justinTrudeau1.jpg")
    screen.blit(justinTrudeau1,[275, 300])
    yvesFrancois1 = pygame.image.load("yvesFrancois1.jpg")
    screen.blit(yvesFrancois1,[425, 300])
    jagmeetSingh1 = pygame.image.load ("jagmeetSingh1.jpg")
    screen.blit(jagmeetSingh1,[575, 300])

def selectWeaponScene():
    background1 = pygame.image.load("startingBackground1.jpg")
    screen.blit(background1,[0, 0])
    
    font = pygame.font.Font(None,60)
    text = font.render("Choose a weapon", True, WHITE)
    screen.blit(text, [100,100])
    
    cupcake = pygame.image.load("cupcake.jpg")
    screen.blit(cupcake,[125,300])
    voteSticker = pygame.image.load("voteSticker.png")
    screen.blit(voteSticker,[325,300])
    poster = pygame.image.load("poster.jpg")
    screen.blit(poster,[525,300])

def selectBackgroundScene():
    background1 = pygame.image.load("startingBackground1.jpg")
    screen.blit(background1,[0, 0])
    
    font = pygame.font.Font(None,60)
    text = font.render("Choose a background", True, WHITE)
    screen.blit(text, [100,100])
    
    sea = pygame.image.load("underTheSea.jpg")
    screen.blit(sea,[150,300])
    forest = pygame.image.load("forest.jpg")
    screen.blit(forest,[325,300])
    town = pygame.image.load("town.png")
    screen.blit(town,[525,300])
    
    

#user's selection subprograms
def selectChar(x, y):
    character = "None"
    if 125 < x < 225 and 300 < y < 400:
        character = "Andrew Scheer"
    elif 275 < x < 375 and 300 < y < 400:
        character = "Justin Trudeau"
    elif 425 < x < 525 and 300 < y < 400:
        character = "Yves Francois"
    elif 575 < x < 675 and 300 < y < 400:
        character = "Jagmeet Singh"
    
    return character
    
def selectWeapon(x,y):
    weapon = "None"
    if 125 < x < 275 and  300 < y < 400:
        weapon = "cupcake"
    elif 325 < x < 425 and 300 < y < 400:
        weapon = "voteSticker"
    elif 525 < x < 625 and 300 < y < 400:
        weapon = "poster"
    
    return weapon

def selectBackground(x,y):
    background = "None"
    if 150 < x < 250 and 300 < y < 400:
        background = "sea"
    elif 325 < x < 425 and 300 < y < 400:
        background = "forest"
    elif 575 < x < 675 and 300 < y < 400:
        background = "town"
    
    
    return background
    
#Loading character, weapon and background
def loadCharacter(character):
    charLoad = "None"
    if (character == "Andrew Scheer"):
        charLoad = pygame.image.load("andrewScheer1.jpg")
    elif (character == "Justin Trudeau"):
        charLoad = pygame.image.load("justinTrudeau1.jpg")
    elif (character == "Yves Francois"):
        charLoad = pygame.image.load("yvesFrancois1.jpg")
    elif (character == "Jagmeet Singh"):
        charLoad = pygame.image.load ("jagmeetSingh1.jpg")
    
    return charLoad

def loadWeapon(weapon):
    weaponLoad = "None"
    if (weapon == "cupcake"):
        weaponLoad = pygame.image.load("cupcake.jpg")
    elif (weapon =="voteSticker"):
        weaponLoad = pygame.image.load("voteSticker.png")
    elif (weapon == "poster"):
        weaponLoad = pygame.image.load("poster.jpg")
    
    return weaponLoad

def loadBackground (background):
    backgroundLoad = "None"
    if (background =="sea"):
        backgroundLoad = pygame.image.load("underTheSeaBattle.jpg")
    elif (background =="forest"):
        backgroundLoad = pygame.image.load("forestBattle.jpg")
    elif (background =="town"):
        backgroundLoad = pygame.image.load("townBattle.png")
    
    return backgroundLoad


#load CPU character
def loadCPU (character):
    cpuCharacter = "None"
    if (character == "Andrew Scheer"):
        cpuCharacter = pygame.image.load("jagmeetSingh1.jpg")  #how do i make the options randomized?
    elif (character == "Justin Trudeau"):
        cpuCharacter = pygame.image.load("jagmeetSingh1.jpg")   #rand int = if cpuCharacter = 1, print this guy
    elif (character == "Yves Francois"):
        cpuCharacter = pygame.image.load("jagmeetSingh1.jpg")
    elif (character == "Jagmeet Singh"):
        cpuCharacter = pygame.image.load("justinTrudeau1.jpg")
    
    return cpuCharacter
    


    
#draw the stick figures of all characters
def drawStickFig (screen,x,y,):
        pygame.draw.line(screen, BLACK, [100 + x, 460 + y], [100+ x,600+ y], 10 )
        pygame.draw.line(screen, BLACK, [0+ x, 480+ y], [100+ x, 530+ y], 10 )
        pygame.draw.line(screen, BLACK, [200+ x, 480+ y], [100+ x, 530+ y], 10 )

#draw health bars
def drawHealthBars():
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

#--questions--

#draw the question and answer
class QuestionRectangleFill():
    def __init__(self):
        #attributes for questionImage
        
        #rectangle image
        self.x = 0
        self.y = 0
        
        #rectangle size
        self.width = 0
        self.height = 0
        
        #colour
        self.colour = [255,255,255]
      
    #class methods
    def draw(self):
        pygame.draw.rect(screen,self.colour,[self.x,self.y,self.width,self.height],0)
        

#instances for rectangle
fillRectangleQ = QuestionRectangleFill() # "Q" means the question box
fillRectangleQ.x = 200
fillRectangleQ.y = 100
fillRectangleQ.width = 400
fillRectangleQ.height = 60
fillRectangleQ.colour = [0,93,155]

fillRectangle1 = QuestionRectangleFill()
fillRectangle1.x = 200
fillRectangle1.y = 160                      #the rest are answer boxes
fillRectangle1.width = 400
fillRectangle1.height = 60
fillRectangle1.colour = [255,255,255]

fillRectangle2 = QuestionRectangleFill()
fillRectangle2.x = 200
fillRectangle2.y = 220
fillRectangle2.width = 400
fillRectangle2.height = 60
fillRectangle2.colour = [255,255,255]

fillRectangle3 = QuestionRectangleFill()
fillRectangle3.x = 200
fillRectangle3.y = 280
fillRectangle3.width = 400
fillRectangle3.height = 60
fillRectangle3.colour = [255,255,255]

fillRectangle4 = QuestionRectangleFill()
fillRectangle4.x = 200
fillRectangle4.y = 340
fillRectangle4.width = 400
fillRectangle4.height = 60
fillRectangle4.colour = [255,255,255]


class QuestionRectangleOutline():
    def __init__(self):
        #attributes for questionImage
        
        #rectangle image
        self.x = 0
        self.y = 0
        
        #rectangle size
        self.width = 0
        self.height = 0
      
    #class methods
    def draw(self):
        pygame.draw.rect(screen,BLUE,[self.x,self.y,self.width,self.height],2)
        

#instances for rectangle
rectangleQ = QuestionRectangleOutline()
rectangleQ.x = 200
rectangleQ.y = 100
rectangleQ.width = 400
rectangleQ.height = 60

rectangle1 = QuestionRectangleOutline()
rectangle1.x = 200
rectangle1.y = 160
rectangle1.width = 400
rectangle1.height = 60

rectangle2 = QuestionRectangleOutline()
rectangle2.x = 200
rectangle2.y = 220
rectangle2.width = 400
rectangle2.height = 60

rectangle3 = QuestionRectangleOutline()
rectangle3.x = 200
rectangle3.y = 280
rectangle3.width = 400
rectangle3.height = 60

rectangle4 = QuestionRectangleOutline()
rectangle4.x = 200
rectangle4.y = 340
rectangle4.width = 400
rectangle4.height = 60


def firstQAText():
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
    #"A"
    font = pygame.font.SysFont('Arial', 75, True, False)
    text = font.render("A:", True, BLUE)    
    screen.blit(text, [210, 165])    
    #Answer
    font = pygame.font.SysFont('Arial', 30, True, False)    
    text = font.render("John Aaron Macdonald", True, BLUE)    
    screen.blit(text, [300, 185])
    #"B"
    font = pygame.font.SysFont('Arial', 75, True, False)    
    text = font.render("B:", True, BLUE)    
    screen.blit(text, [210, 225])    
    #Answer
    font = pygame.font.SysFont('Arial', 30, True, False)    
    text = font.render("John Alex Macdonald", True, BLUE)    
    screen.blit(text, [300, 245])
    #"C"
    font = pygame.font.SysFont('Arial', 75, True, False)    
    text = font.render("C:", True, BLUE)    
    screen.blit(text, [210, 285])    
    #Answer
    font = pygame.font.SysFont('Arial', 30, True, False)    
    text = font.render("John Alexander Macdonald", True, BLUE)    
    screen.blit(text, [280, 305])
    #"D"
    font = pygame.font.SysFont('Arial', 75, True, False)    
    text = font.render("D:", True, BLUE)    
    screen.blit(text, [210, 345])    
    #Answer
    font = pygame.font.SysFont('Arial', 30, True, False)    
    text = font.render("John Abraham Macdonald", True, BLUE)    
    screen.blit(text, [290, 365])



    

question = [
"1. Who is Canada’s first Prime Minister?",
"2. Where are liberal parties on the political spectrum?",
"3. What is a campaign?",
"4. Which party does Justin Trudeau belong to?",
"5. What party does Jagmeet Singh belong to?",

]

def getAnswer(question,x,y):
    answer = "None"
    if (question[0]):
    
    
        # C.John Alexander Macdonald"
        answer = 200 < x < 400 and 280 < y < 340
    

    return answer

def determineCorrect(question,answer):
    result = "Incorrect"
    if question[0]:
        if (answer == 200 < x < 400 and 280 < y < 340):
            result = "Correct"
        
    return result
    
#code was not working when we called the getAnswer and determineCorrect subprogram for one question so we did not write the other questions
    

        
    
    

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128,128,128)
BLUE = (0,93,155)
 

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Election")
 
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
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            
            #switching scenes
            if scene == 0:
                if 225 < x < 425 and 300 < y < 400:
                    scene = 1
            
            elif (scene ==1):
                characterName = selectChar(x, y)
                characterImage = loadCharacter(characterName)
                cpuCharacterImage = loadCPU(characterName)
                if (characterImage != "None"):
                    scene = 2
               
            elif (scene ==2):
                weaponName = selectWeapon(x,y)
                weaponImage = loadWeapon(weaponName)
                if (weaponImage !="None"):
                    scene = 3
             
            elif (scene == 3):
                backgroundName = selectBackground(x,y)
                backgroundImage = loadBackground(backgroundName)
                if (backgroundImage != "None"):
                    scene = 4
            elif (scene == 4):
                userAnswer0 = getAnswer(question[0],x,y)
                answerResult = determineCorrect(question[0],userAnswer0)
                if (answerResult == "Correct"):
                    print (answerResult)
                    scene = 5
            
                
        
                    
            
            
             
            
                
            
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.  
    
    
    # --- Drawing code should go here
    if (scene == 0):
        homeScene()
    elif (scene == 1):
        selectCharScene()
    elif (scene == 2):
        selectWeaponScene()
    elif (scene == 3):
        selectBackgroundScene()
    elif (scene == 4):
        
        if (backgroundImage != "None"):
            screen.blit(backgroundImage,[0,0])
            drawHealthBars()
            #draw Question box
            fillRectangleQ.draw()
            fillRectangle1.draw()
            fillRectangle2.draw()
            fillRectangle3.draw()
            fillRectangle4.draw()
            rectangleQ.draw()
            rectangle1.draw()
            rectangle2.draw()
            rectangle3.draw()
            rectangle4.draw()
            firstQAText()
           
            
        if (characterImage != "None"):
            drawStickFig(screen,0,0)
            screen.blit(characterImage,[50,350])
            drawStickFig(screen,600,30)
            screen.blit(cpuCharacterImage, [650,350])
            
        if (weaponImage != "None"):
            screen.blit(weaponImage,[170,400])
            
    elif (scene == 5):
        if (backgroundImage != "None"):
            screen.blit(backgroundImage,[0,0])
            drawHealthBars()
            
        if (characterImage != "None"):
            drawStickFig(screen,0,0)
            screen.blit(characterImage,[50,350])
            drawStickFig(screen,600,30)
            screen.blit(cpuCharacterImage, [650,350])
            
        if (weaponImage != "None"):
            screen.blit(weaponImage,[170,400])
            if (weaponImage == "cupcake"):
                cupcake1.draw()
                cupcake1.move()
                cupcake2.draw()
                cupcake2.move()
                cupcake3.draw()
                cupcake3.move()
            elif ( weaponImage == "sticker"):
                sticker1.draw()
                sticker1.move()
                sticker2.draw()
                sticker2.move()
                sticker3.draw()
                sticker3.move()
            elif (weaponImage=="poster"):
                poster1.draw()
                poster1.move()
                poster2.draw()
                poster2.move()
                poster3.draw()
                poster3.move()
                
            
         #the intention was for the character or CPU to shoot their weapon across the screen, but the scene would not change as the mouse selectioncode did not work
                
           
          
            
        
   
        
        
        
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()