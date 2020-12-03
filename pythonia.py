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

# Game components
from UserInterfaces.titleScreen import menuTitleScreen
  
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    logo = pygame.image.load(which("winThumbnail.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pythonia the Game")
     
    # create a surface on screen that has the size of 1280 x 960
    display = pygame.display.set_mode((1280,960))
     
    # Launch Title screen
    menuTitleScreen(pygame, display, mixer)
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
    
    