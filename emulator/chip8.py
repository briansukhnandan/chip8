import sys
import random

'''
How to run this program:
python3 chip8.py ROMs/Pong.ch8
'''

########################################################
NUM_REGISTERS = 0x10 # 16
MAX_MEMORY = 0x1000 # 4096
STACK_POINTER_START = 0x52
PROGRAM_COUNTER_START = 0x200 # PC starts at 512
########################################################

class CPU:
    def __init__(self, ROM_path):

        '''Our .ch8 file.'''
        self.ROM = ROM_path

        '''Chip8 has 2 timers. They both count down at 60Hz until 0.'''
        self.timers = {
            'delay' : 0, # Intended to be used for timing events of games. Value can be set/read.
            'sound' : 0 # Used for sound effects. When value is nonzero, a beep is made.
        }

        '''
        There are 16 main registers going from V0-VF.
        Each register is 8 bits long.

        NOTE - Register VF sometimes doubles as a flag for certain
        instructions.
        '''
        self.V = [0] * NUM_REGISTERS

        '''8-bit stack pointer so we can keep track of the next thing on the stack to be popped.'''
        self.sp = STACK_POINTER_START

        '''8-bit program counter to keep track of current instruction.'''
        self.pc = PROGRAM_COUNTER_START

        '''A 16-bit index register used with several opcodes that involve memory operations.'''
        self.I = 0

        '''
        The memory for Chip8 is 4096 (0x1000) or 4kb.
        Python's bytearray function will correctly allocate the specified
        amount of memory for us.
        '''
        self.memory = bytearray(MAX_MEMORY)

        '''The current opcode to be executed.'''
        self.current_opcode = 0x0

        '''A random number which will be regenerated upon every 0xC opcode'''
        self.random_num = random.randint(0,255)
        
        # print('Loading ROM')
        self.load_rom_into_memory()

    '''If we ever needed to reset CPU back to original state, run this function.'''
    def restart_cpu(self):
        self.V = [0] * NUM_REGISTERS
        self.sp = STACK_POINTER_START
        self.pc = PROGRAM_COUNTER_START
        self.I = 0
        self.memory = bytearray(MAX_MEMORY)
        self.current_opcode = 0x0

        self.timers = {
            'delay' : 0,
            'sound' : 0
        }

        self.load_rom_into_memory()
    
    '''Function to load rom from .ch8 file into memory.'''
    def load_rom_into_memory(self):
        print('Loading ROM into memory...')
        i = PROGRAM_COUNTER_START # All chip 8 roms will have pc set to 0x200.

        with open(self.ROM, "rb") as f:
            while True:
                byte = f.read(1) # Read one byte at a time and store into memory.
                if not byte: # Once we reach EOF.
                    break

                # Python 3 lets us write 1 byte at a time to memory.
                self.memory[i] = int.from_bytes(byte, "big", signed=False)
                i += 1

    '''Function to dump all register data to txt file for debug.'''
    def dump_registers(self):

        f = open("debug/register_dump.txt", "a")

        f.write('\n')
        f.write('Opcode: '+str(hex(self.current_opcode)))
        f.write('\n\n')
        for i in range(NUM_REGISTERS):
            s = 'V'+str(i)+' -> '+str(hex(self.V[i]))+' | '
            f.write(s)

            if (i+1) % 4 == 0:
                f.write('\n')

        f.write('\n')
        f.write('pc -> '+str(hex(self.pc))+'\n')
        f.write('sp -> '+str(hex(self.sp))+'\n')
        f.write('I (addr register) -> '+str(hex(self.I))+'\n')
        f.write('\n--------------------------------------\n')

        f.close()


    '''#####################################################'''
    '''# ALL OPCODE RELATED IMPLEMENTATIONS ARE BELOW.     #'''
    '''# IN ORDER TO SEE WHICH OPCODES CALL THEM REFER TO  #'''
    '''# .execute_current_opcode() function.               #'''
    '''#####################################################'''


    '''Get current opcodes starting at PC and PC+1.'''
    def get_current_opcode(self):
        # Each indiv memory is 1 byte, i.e. 2 hex each.
        # Shift current pc over by 8 bits, then add next bit (pc+1).
        return ((self.memory[self.pc] << 8) + self.memory[self.pc+1])

    
    '''Our workflow function to execute the current opcode.'''
    def execute_current_opcode(self, debug_instruction=None):

        # Only for testing specific opcodes for debugging.
        if debug_instruction:
            self.current_opcode = debug_instruction
        else:
            self.current_opcode = self.get_current_opcode()
        
        # Increment opcode before executing instruction in case
        # our next instr jumps to a diff address.
        # Each instruction is 2 bytes long so increment by 2.
        self.pc += 2

        # Then shift by 12 bits (3 hex) to the right to get MSB which is
        # our specified operation.
        operation = (self.current_opcode & 0xF000) >> 12

        ###########--OPCODE--##########
        if operation == 0x0:
            
            # 3 cases:
            # 0NNN - Not necessary for most ROMs.
            # 00E0
            # 00EE

            print('Opcode not implemented yet')

        elif operation == 0x1:
            print('JUMP {}, operation {}'.format(
                hex(self.current_opcode & 0x0FFF), 
                hex(self.current_opcode >> 12)
                )
            )
            self.jump_to_NNN()

        elif operation == 0x2:
            print('CALL {}, operation {}'.format(
                hex(self.current_opcode & 0x0FFF), 
                hex(self.current_opcode >> 12)
                )
            )
            self.call_subroutine_at_NNN()

        elif operation == 0x3:
            print('SKIP {}, operation {}'.format(
                self.pc,
                hex(self.current_opcode >> 12)
                )
            )
            self.skip_Vx_equals_NN()

        elif operation == 0x4:
            print('SKIP {}, operation {}'.format(
                hex(self.pc),
                hex(self.current_opcode >> 12)
                )
            )
            self.skip_Vx_not_equals_NN()

        elif operation == 0x5:
            print('SKIP {}, operation {}'.format(
                self.pc,
                hex(self.current_opcode >> 12)
                )
            )
            self.skip_Vx_equals_Vy()

        elif operation == 0x6:
            print('SET V{}->{}, operation {}'.format(
                ((self.current_opcode & 0x0F00) >> 8), 
                hex(self.current_opcode & 0x00FF), 
                hex(self.current_opcode >> 12)
                )
            )
            self.set_Vx_NN()

        elif operation == 0x7:
            print('ADD {}->V{}, operation {}'.format(
                hex(self.current_opcode & 0x00FF), 
                ((self.current_opcode & 0x0F00) >> 8), 
                hex(self.current_opcode >> 12)
                )
            )
            self.add_NN_Vx()

        elif operation == 0x8:

            # Grab least significant bit to differentiate between 0x8 opcodes.
            diff = self.current_opcode & 0x000F

            # 8XY0
            if diff == 0x0:
                print('SET V{} -> V{}'.format(
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x00F0) >> 4
                    )
                )
                self.set_Vx_Vy()

            # 8XY1
            elif diff == 0x1:
                print('SET V{} -> V{} OR V{}'.format(
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x00F0) >> 4
                    )
                )
                self.set_Vx_Vx_or_Vy()
            
            # 8XY2
            elif diff == 0x2:
                print('SET V{} -> V{} AND V{}'.format(
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x00F0) >> 4
                    )
                )
                self.set_Vx_Vx_and_Vy()

            # 8XY3
            elif diff == 0x3:
                print('SET V{} -> V{} XOR V{}'.format(
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x00F0) >> 4
                    )
                )
                self.set_Vx_Vx_xor_Vy()

            # 8XY4
            elif diff == 0x4:
                print('SET V{} -> V{} + V{}'.format(
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x00F0) >> 4
                    )
                )
                self.add_Vy_to_Vx()

            # 8XY5
            elif diff == 0x5:
                print('SET V{} -> V{} - V{}'.format(
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x00F0) >> 4
                    )
                )
                self.subtract_Vy_from_Vx()

            # 8XY6
            elif diff == 0x6:
                print('SHIFT V{} RIGHT 1'.format(
                    (self.current_opcode & 0x0F00) >> 8
                    )
                )           
                self.shift_Vx_right_1()

            # 8XY7
            elif diff == 0x7:
                print('SET V{} -> V{} - V{}'.format(
                    (self.current_opcode & 0x0F00) >> 8,
                    (self.current_opcode & 0x00F0) >> 4,
                    (self.current_opcode & 0x0F00) >> 8
                    )
                )
                self.set_Vx_Vy_minus_Vx()

            # 8XYE
            elif diff == 0xE:
                print('SHIFT V{} LEFT 1'.format(
                    (self.current_opcode & 0x0F00) >> 8
                    )
                )
                self.shift_Vx_left_1()

        elif operation == 0x9:
            print('SKIP {}, operation {}'.format(
                self.pc,
                hex(self.current_opcode >> 12)
                )
            )
            self.skip_Vx_not_equals_Vy()

        elif operation == 0xA:
            print('SET I -> {}, operation {}'.format(
                hex(self.current_opcode & 0x0FFF),
                hex(self.current_opcode >> 12)
                )
            )
            self.set_I_NNN()

        elif operation == 0xB:
            print('JUMP {}, operation {}'.format(
                hex(self.V[0] + (self.current_opcode & 0x0FFF)), 
                hex(self.current_opcode >> 12)
                )
            )
            self.jump_V0_plus_NNN()

        elif operation == 0xC:
            print('SET V{} -> {} AND {}'.format(
                (self.current_opcode & 0x0F00) >> 8,
                hex(self.random_num),
                hex(self.current_opcode & 0x00FF)
                )
            )
            self.set_Vx_rand_and_NN()

        elif operation == 0xD:
            print('Opcode not implemented yet')

        elif operation == 0xE:
            
            diff = self.current_opcode & 0x00FF

            if diff == 0x9E:
                pass

            elif diff == 0xA1:
                pass

            print('Opcode not implemented yet')

        elif operation == 0xF:
            
            diff = self.current_opcode & 0x00FF

            if diff == 0x07:
                pass

            elif diff == 0x0A:
                pass

            elif diff == 0x15:
                pass

            elif diff == 0x18:
                pass

            elif diff == 0x1E:
                pass

            elif diff == 0x29:
                pass

            elif diff == 0x33:
                pass

            elif diff == 0x55:
                pass

            elif diff == 0x65:
                pass 

            print('Opcode not implemented yet')

    #####################################################################

    # 0x1NNN
    def jump_to_NNN(self):
        # We can simply set our program counter to be
        # NNN, which is last 3 sig. digits of current opcode.
        self.pc = self.current_opcode & 0x0FFF

    # 0x2NNN
    def call_subroutine_at_NNN(self):
        
        # Save the current pc onto the stack, 2 bytes at a time.
        self.memory[self.sp] = self.pc & 0x00FF # First 2 LSB
        self.sp += 1 # Increment stack pointer
        self.memory[self.sp] = (self.pc & 0xFF00) >> 8 # First 2 MSB.
        self.sp += 1

        # Set pc to NNN.
        self.pc = self.current_opcode & 0x0FFF

    # 0x3XNN
    def skip_Vx_equals_NN(self):
        NN = self.current_opcode & 0x00FF
        x = (self.current_opcode & 0x0F00) >> 8

        # Skip next instruction by simply incrementing our program
        # counter to next instruction.
        if (self.V[x] == NN):
            self.pc += 2

    # 0x4XNN
    def skip_Vx_not_equals_NN(self):
        NN = self.current_opcode & 0x00FF
        x = (self.current_opcode & 0x0F00) >> 8

        # Skip next instruction by simply incrementing our program
        # counter to next instruction.
        if (self.V[x] != NN):
            self.pc += 2

    # 0x5XY0
    def skip_Vx_equals_Vy(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        if (self.V[x] == self.V[y]):
            self.pc += 2
        
    # 0x6XNN
    def set_Vx_NN(self):
        NN = self.current_opcode & 0x00FF
        x = (self.current_opcode & 0x0F00) >> 8

        self.V[x] = NN

    # 0x7XNN
    def add_NN_Vx(self):
        NN = self.current_opcode & 0x00FF
        x = (self.current_opcode & 0x0F00) >> 8

        # Since each register is 8 bit we must handle overflow.
        # i.e we cannot let the registers go over 255.
        t = self.V[x] + NN
        self.V[x] = t if t < (2**8) else t - (2**8)

    # 0x9XY0
    def skip_Vx_not_equals_Vy(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        if (self.V[x] != self.V[y]):
            self.pc += 2

    # 0xANNN
    def set_I_NNN(self):
        NNN = self.current_opcode & 0x0FFF
        self.I = NNN

    # 0xBNNN
    def jump_V0_plus_NNN(self):
        NNN = self.current_opcode & 0x0FFF
        self.pc = self.V[0] + NNN

    # 0xCXNN
    def set_Vx_rand_and_NN(self):
        x = (self.current_opcode & 0x0F00) >> 8
        NN = self.current_opcode & 0x00FF

        self.V[x] = self.random_num & NN

        # Regen random_num so next random number is different.
        self.random_num = random.randint(0,255)


    '''##################################################'''
    '''# All 0x8XYZ instructions are implemented below. #'''
    '''##################################################'''

    # 0x8XY0
    def set_Vx_Vy(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        self.V[x] = self.V[y]

    # 0x8XY1
    def set_Vx_Vx_or_Vy(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        self.V[x] = self.V[x] | self.V[y]

    # 0x8XY2
    def set_Vx_Vx_and_Vy(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        self.V[x] = self.V[x] & self.V[y]

    # 0x8XY3
    def set_Vx_Vx_xor_Vy(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        self.V[x] = self.V[x] ^ self.V[y]

    # 0x8XY4
    def add_Vy_to_Vx(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        # We must check for overflow (carry) and set VF to 1 if so.
        # Else we can just leave it at 0.
        t = self.V[x] + self.V[y]

        if t > 255:
            self.V[x] = t - (2**8)
            self.V[0xF] = 1
        else:
            self.V[x] = t
            self.V[0xF] = 0

    # 0x8XY5
    def subtract_Vy_from_Vx(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        # If Vx > Vy, then VF is set to 1, otherwise 0. 
        # Then Vy is subtracted from Vx, and the results stored in Vx.
        # Account for overflow if Vx < Vy

        if self.V[x] > self.V[y]:
            self.V[0xF] = 1
            self.V[x] = self.V[x] - self.V[y]
        else:
            self.V[0xF] = 0
            self.V[x] = 2**8 + (self.V[x] - self.V[y])

    # 0x8XY6
    def shift_Vx_right_1(self):
        x = (self.current_opcode & 0x0F00) >> 8
        # y = (self.current_opcode & 0x00F0) >> 4
        
        # If the least-significant bit of Vx is 1, then VF is set to 1, 
        # otherwise 0. Then Vx is divided by 2.
        lsb_Vx = self.V[x] & 0x1

        self.V[x] = self.V[x] >> 1
        self.V[0xF] = lsb_Vx

    # 0x8XY7
    def set_Vx_Vy_minus_Vx(self):
        x = (self.current_opcode & 0x0F00) >> 8
        y = (self.current_opcode & 0x00F0) >> 4

        if self.V[y] > self.V[x]:
            self.V[0xF] = 1
            self.V[x] = self.V[y] - self.V[x]
        else:
            self.V[0xF] = 0
            self.V[x] = 2**8 + (self.V[y] - self.V[x])

    # 0x8XYE
    def shift_Vx_left_1(self):
        x = (self.current_opcode & 0x0F00) >> 8
        # y = (self.current_opcode & 0x00F0) >> 4

        # If the most-significant bit of Vx is 1, then VF is set to 1, 
        # otherwise to 0. Then Vx is multiplied by 2.
        msb_Vx = (self.V[x] & 0x80) >> 8

        self.V[x] = self.V[x] << 1
        self.V[0xF] = msb_Vx


    '''############################'''
    '''# Screen related functions #'''
    '''############################'''
    

    # 0x00E0
    def clear_screen(self):
        pass

    # 0x00EE
    def return_from_subroutine(self):
        pass
    

    '''######################'''
    '''# CPU cycle function #'''
    '''######################'''


    def cycle(self, debug_instruction=None):
        self.execute_current_opcode(debug_instruction)
