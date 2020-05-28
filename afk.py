import time
import mouse
import random
from sys import exit
from signal import signal, SIGINT

# handle ctrl-C
def handler(signal_recieved, frame):
    print("You were AFK for about", numIntervals, "intervals of", intervals, "seconds!")
    exit()

numIntervals = 0
print("How long would you like the intervals to be in seconds?")
intervals = int(input())
print("When you're back, press ctrl+C to quit.")
run = 'r'
signal(SIGINT, handler)

while run == 'r':
    time.sleep(intervals)
    numIntervals += 1
    x = random.randint(1, 1080)
    y = random.randint(1, 1920)
    mouse.move(x, y, duration=1)


