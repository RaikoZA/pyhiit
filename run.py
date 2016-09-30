from system.sys import *

'''
Takes user input in seconds to calculate timings and amount of exercises/sets
'''
WARMUP = int(input('Warmup: '))
ACTIVE_TIME = int(input('Active: '))
REST_TIME = int(input('Rest: '))
COOLDOWN = int(input('Cooldown: '))
EXERCISES = int(input('Exercises: '))
SETS = int(input('Sets: '))

'''
Clear screen after user input
'''
clear()

'''
Warmup phase
'''
WarmupPhase.warmup(WARMUP)

'''
This will start the main script with user
input of amount of sets, exercises and times for active
and rest periods
'''
Start.exercises(SETS, EXERCISES, ACTIVE_TIME, REST_TIME)

'''
This will begin the Cooldown phase in the script which
takes in the COOLDOWN user input as an argument
'''
CooldownPhase.cooldown(COOLDOWN)

