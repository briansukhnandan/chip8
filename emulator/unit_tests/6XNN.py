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

    Chip8.cycle(debug_instruction=0x6AB1)
    assert Chip8.V[10] == 0xB1

    Chip8.restart_cpu()

    Chip8.cycle(debug_instruction=0x6327)
    assert Chip8.V[3] == 0x27

    Chip8.restart_cpu()

    Chip8.cycle(debug_instruction=0x667A)
    assert Chip8.V[6] == 0x7A

    Chip8.restart_cpu()

    Chip8.cycle(debug_instruction=0x6803)
    assert Chip8.V[8] == 0x03

    Chip8.restart_cpu()

    Chip8.cycle(debug_instruction=0x6E21)
    assert Chip8.V[14] == 0x21

    Chip8.restart_cpu()

    Chip8.cycle(debug_instruction=0x6217)
    assert Chip8.V[2] == 0x17

    Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('6XNN: Test passed')

if __name__ == '__main__':
    run_test()