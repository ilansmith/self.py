#!/usr/bin/python

import random

# print pening screen

# option to read from file:
#game_logo = open("hangman.txt").read()
game_logo=("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
""")
guesses = random.randint(5, 10)

hangman_1="""
    x-------x
"""

hangman_2="""
    x-------x
    |
    |
    |
    |
    |
"""

hangman_3="""
    x-------x
    |       |
    |       0
    |
    |
    |
"""

hangman_4="""
    x-------x
    |       |
    |       0
    |       |
    |
    |
"""

hangman_5="""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
"""

hangman_6="""
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
"""

hangman_7="""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""

print(game_logo)
print(guesses)
print(hangman_1)
print(hangman_2)
print(hangman_3)
print(hangman_4)
print(hangman_5)
print(hangman_6)
print(hangman_7)
