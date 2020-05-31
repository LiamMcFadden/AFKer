import time
import keyboard
import mouse
import random
from sys import exit
from signal import signal, SIGINT
import csv

numIntervals = 0
intervals = 0 

# handle ctrl-C
def handler(signal_recieved, frame):
    if (intervals == 0):
        print("Goodbye!")
        exit()

    print("You were AFK for about", numIntervals, "intervals of", intervals, "seconds!")
    exit()

signal(SIGINT, handler)

def move(intervals):
    global numIntervals
    time.sleep(intervals)
    keyboard.press('w')
    time.sleep(0.2)
    keyboard.release('w')
    keyboard.press('s')
    time.sleep(0.2)
    keyboard.release('s')
    numIntervals += 1

def respawn(x, y):
    mouse.move(x, y)
    mouse.click()

def afk(interval=None, x=None, y=None, profile=None):
    global intervals
    if profile is None:
        if x is None or y is None:
            while True:
                move(interval)
        else:
            while True:
                move(interval)
                if numIntervals % intervals == 0:
                    respawn(x, y)
    else:
        csvfile = open('profile.csv', 'r', newline='')
        data = csv.reader(csvfile)
        x = 0
        y = 0
        for row in data:
            if row[0] == profile:
                intervals = int(row[1])
                x = int(row[2])
                y = int(row[3])
                break
        if x == 0 and y == 0:
            while True:
                move(intervals)
        else:
            while True:
                move(intervals)
                if (numIntervals % intervals == 0):
                        respawn(x,y)

# set up a new profile
newProf = input("Would you like to create a new game profile?(y/n): ")
if (newProf == 'y'):
    profName = input("Name your profile: ")
    data = {}
    intervals = int(input("How long would you like to wait between movments?: "))
    respawn = input("Would you like to check for respawn?(y/n): ")
    y = 0
    x = 0
    if (respawn == 'y'):
        print("If (0,0) is the top left corner of your screen, about where do you think the button is?")
        x = int(input("x coord: "))
        y = int(input("y coord: "))
        mouse.move(x,y,duration=1)
        good = input("Is this correct?(y/n): ")
        while (good != 'y'):
            x = int(input("x coord: "))
            y = int(input("y coord: "))
            mouse.move(x,y,duration=1)
            good = input("Is this correct?(y/n): ")

    data = [profName,intervals,x,y]
    csvfile = open('profile.csv', 'a', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(data)
    print("When you're back, press ctrl+C to quit.")
    afk(profile=profName)

else:
    loadProf = input("Would you like to load a profile?(y/n): ")
    if loadProf == 'y':
        profName = input("What is the name of your profile?: ")
        print("When you're back, press ctrl+C to quit.")
        afk(profile=profName)
        
    print("How long would you like the intervals between movments to be in seconds?")
    intervals = int(input())
    respawn = input("Would you like to check for respawn?(y/n): ")
    y = 0
    x = 0
    if (respawn == 'y'):
        print("If (0,0) is the top left corner of your screen, about where do you think the button is?")
        x = int(input("x coord: "))
        y = int(input("y coord: "))
        mouse.move(x,y,duration=1)
        good = input("Is this correct?(y/n): ")
        while (good != 'y'):
            x = int(input("x coord: "))
            y = int(input("y coord: "))
            mouse.move(x,y,duration=1)
            good = input("Is this correct?(y/n): ")
        print("When you're back, press ctrl+C to quit.")
        afk(interval=intervals, x=x, y=y)
    print("When you're back, press ctrl+C to quit.")
    afk(interval=intervals)


