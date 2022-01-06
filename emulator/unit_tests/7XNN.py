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

    Chip8.V[6] = 0x2
    Chip8.cycle(debug_instruction=0x767A)
    assert Chip8.V[6] == 0x7C

    Chip8.restart_cpu()

    Chip8.V[4] = 0x21
    Chip8.cycle(debug_instruction=0x747A)
    assert Chip8.V[4] == (0x7A + 0x21)

    Chip8.restart_cpu()

    Chip8.V[10] = 0xF3
    Chip8.cycle(debug_instruction=0x7A03)
    assert Chip8.V[10] == (0xF3 + 0x03)

    Chip8.restart_cpu()

    Chip8.V[14] = 0x66
    Chip8.cycle(debug_instruction=0x7E0A)
    assert Chip8.V[14] == (0x66 + 0x0A)

    Chip8.restart_cpu()

    Chip8.V[9] = 0x71
    Chip8.cycle(debug_instruction=0x7912)
    assert Chip8.V[9] == (0x71 + 0x12)

    Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('7XNN: Test passed')

if __name__ == '__main__':
    run_test()