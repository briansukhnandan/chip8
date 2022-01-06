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

    Chip8.cycle(debug_instruction=0x1204)
    assert Chip8.pc == 0x204

    Chip8.cycle(debug_instruction=0x1210)
    assert Chip8.pc == 0x210

    Chip8.cycle(debug_instruction=0x1300)
    assert Chip8.pc == 0x300

    Chip8.cycle(debug_instruction=0x1304)
    assert Chip8.pc == 0x304

    Chip8.cycle(debug_instruction=0x1312)
    assert Chip8.pc == 0x312

    Chip8.cycle(debug_instruction=0x1316)
    assert Chip8.pc == 0x316

    Chip8.cycle(debug_instruction=0x1322)
    assert Chip8.pc == 0x322

    sys.stdout = save_stdout
    print('1NNN: Test passed')

if __name__ == '__main__':
    run_test()