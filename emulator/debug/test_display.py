import sys
sys.path.append("..")

from chip8 import CPU
from display import Display

import pygame

TIMER = pygame.USEREVENT + 1

def test_screen():

    # while 1:
    d = Display()
    d.initialize_display()

    Chip8 = CPU(
        ROM_path='../ROMs/Pong.ch8',
        screen=d
    )

    pygame.init()

    opcode_test = [
        0x00E0
    ]

    while Chip8.is_running:

        pygame.time.wait(5000)
        Chip8.execute_current_opcode(debug_instruction=opcode_test[0])

        for event in pygame.event.get():
            if event.type == TIMER:
                # Decrement sound/delay timers.
                pass

            if event.type == pygame.QUIT:
                Chip8.stop_CPU()

            if event.type == pygame.KEYDOWN:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_ESCAPE]:
                    Chip8.stop_CPU()


if __name__ == '__main__':
    test_screen()