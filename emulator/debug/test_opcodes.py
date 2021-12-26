import sys
sys.path.append("..")

from chip8 import CPU

def cpu_cycle():
    # Erase contents of file first before we append.
    f = open("register_dump.txt", "w").close()
    Chip8 = CPU(
        ROM_path='../ROMs/Pong.ch8',
        screen=None
    )
    
    #############################################
    # Testing 0x3, 0x5, 0x7, 0xA, 0x8XY0
    #############################################
    Chip8.cycle(debug_instruction=0x7B2A)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x84B0)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x54B0)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x3B2A)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0xa28a)
    Chip8.dump_registers()
    
    Chip8.restart_cpu()

    ########################################
    # Testing 0x4, 0x6, 0x8, 0xB opcodes
    ########################################
    Chip8.cycle(debug_instruction=0x7B02)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x671C)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x600C)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x4B03)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0xB200)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x87B1)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x8702)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x80B3)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x80B4)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x87B5)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x8706)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x8077)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x870E)
    Chip8.dump_registers()

    Chip8.restart_cpu()

    ########################################
    # Testing 0x9, 0xC opcodes
    ########################################
    Chip8.cycle(debug_instruction=0xC72A)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x600C)
    Chip8.dump_registers()

    Chip8.cycle(debug_instruction=0x9700)
    Chip8.dump_registers()

if __name__ == '__main__':
    cpu_cycle()

