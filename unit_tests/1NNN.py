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
        NNN = random.randint(0x202, 0xFFD)

        test_opcode = 0x1
        test_opcode = test_opcode << 12
        test_opcode = test_opcode | NNN

        Chip8.cycle(debug_instruction=test_opcode)
        assert Chip8.pc == (test_opcode & 0x0FFF)

        Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('1NNN: Test passed')

if __name__ == '__main__':
    run_test()