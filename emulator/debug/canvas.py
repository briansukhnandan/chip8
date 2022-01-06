# print("{}".format(0x1000))

# # for i in range(0x10):
# #     print(i)

# a = [0]*3
# print(a)

# a = 0xF

# print(a)
# print(a << 8)

# a = bytearray(10)
# print(a)




# # def getCurrentOpcode(): 	# Retrieves the value of current opcode

# #     # We retrieve the value in the memory for the current PC, and shift it 8 times to the left because it represents the 8 MSB of 16 bits message
# #     # We then add the value for the next memory cell, without any shifting because those are the 8 LSB
# #     # We now have our current opcode
# #     return ((self.memory[self.PC] << 8) + self.memory[self.PC+1])

# def loadGame(offset=0x200):
#     """
#     Load the ROM indicated by the filename into memory.
#     @param filename: the name of the file to load
#     @type filename: string
#     @param offset: the location in memory at which to load the ROM
#     @type offset: integer
#     """

#     memory = bytearray(4096)

#     romdata = open("Pong.ch8", 'rb').read()
#     for index, val in enumerate(romdata):
#         memory[offset + index] = val

#     return memory


# def loadGame2(): 	# Loads the game from the ROM into memory

#     memory = bytearray(4096)

#     i = 0x200									# Default adress to store the program

#     with open("Pong.ch8", "rb") as f: 								# Opening the ROM
#         while 1: 														# While the universe is working
#             byte = f.read(1) 											# We get a byte
#             if not byte: 												# If it is empty we reached the EOF
#                 break													# Breaking out of the loop
#             memory[i] = int.from_bytes(byte, "big", signed=False) 	# Storing into the memory at the i position the value of the byte we just read
#             i += 1


#     return memory

# # loadGame()

# # print()
# # print()
# # print()

# # loadGame2()

# if loadGame() == loadGame2():
#     print('Opcodes in same positions')
# else:
#     print('Not same')

# # memory = loadGame2()

# # def execute_instruction(memory):
# #     """
# #     Execute the next instruction pointed to by the program counter.
# #     For testing purposes, pass the operand directly to the
# #     function. When the operand is not passed directly to the
# #     function, the program counter is increased by 2.
# #     :param operand: the operand to execute
# #     :return: returns the operand executed
# #     """


# #     operand = int(memory[0x200])
# #     operand = operand << 8 # remember that 1 hex num is 4 binary cause 2^4=16.
# #     operand += int(memory[0x200 + 1])
# #         # self.registers['pc'] += 2

# #     # Then shift by 12 bits (3 hex) to the right to get MSB which is
# #     # our specified operation.
# #     operation = (operand & 0xF000) >> 12

# #     print(hex(operand))
# #     print(operation)
# #     # return self.operand

# # execute_instruction(memory)



# memory = loadGame2()

# def get_current_opcode(memory):
#     return ((memory[0x21c] << 8) + memory[0x21c+1])

# def execute_current_opcode(memory):
#     current_opcode = get_current_opcode(memory)

#     # Then shift by 12 bits (3 hex) to the right to get MSB which is
#     # our specified operation.
#     operation = (current_opcode & 0xF000) >> 12
#     print()
#     print(hex(current_opcode))
#     print(operation)
#     ###########--OPCODE--##########

#     if operation == 0x2:
#         print('CALL {}'.format(hex(current_opcode)))

#     ###############################

#     # pc += 2

# execute_current_opcode(memory)

# m = 0x22f6 # 0010001011110110
# print(m) # 8950 = 0010001011110110

# # 0xF000 = 1111000000000000 - So we are taking 4 MSB's. 
# print(m & 0xF000) # 8192 = 0010000000000000

# print(0x2)

# def bitLen(value): 	# Gives the length of an unsigned value in bits
# 	length = 0
# 	while (value):
# 		value >>= 1
# 		length += 1
# 	return(length)

# def getMSB(value, size): 	# Gets the MSB of an unsigned value in a size-bit format
# 	length = bitLen(value)
# 	if(length == size):
# 		return 1
# 	else:
# 		return 0


# a = 0xAB

# msb = (a & 0x80) >> 8

# print(bin(a))
# print(bin(msb))

# msb = getMSB(a, 8)

# print(bin(a))
# print(bin(msb))

# fruits = {
# 	1 : 'apple',
# 	2 : 'banana',
# 	3 : 'grape'
# }

# for key, val in fruits.items():
# 	print(key)

# each register will only be 0-255.
# v_register = 8

# def BCD(v):
# 	ones = int(v % 10)
# 	tens = int((v / 10) % 10)
# 	hundreds = int((v / 100) % 10)

# 	print(hundreds)
# 	print(tens)
# 	print(ones)

# print(BCD(v_register))

# rand_reg_label_1 = 0xE
# rand_reg_label_2 = 0x6

# opcode = 0x8
# opcode = ((((opcode << 4) | rand_reg_label_1) << 4) | rand_reg_label_2)
# opcode = (opcode << 4) | 0x1

# print(hex(opcode))

a = 255
b = a >> 1

print(b)