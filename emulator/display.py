import pygame

class Display:

    def __init__(self):

        '''
        This screen is 32x64.
        Depth of the screen is # of bits of pixel color.
        A pygame surface is used to represent an image.
        '''
        self.height = 32
        self.width = 64
        self.depth = 8
        self.surface = None

        '''
        Chip8 is simple in that there are only 2 colors, black and white.
        Black is used for when a pixel is in the off state, and conversely,
        White is used for when a pixel is on the on state.
        '''
        self.off_pixel_colors = pygame.Color(0,0,0,255)
        self.on_pixel_colors = pygame.Color(250,250,250,255)

    def initialize_display(self):
        
        '''
        With pygame, we first initialize our display and then worry about
        setting the mode.

        Surface Mode parameters -
            size - Our size width/height.
            flags - Double Buffering so that we have no flickering on the display.
            depth - Our depth of pixel color.
        '''
        pygame.display.init()
        pygame.display.set_caption('Chip8')

        self.surface = pygame.display.set_mode(
            size=(self.width, self.height),
            flags=pygame.HWSURFACE | pygame.DOUBLEBUF
            depth=self.depth,
        )
        
        '''After init all our parameters, clear and update the display.'''
        self.clear_screen()
        self.update()

    def clear_screen(self):

        '''Clearing the surface is basically setting all pixels to off state.'''
        self.surface.fill(self.off_pixel_colors)


    '''
    These two methods below pertain to our pygame display which
    should be static as we do not want multiple of them running in
    a single session with our CPU.
    '''

    @staticmethod
    def update()
        pygame.display.flip()

    @staticmethod
    def destroy():
        pygame.display.quit()
