import sys
import random
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

        rand_reg_label_2 = random.choice(reg_labels)
        while rand_reg_label_2 == rand_reg_label_1:
            rand_reg_label_2 = random.choice(reg_labels)

        Chip8.V[rand_reg_label_1] = random.randint(0, 127)
        tmp = Chip8.V[rand_reg_label_1]

        test_opcode = 0x8
        test_opcode = ((((test_opcode << 4) | rand_reg_label_1) << 4) | rand_reg_label_2)
        test_opcode = (test_opcode << 4) | 0xE

        Chip8.cycle(debug_instruction=test_opcode)

        # Helper functions to find MSB.
        def bitLen(value): # Gives the length of an unsigned value in bits
            length = 0
            while (value):
                value >>= 1
                length += 1
            return(length)

        def getMSB(value, size): # Gets the MSB of an unsigned value in a size-bit format
            length = bitLen(value)
            if(length == size):
                return 1
            else:
                return 0

        assert Chip8.V[0xF] == getMSB(tmp, 8)

        assert (2*tmp == Chip8.V[rand_reg_label_1])

        Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('8XYE: Test passed')

if __name__ == '__main__':
    run_test()