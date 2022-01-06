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

    assert Chip8.sp == 0x52
    old_sp = Chip8.sp

    Chip8.cycle(debug_instruction=0x2212)
    assert Chip8.pc == 0x212
    assert Chip8.sp == old_sp+2

    Chip8.restart_cpu()

    Chip8.cycle(debug_instruction=0x2304)
    assert Chip8.pc == 0x304
    assert Chip8.sp == old_sp+2

    Chip8.restart_cpu()

    Chip8.cycle(debug_instruction=0x2412)
    assert Chip8.pc == 0x412
    assert Chip8.sp == old_sp+2

    Chip8.restart_cpu()

    Chip8.cycle(debug_instruction=0x2506)
    assert Chip8.pc == 0x506
    assert Chip8.sp == old_sp+2

    sys.stdout = save_stdout
    print('2NNN: Test passed')

if __name__ == '__main__':
    run_test()