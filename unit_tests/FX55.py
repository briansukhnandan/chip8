import random
import sys
sys.path.append('../emulator')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

from chip8 import CPU

def run_test():

    save_stdout = sys.stdout
    sys.stdout = open('trash', 'w')

    Chip8 = CPU(
        ROM_path='../emulator/ROMs/Pong.ch8',
        screen=None
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

        # V0 to Vx inclusive
        for i in range(rand_reg_label_1 + 1):
            Chip8.V[i] = random.randint(0, 255)

        test_opcode = 0xF
        test_opcode = ((test_opcode << 4) | rand_reg_label_1) << 8
        test_opcode = test_opcode | 0x55

        Chip8.cycle(debug_instruction=test_opcode)
        
        for i in range(rand_reg_label_1 + 1):
            assert Chip8.memory[Chip8.I + i] == Chip8.V[i]

        Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('FX55: Test passed')

if __name__ == '__main__':
    run_test()