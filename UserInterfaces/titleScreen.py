# Supporting utilities
from miscUtils import which

## Function: Manage the Title screen user interface
#
#  @brief Start music, load title graphics and let user pick game type 
#  @return User command (new game or load game)
#
def menuTitleScreen(pygame, display, mixer):

    clock = pygame.time.Clock()    
    black = (0,0,0)

    # Starting the mixer with titlescreen music
    mixer.init() 
    mixer.music.load(which("TitleScreen.mp3"))
    mixer.music.set_volume(0.7) 
#    mixer.music.play(-1, 0 ) # Play infinite loop
    
    # define a variable to control the main loop
    running = True
    
    # Images
    imgTitle    = pygame.image.load(which("title.png"));
    imgNewGame  = pygame.image.load(which("newgame.png"));
    imgLoadGame = pygame.image.load(which("savedgame.png"));
    
    # Initial title image location
    x = 200
    y = 1
    display.blit(imgTitle, (x,y))
    pygame.display.update()
    
    # Move the title down slowly
    for y in range(1,150):
        display.fill(black)
        display.blit(imgTitle, (x,y))
        pygame.display.update()
        clock.tick(40) # Limit to 40 frames per sec
        
    
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
    
    