from random import randint

orange = Actor("orange")
apple = Actor("apple")

count = 0 
missed_counts = 0

def draw():
    screen.clear()
    orange.draw()
    apple.draw()

def place_orange():
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    global count, missed_counts
    if orange.collidepoint(pos):
        count += 1
        print("Good shot!")
        print("Count:", count)
        place_orange()
        place_apple()
    else:
        print("You missed!")
        missed_counts += 1
        print("Missed Counts:", missed_counts)
        if missed_counts == 3:
            quit()

place_orange()
place_apple()