import pygame

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

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
        self.off_pixel_colors = pygame.Color(0, 0, 0, 255)
        self.on_pixel_colors = pygame.Color(250, 250, 250, 255)

        '''
        Scale would resize the display to (64x32) * scale (associative).
        '''
        self.scale = 10

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
            size=(self.width * self.scale, self.height * self.scale),
            flags=pygame.HWSURFACE | pygame.DOUBLEBUF,
            depth=self.depth
        )
        
        '''After init all our parameters, clear and update the display.'''
        self.clear_screen()
        self.update()

    def draw_single_pixel(self, x, y, c):

        '''
        Draws a single pixel to the screen. We need to wrap this
        function within another in our DXYN opcode to actually draw it
        though.

        c will be 0/1 to determine whether our selected color is off/on.
        '''
        if c == 0:
            p_color = self.off_pixel_colors
        else: 
            p_color = self.on_pixel_colors

        x_lower_left = x * self.scale
        y_lower_left = y * self.scale

        # print('Got here')

        # TESTING ONLY
        # pygame.draw.rect(
        #     surface=self.surface,
        #     color=self.on_pixel_colors,
        #     rect=(x_lower_left, y_lower_left, self.scale, self.scale)
        # )

        pygame.draw.rect(
            surface=self.surface,
            color=p_color,
            rect=(x_lower_left, y_lower_left, self.scale, self.scale)
        )

    def clear_screen(self):

        '''Clearing the surface is basically setting all pixels to off state.'''
        self.surface.fill(self.off_pixel_colors)

    def get_pixel_at_coordinate(self, x, y):

        x_lower_left = x * self.scale
        y_lower_left = y * self.scale

        p_color = self.surface.get_at((x_lower_left, y_lower_left))

        color = 0 if p_color == self.off_pixel_colors else 1
        return color

    '''
    These two methods below pertain to our pygame display which
    should be static as we do not want multiple of them running in
    a single session with our CPU.
    '''

    @staticmethod
    def update():
        pygame.display.flip()

    @staticmethod
    def destroy():
        pygame.display.quit()
