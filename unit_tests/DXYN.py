import random
import pygame
import sys
sys.path.append('../emulator')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

from chip8 import CPU
from display import Display

# NOTE - This test is for both 0xDXYN and 0x00E0 opcodes.
def run_test():

    save_stdout = sys.stdout
    sys.stdout = open('trash', 'w')

    d = Display()
    d.initialize_display()

    Chip8 = CPU(
        ROM_path='../emulator/ROMs/Pong.ch8',
        screen=d
    )

    for i in range(0x200):

        # Don't include 0xF
        reg_labels = [
            0x0, 0x1, 0x2, 
            0x3, 0x4, 0x5, 
            0x6, 0x7, 0x8, 
            0x9, 0xA, 0xB,
            0xC, 0xD, 0xE
        ]

        rand_reg_label_1 = random.choice(reg_labels)
        rand_reg_label_2 = random.choice(reg_labels)
        while rand_reg_label_2 == rand_reg_label_1:
            rand_reg_label_2 = random.choice(reg_labels)

        N = random.randint(1,8)
        Chip8.V[rand_reg_label_1] = random.randint(1,Chip8.screen.width-8)
        Chip8.V[rand_reg_label_2] = random.randint(1,Chip8.screen.height-N)

        test_opcode = 0xD
        test_opcode = ((((test_opcode << 4) | rand_reg_label_1) << 4) | rand_reg_label_2)
        test_opcode = (test_opcode << 4) | N

        Chip8.cycle(debug_instruction=test_opcode)
        assert Chip8.screen.get_pixel_at_coordinate(x=Chip8.V[rand_reg_label_1], y=Chip8.V[rand_reg_label_2]) == 1

        pygame.time.wait(2)
        
        Chip8.cycle(debug_instruction=0x00E0)
        assert Chip8.screen.get_pixel_at_coordinate(random.randint(1,63), y=random.randint(1,31)) == 0

        Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('DXYN: Test passed')

if __name__ == '__main__':
    run_test()