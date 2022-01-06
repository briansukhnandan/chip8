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
    Chip8.V[7] = 0x71
    Chip8.cycle(debug_instruction=0x8670)
    assert Chip8.V[6] == Chip8.V[7]

    Chip8.restart_cpu()

    Chip8.V[8] = 0x15
    Chip8.V[12] = 0x14
    Chip8.cycle(debug_instruction=0x88C0)
    assert Chip8.V[8] == Chip8.V[12]
    
    Chip8.restart_cpu()

    Chip8.V[1] = 0x17
    Chip8.V[14] = 0x71
    Chip8.cycle(debug_instruction=0x81E0)
    assert Chip8.V[1] == Chip8.V[14]
    
    Chip8.restart_cpu()

    Chip8.V[11] = 0x99
    Chip8.V[14] = 0xFF
    Chip8.cycle(debug_instruction=0x8BE0)
    assert Chip8.V[11] == Chip8.V[14]
    
    Chip8.restart_cpu()

    Chip8.V[3] = 0x24
    Chip8.V[12] = 0xAA
    Chip8.cycle(debug_instruction=0x83C0)
    assert Chip8.V[3] == Chip8.V[12]
    
    Chip8.restart_cpu()

    sys.stdout = save_stdout
    print('8XY0: Test passed')

if __name__ == '__main__':
    run_test()