#!/bin/sh

# Do all arithmetic/graphics opcodes
python 1NNN.py
python 2NNN.py
python 3XNN.py
python 4XNN.py
python 5XY0.py
python 6XNN.py
python 7XNN.py
python 8XY0.py
python 8XY1.py
python 8XY2.py
python 8XY3.py
python 8XY4.py
python 8XY5.py
python 8XY6.py
python 8XY7.py
python 8XYE.py
python 9XY0.py
python ANNN.py
python BNNN.py
python CXNN.py
python DXYN.py
python FX07.py
python FX15.py
python FX18.py
python FX1E.py
python FX29.py
python FX33.py
python FX55.py
python FX65.py

# Lastly do keyboard-related opcode tests.
python EX9E.py
python EXA1.py