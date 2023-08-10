import time
import random
from adafruit_circuitplayground.express import cpx
import sys

colors = {'red':(50,0,0),'green':(0,50,0),'blue':(0,0,50),'white':(50,50,50),'black':(0,0,0)}
players = {}
players['one'] = {"score": 0}

# Game Won
def gamewon():
    cpx.pixels.fill (colors['green'])
    cpx.play_file("win.wav")
    players['one']['score'] = players['one']['score'] + 10
    print ("Your Score Is:", players['one']['score'])
    speed(players['one']['score'])
    randomize()


# Game Lost
def gamelost():
    cpx.pixels.fill(colors['red'])
    cpx.play_file("lose.wav")
    print("GAME OVER")
    cpx.play_file("gameover.wav")
    print ("Final Score:", players['one']['score'])
    players['one']['score'] = 0
    time.sleep(3)
    intro()

# Countdown timer and lights
# Still need to figure out how to make the levels at certain times and then put time into t
def countdown_lights(t):
    cpx.pixels.fill(colors['red'])
    for i in range (0, 9):
        cpx.pixels[-i-1] = (colors['black'])
        time.sleep(t/9)
        i += 1

#Level System
def speed(score):
    if 0 <= players['one']['score'] <= 90:
        t = 6 - (.055 * players['one']['score'])
        return (t)
    else:
        print("You Win!")
        players['one']['score'] = 0
        cpx.play_file("youwin.wav")
        time.sleep(4)
        intro()

# Tap It
def tapit():
    cpx.detect_taps = 2
    cpx.play_file("tapit.wav")
    print("Tap It!")
    countdown_lights(speed(players['one']['score']))

    if cpx.tapped:
        print("Tapped!")
        gamewon()

    else:
        print("You Didn't Tap It...")
        gamelost()

#Press it A
def pressitA():
    cpx.play_file("pressitA.wav")
    print("Press A!")
    countdown_lights(speed(players['one']['score']))

    if cpx.button_a:
        print("Button A Pressed!")
        gamewon()

    elif cpx.button_b:
        print("Wrong Button!")
        gamelost()

    else:
        print("You Didn't Press A...")
        gamelost()


# Press it B
def pressitB():
    cpx.play_file("pressitB.wav")
    print("Press B!")
    countdown_lights(speed(players['one']['score']))

    if cpx.button_b:
        print("Button B Pressed!")
        gamewon()

    elif cpx.button_a:
        print("Wrong Button!")
        gamelost()
    else:
        print("You Didn't Press B...")
        gamelost()

#Switch It Game
def switchit():
    inital = cpx.switch
    print ("Switch is at:", inital)
    cpx.play_file("switchit.wav")
    print("Switch It!")
    countdown_lights(speed(players['one']['score']))

    if bool(inital) != cpx.switch:
        print("Switched! Switch is now at:", cpx.switch)
        gamewon()

    elif bool(inital) == cpx.switch:
        print("You Didn't Switch It...")
        gamelost()

#Shake it Game
def shakeit():
    cpx.play_file("shakeit.wav")
    print("Shake It!")
    countdown_lights(speed(players['one']['score']))

    if cpx.shake(shake_threshold=10):
        print("Shake Detected!")
        gamewon()

    else:
        print ("You Didn't Shake It...")
        gamelost()

#Randomize Games
games = [tapit, pressitA, pressitB, switchit, shakeit]
def randomize():
    global r
    r = random.randint(0,len(games)-1)
    return r

# Intro Sequence
def intro():
    cpx.pixels.fill(colors['white'])
    cpx.play_file("loading.wav")
    time.sleep(1)
    startgame()
#Start Game
def startgame():
    if (cpx.button_a and cpx.button_b) == True:
        cpx.pixels.fill(colors['green'])
        cpx.play_file("startingsound.wav")
    elif cpx.button_a == True:
        sys.exit()
    else:
        intro()
        return False

#RUNNING THE GAME
intro()
while True:
    randomize()
    games[r]()
