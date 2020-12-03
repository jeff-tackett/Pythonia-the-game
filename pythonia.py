# import the pygame module, so you can use it
import pygame
import os
import sys

# Main directories
musicDir = os.path.join(os.getcwd(), "Resources", "Music", "");
imageDir = os.path.join(os.getcwd(), "Resources", "Images", "");
utilDir  = os.path.join(os.getcwd(), "Utils", "");
sys.path.insert(1, musicDir);
sys.path.insert(1, imageDir);
sys.path.insert(1, utilDir);

# audio
from pygame import mixer 

# Supporting utilities
from miscUtils import which
 
  
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    
    # Starting the mixer with titlescreen music
    mixer.init() 
    mixer.music.load(which("TitleScreen.mp3"))
    mixer.music.set_volume(0.7) 
    mixer.music.play(-1, 0 ) # Play infinite loop

    # load and set the logo
    logo = pygame.image.load(which("winThumbnail.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pythonia the Game")
     
    # create a surface on screen that has the size of 640 x 480
    screen = pygame.display.set_mode((640,480))
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                mixer.music.stop()
                pygame.display.quit()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
    
    