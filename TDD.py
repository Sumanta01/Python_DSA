# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:56:24 2023

@author: KIIT
"""

class Chandrayaan3:
    def __init__(self):
        self.position = [0, 0, 0]
        self.direction = "N"

    def move_forward(self):
        if self.direction == "N":
            self.position[1] += 1
       
    def move_backward(self):
        if self.direction == "N":
            self.position[1] -= 1
       
    def turn_left(self):
       
        pass

    def turn_right(self):
       
        pass

    def turn_up(self):
        
        pass

    def turn_down(self):
       
        pass

def execute_commands(commands):
    chandrayaan = Chandrayaan3()
    
    for cmd in commands:
        if cmd == "f":
            chandrayaan.move_forward()
        elif cmd == "b":
            chandrayaan.move_backward()
        elif cmd == "l":
            chandrayaan.turn_left()
        elif cmd == "r":
            chandrayaan.turn_right()
        elif cmd == "u":
            chandrayaan.turn_up()
        elif cmd == "d":
            chandrayaan.turn_down()

    return chandrayaan.position, chandrayaan.direction

def main_Fun():
    input_str = input("Enter commands (f, b, l, r, u, d) separated by spaces: ")
    commands = input_str.split()

    final_position, final_direction = execute_commands(commands)
    print("Final Position:", final_position)
    print("Final Direction:", final_direction)

if __name__ == "__main__":
    main_Fun()
