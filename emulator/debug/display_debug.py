import sys
sys.path.append("..")

from chip8 import CPU
from display import Display

import pygame

TIMER = pygame.USEREVENT + 1

def test_screen():

    d = Display()
    d.initialize_display()

    Chip8 = CPU(
        ROM_path='../ROMs/chip8-test-rom.ch8',
        screen=d
    )

    pygame.init()

    opcode_test = [
        0x00E0, # Clear screen
        0x6210, # Load 16 into V2
        0x8320, # Set V3 = V2 (16)
        0xD238, # Draw a pixel at (16,16) of height 5.
    ]

    for i in opcode_test:
        pygame.time.wait(3000)
        Chip8.execute_current_opcode(debug_instruction=i)

    pygame.time.wait(3000)
    
    # while Chip8.is_running:

    #     pygame.time.wait(5000)
    #     Chip8.execute_current_opcode(debug_instruction=opcode_test[0])

    #     for event in pygame.event.get():
    #         if event.type == TIMER:
    #             Chip8.update_timers()

    #         if event.type == pygame.QUIT:
    #             Chip8.stop_CPU()

    #         if event.type == pygame.KEYDOWN:
    #             keys_pressed = pygame.key.get_pressed()
    #             if keys_pressed[pygame.K_ESCAPE]:
    #                 Chip8.stop_CPU()


if __name__ == '__main__':
    test_screen()