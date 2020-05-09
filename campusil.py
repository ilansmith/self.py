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

print(game_logo)
print(guesses)
