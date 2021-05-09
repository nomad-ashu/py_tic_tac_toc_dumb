# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:18:47 2021

@author: Ashu
"""

import random

# Create an empty board
board_input = []
for i in range (0,9):
    board_input.append(" ")

def board_display(board_input):
    print(f"{board_input[0]}|{board_input[1]}|{board_input[2]}")
    print(f"{board_input[3]}|{board_input[4]}|{board_input[5]}")
    print(f"{board_input[6]}|{board_input[7]}|{board_input[8]}")
    
board_display(board_input)

user_inputs = []
computer_move_type = 'dumb'
computer_inputs = []
winning_conditions = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
board_status = {'move': 'user', 'won': False, 'complete': False}

# Take user input and show it in the board
def user_move(board_status):
    p1 = int(input('Please enter your move: '))
    if board_input[p1-1] != " ":
        print("Inavlid move!")
        user_move(board_status)
    else:
        user_inputs.append(p1)
        board_input[p1-1] = "X"
        print('User\'s move \n')
        board_display(board_input)
        # If you win
        move_win(user_inputs, winning_conditions, board_status)
        if board_status['won']:
            print(f"{board_status['move']} won!!")
        # If it's a draw
        elif " " not in board_input:
            print('It\'s a draw!!')
            board_status['complete'] = True
            return board_status
        # Toggle move to computer
        else:
            board_status['move'] = 'computer'
            return board_status

#take computer input and show it on the board
def computer_move(board_status):
    print('Computer\'s move\n')
    if computer_move_type == 'dumb':
        move_completed = False
        while not move_completed:
            p2 = random.randint(1,9)
            if board_input[p2-1] == " ":
                computer_inputs.append(p2)
                move_completed = True
                board_input[p2-1] = "O"
                board_display(board_input)
        # If Computer wins
        move_win(computer_inputs, winning_conditions, board_status)
        if board_status['won']:
            print(f"{board_status['move']} won!!")
        # Toggle move to user
        else:
            board_status['move'] = 'user'
            return board_status

# Determine if won
def move_win(input_list, winning_conditions, board_status):
    for condition in winning_conditions:
        if set(condition).issubset(set(input_list)):
            board_status['won'] = True
            board_status['complete'] = True
            return board_status

# toggle moves
def move_toggle(board_status):
    if board_status['move'] == 'user':
        user_move(board_status)
    elif board_status['move'] == 'computer':
        computer_move(board_status)

while not board_status['complete']:
    move_toggle(board_status)
    
