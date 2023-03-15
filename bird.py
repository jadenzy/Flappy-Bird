import pygame
import random
import sys
# Initialize Pygame
pygame.init()

# Set up the window
win_width = 400
win_height = 600
win = pygame.display.set_mode((win_width, win_height)) #Mind the double () here because set_mode function can take four argument
pygame.display.set_caption("Flappy Bird") # set the window name 

# Set up the colors
bg_color = (135, 206, 250)  # sky blue
bird_color = (255, 255, 0)  # yellow
pipe_color = (34, 139, 34)  # forest green

# Set up the font throught out the progrom 
font = pygame.font.SysFont(None, 30) 

# Set up the bird
bird_size = 20 #the size 
bird_x = 50 #The x position 
bird_y = 250 #The y position 
bird_vel = 0 #The speed that is going down 
bird_acc = 1 #How fast the bird is going down 

# Set up the pipes
pipe_width = 50 
pipe_gap = random.randint(100, 150) # The gap between top and bottom 
pipe_x = win_width
pipe_y_top = random.randint(100, 400) # Its top part 
pipe_y_bottom = pipe_y_top + pipe_gap # Its bottom part 
pipe_vel = 6 #How fast is each pipe moving across the screen, you can modify this part to make the game harder 

# Set up the score
score = 0

# Set up the game states
game_start = False
game_over = False

# Define the functions
def draw_bird(): #Draw the bird on the screen, which is only going up and down 
    pygame.draw.rect(win, bird_color, (bird_x, bird_y, bird_size, bird_size))

def draw_pipe(pipe_x, pipe_y_top, pipe_y_bottom): #Draw the pipes on the screen, here is when the perivous one disappear, then the next one will show up 
    pygame.draw.rect(win, pipe_color, (pipe_x, 0, pipe_width, pipe_y_top)) #Draw the top one 
    pygame.draw.rect(win, pipe_color, (pipe_x, pipe_y_bottom, pipe_width, win_height - pipe_y_bottom)) #Draw the bottom one 

def draw_score(): #The score on the screen 
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    win.blit(text, (10, 10))

def game_start_screen(): #The start menu 
    text = font.render("Press Space to Start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(win_width/2, win_height/2))
    win.blit(text, text_rect)

def game_over_screen(score): #Game over menu 
    text = font.render("Game Over! Press Space to Play Again", True, (0, 0, 0))
    text_rect = text.get_rect(center=(win_width/2, win_height/2))
    text_socre = font.render("Your score is: " + str(score), True, (0,0,0))
    textscore_rect = text_socre.get_rect(center=(win_width/2, win_height/3))
    win.blit(text, text_rect)
    win.blit(text_socre, textscore_rect)
    

def reset_game(): #Function use to reset every variables to its defualt 
    global bird_y, bird_vel, score, pipe_x, pipe_y_top, pipe_y_bottom, game_over
    bird_y = 250
    bird_vel = 0
    score = 0
    pipe_x = win_width
    pipe_y_top = random.randint(100, 400)
    pipe_y_bottom = pipe_y_top + pipe_gap
    game_over = False

# Set up the game loop
clock = pygame.time.Clock() #The a clock varibale to set the fps 
run = True

while run:
    clock.tick(30) # Call the clock varibale to set fps to 30
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #When you click the cross on top of the window 
            run = False #Then Exit 
            sys.exit() # Ensure the program is shutdown 
        if event.type == pygame.KEYDOWN: #When user is pressing a key 
            if event.key == pygame.K_SPACE: #If it is space bar 
                if not game_over: #If is in game 
                    bird_vel = -10 #Control the bird to move up and down 
                if not game_start: #If is in the start menu 
                    game_start = True #Then start the game 
                if game_over: #If is in the gameover menu 
                    reset_game() #Restart the game 

    # Update the game
    if game_start and not game_over:
        # Update the bird
        bird_vel += bird_acc
        bird_y += bird_vel

        # Update the pipes
        pipe_x -= pipe_vel
        if pipe_x < -pipe_width:
            pipe_x = win_width
            pipe_y_top = random.randint(100, 400)
            pipe_y_bottom = pipe_y_top + pipe_gap
            score += 1

    # Check for collisions
    if bird_y < 0 or bird_y > win_height - bird_size or (bird_x + bird_size > pipe_x and bird_x < pipe_x + pipe_width and (bird_y < pipe_y_top or bird_y + bird_size > pipe_y_bottom)):
        game_over = True

# Draw the graphics
    win.fill(bg_color)

# Draw the start menu 
    if not game_start:
        game_start_screen()

# Draw the bird and pipes
    if not game_over:
        draw_pipe(pipe_x, pipe_y_top, pipe_y_bottom)

        draw_bird()
        draw_score()
    else:
        game_over_screen(score)
    
# Keep updating the dispaly 
    #Use one of them to fix your need 
    pygame.display.update() # This will update the specific area if given an argument 
    #pygame.display.flip() #This will update the entire screen and no argument can be input 

