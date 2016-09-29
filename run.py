from system.sys import *

WARMUP = int(input('Warmup: '))
ACTIVE_TIME = int(input('Active: '))
REST_TIME = int(input('Rest: '))
COOLDOWN = int(input('Cooldown: '))
EXERCISES = int(input('Exercises: '))
SETS = int(input('Sets: '))

clear()


WarmupPhase.warmup(WARMUP)
Start.exercises(SETS, EXERCISES, ACTIVE_TIME, REST_TIME)
CooldownPhase.cooldown(COOLDOWN)

