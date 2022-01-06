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
        Chip8.V[rand_reg_label_1] = random.randint(0, 255)
        NN = random.randint(0, 255)
        old_cpu_rand = Chip8.random_num

        test_opcode = 0xC
        test_opcode = (((test_opcode << 4) | rand_reg_label_1) << 8)
        test_opcode = test_opcode | NN

        Chip8.cycle(debug_instruction=test_opcode)
        assert Chip8.V[rand_reg_label_1] == old_cpu_rand & NN

        Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('CXNN: Test passed')

if __name__ == '__main__':
    run_test()