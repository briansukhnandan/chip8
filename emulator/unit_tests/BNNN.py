import random
import sys
sys.path.append('..')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

from chip8 import CPU

def run_test():

    save_stdout = sys.stdout
    sys.stdout = open('trash', 'w')

    Chip8 = CPU(
        ROM_path='../ROMs/Pong.ch8',
        screen=None
    )

    for i in range(0x200):

        NNN = random.randint(0x202, 0xAAD)
        Chip8.V[0] = random.randint(0, 1000)
        assert Chip8.pc == 0x200

        test_opcode = 0xB
        test_opcode = test_opcode << 12
        test_opcode = test_opcode | NNN

        Chip8.cycle(debug_instruction=test_opcode)
        
        assert Chip8.pc == Chip8.V[0] + NNN

        Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('BNNN: Test passed')

if __name__ == '__main__':
    run_test()