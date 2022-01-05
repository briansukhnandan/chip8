import pygame

from chip8 import CPU
from display import Display

TIMER = pygame.USEREVENT + 1

def main():

    d = Display()
    d.initialize_display()

    Chip8 = CPU(
        ROM_path='./ROMs/test_opcode.ch8',
        screen=d
    )

    pygame.init()
    pygame.time.set_timer(TIMER, 200)

    while Chip8.is_running:
        pygame.time.wait(200)
        Chip8.cycle()

        for e in pygame.event.get():

            if e.type == TIMER:
                Chip8.update_timers()

            if e.type == pygame.QUIT:
                Chip8.stop_CPU()

            if e.type == pygame.KEYDOWN:
                pressed_key = pygame.key.get_pressed()
                if pressed_key[pygame.K_BACKSPACE]:
                    Chip8.stop_CPU()


if __name__ == '__main__':
    main()