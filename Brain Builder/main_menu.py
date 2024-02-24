import pygame
from button.button import Button
from math_game.game import Game
from memory_game.memory_game import MGame
from guess_game.guess_game import VegetableFruitGame
from pygame import mixer



pygame.init()
screen_height= 800
screen_width = 1040

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brain Builders")

#font
font = pygame.font.SysFont("arialblack", 40)

#text colour
TEXT_COL = (255, 255, 255)

#images
guess_img = pygame.image.load("Assests/guess.png").convert_alpha()
math_img = pygame.image.load("Assests/Maths.png").convert_alpha()
memory_img = pygame.image.load("Assests/Memory.png").convert_alpha()
exit_img = pygame.image.load("Assests/cross.png").convert_alpha()
background_img = pygame.image.load("Assests/background.png").convert_alpha()

#load image
background_main = pygame.image.load('Assests/background.png')

#sound
mixer.music.load("Assests/background_audio.mp3")
mixer.music.play(-1)


#drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#button instances
Guess_button =  Button(385, 400 ,guess_img, 0.3)
Memory_button = Button(385,295, memory_img, 0.3)
Math_button = Button(385,504, math_img, 0.3)
Exit_button = Button(957, 32, exit_img, 0.3)


#game states
def math():
    pygame.display.set_caption("Brain Builders")

    while True:
        menupos = pygame.mouse.get_pos()
        done = False
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        # Create game object
        game = Game()
         # -------- Main Program Loop -----------
        while not done:
            # --- Process events (keystrokes, mouse clicks, etc)
            done = game.process_events()
            # --- Game logic should go here
            game.run_logic()
            # --- Draw the current frame
            game.display_frame(screen)
            # --- Limit to 30 frames per second
            clock.tick(30)
        pygame.quit()

def memory():
    game = MGame()
    game.run()
    

def guess():
    
    GGame = Game()
    if __name__ == "__main__":
        GGame = VegetableFruitGame()
        GGame.run()

def menu():
    running = True
    while running:

        menu_pos = pygame.mouse.get_pos()
        print(menu_pos)
        
        
        
        screen.fill((52,78,91))
        screen.blit(background_main, (0,0))
        
        
        #draw_text("GAME NAME", font, TEXT_COL, 362,142)
        Math_button.draw(screen)
        Guess_button.draw(screen)
        Memory_button.draw(screen)
        Exit_button.draw(screen)
        
        #event handler
        for event in pygame.event.get():
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Math_button.checkForInput(menu_pos):
                    
                    math()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Guess_button.checkForInput(menu_pos):
                    guess()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Memory_button.checkForInput(menu_pos):
                    memory()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Exit_button.checkForInput(menu_pos):
                    running = False
            
            if event.type == pygame.QUIT:
                running = False
        
        
        pygame.display.update()

    pygame.quit()



running = True
while running:

    menu_pos = pygame.mouse.get_pos()
    
    
    
    screen.fill((52,78,91))
    screen.blit(background_main, (0,0))
    
    
    #draw_text("GAME NAME", font, TEXT_COL, 362,142)
    Math_button.draw(screen)
    Guess_button.draw(screen)
    Memory_button.draw(screen)
    Exit_button.draw(screen)
    
    #event handler
    for event in pygame.event.get():
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Math_button.checkForInput(menu_pos):
                math()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Guess_button.checkForInput(menu_pos):
                guess()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Memory_button.checkForInput(menu_pos):
                memory()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Exit_button.checkForInput(menu_pos):
                running = False
        
        if event.type == pygame.QUIT:
           running = False
    
    
    pygame.display.update()

pygame.quit()