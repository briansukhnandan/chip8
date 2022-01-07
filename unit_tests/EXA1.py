import random
import pygame
import sys
sys.path.append('../emulator')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

from chip8 import CPU
from display import Display

# NOTE - This test is for both 0xDXYN and 0x00E0 opcodes.
def run_test():

    # save_stdout = sys.stdout
    # sys.stdout = open('trash', 'w')

    d = Display()
    d.initialize_display()

    Chip8 = CPU(
        ROM_path='../emulator/ROMs/Pong.ch8',
        screen=d
    )

    for i in range(0x5):

        # Don't include 0xF
        reg_labels = [
            0x0, 0x1, 0x2, 
            0x3, 0x4, 0x5, 
            0x6, 0x7, 0x8, 
            0x9, 0xA, 0xB,
            0xC, 0xD, 0xE
        ]

        rand_reg_label_1 = random.choice(reg_labels)

        KEYBINDS = {
            0x1: pygame.K_1,
            0x2: pygame.K_2,
            0x3: pygame.K_3,
            0x4: pygame.K_4,
            0x5: pygame.K_q,
            0x6: pygame.K_w,
            0x7: pygame.K_e,
            0x8: pygame.K_r,
            0x9: pygame.K_a,
            0x0: pygame.K_s,
            0xA: pygame.K_d,
            0xB: pygame.K_f,
            0xC: pygame.K_z,
            0xD: pygame.K_x,
            0xE: pygame.K_c,
            0xF: pygame.K_v
        }

        TRANSLATIONS = {
            0x1: '1',
            0x2: '2',
            0x3: '3',
            0x4: '4',
            0x5: 'q',
            0x6: 'w',
            0x7: 'e',
            0x8: 'r',
            0x9: 'a',
            0x0: 's',
            0xA: 'd',
            0xB: 'f',
            0xC: 'z',
            0xD: 'x',
            0xE: 'c',
            0xF: 'v'
        }

        Chip8.V[rand_reg_label_1] = random.choice(list(KEYBINDS.keys()))
        old_pc = Chip8.pc

        test_opcode = 0xE
        test_opcode = ((test_opcode << 4) | rand_reg_label_1) << 8
        test_opcode = test_opcode | 0xA1

        print('Press the following char on your keyboard: {}'.format(TRANSLATIONS[Chip8.V[rand_reg_label_1]]))
        # pygame.time.wait(500)

        input_received = False

        # While the user has not pressed a key yet.
        while not input_received:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    pressed_key = pygame.key.get_pressed()

                    # The user pressing the key Vx means we will NOT
                    # skip the next instruction.
                    if pressed_key[KEYBINDS[Chip8.V[rand_reg_label_1]]]:
                        
                        save_stdout = sys.stdout
                        sys.stdout = open('trash', 'w')

                        Chip8.cycle(debug_instruction=test_opcode)
                        assert Chip8.pc == old_pc+2

                        sys.stdout = save_stdout

                        input_received = True

        # print('u got here gj')
        Chip8.restart_cpu()

    # sys.stdout = save_stdout
    print('EXA1: Test passed')

if __name__ == '__main__':
    run_test()