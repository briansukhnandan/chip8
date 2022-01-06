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

    assert Chip8.pc == 0x200
    old_pc = Chip8.pc

    Chip8.V[10] = 0x12
    Chip8.cycle(debug_instruction=0x3A12)
    assert Chip8.pc == old_pc + 4

    Chip8.restart_cpu()

    Chip8.V[5] = 0x34
    Chip8.cycle(debug_instruction=0x3534)
    assert Chip8.pc == old_pc + 4

    Chip8.restart_cpu()

    Chip8.V[6] = 0x78
    Chip8.cycle(debug_instruction=0x3655)
    assert Chip8.pc == old_pc + 2

    Chip8.restart_cpu()

    Chip8.V[7] = 0x78
    Chip8.cycle(debug_instruction=0x3761)
    assert Chip8.pc == old_pc + 2

    sys.stdout = save_stdout
    print('3XNN: Test passed')

if __name__ == '__main__':
    run_test()