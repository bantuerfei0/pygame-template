'''
NOTE: This file is a really bad case of overcommenting and actual
commenting does not need to look like this. Only comment if the 
function of a block of code is not immediately apparent
'''
import pygame

pygame.init() # initialize pygame

# variables that are constant are usually all uppercase in Python conventions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FLAGS = 0 # Window flags, see https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

# creates a window with the given parameters
# this "main_screen" Surface (what pygame calls it) object is your visible canvas that you must draw on
main_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), FLAGS)

# sets the window title
pygame.display.set_caption('pygame-template')

# sets the window's icon, takes in another Surface object. Not implemented in template.
#pygame.display.set_icon()

clock = pygame.time.Clock() # used for various time features, but mainly for keeping a steady framerate (see later)

done = False # a boolean-type variable to dictate program execution

# the "not" operator flips a False to True and True to False
while not done:
    
    # every single time this is called, pygame "polls" the inputs it received between the last frame and this frame
    # we're just looping through them here
    for event in pygame.event.get():
        # UNCOMMENT THIS IF YOU WANT TO SEE WHAT EVENTS ARE BEING BROUGHT IN
        #print(event)
        
        # if the event's type is pygame.QUIT (a constant defined in pygame)
        if event.type == pygame.QUIT:
            done = True # this causes pygame to exit on the next loop
    
    # get the time in milliseconds between the previous frame and this frame
    delta_time = clock.get_time() # useful for calculations that need to remain consistent; even at a different fps

    # UNCOMMENT THIS CODE TO SEE WHAT IT DOES!
    #main_screen.fill((255, 255, 255)) # fill the main screen with white
    #pygame.draw.rect(main_screen, (255, 0, 0), (0, 0, 500, 500)) # draws a red rectangle on main_screen starting at (0, 0) and going to (500,500)

    pygame.display.flip() # redraws the frame on the main window with what is on main_screen
    
    # pause the program long enough to hit 60 fps
    clock.tick(60) # pauses the program until it should run again to keep a steady framerate

pygame.quit() # uninitializes pygame (not needed? but wouldn't hurt to be safe)