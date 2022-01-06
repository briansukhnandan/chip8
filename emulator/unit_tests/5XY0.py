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
    Chip8.V[11] = 0x12
    Chip8.cycle(debug_instruction=0x5AB0)
    assert Chip8.pc == old_pc + 4

    Chip8.restart_cpu()

    Chip8.V[2] = 0x63
    Chip8.V[5] = 0x64
    Chip8.cycle(debug_instruction=0x5250)
    assert Chip8.pc == old_pc + 2

    Chip8.restart_cpu()

    Chip8.V[1] = 0x63
    Chip8.V[10] = 0xFE
    Chip8.cycle(debug_instruction=0x51A0)
    assert Chip8.pc == old_pc + 2

    Chip8.restart_cpu()

    Chip8.V[2] = 0x2
    Chip8.V[12] = 0xD1
    Chip8.cycle(debug_instruction=0x52C0)
    assert Chip8.pc == old_pc + 2

    Chip8.restart_cpu()

    Chip8.V[3] = 0xFE
    Chip8.V[7] = 0xFE
    Chip8.cycle(debug_instruction=0x5370)
    assert Chip8.pc == old_pc + 4

    Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('5XY0: Test passed')

if __name__ == '__main__':
    run_test()