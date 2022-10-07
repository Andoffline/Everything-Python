import time
import random

magic_num=random.randint(0,100)

print('Guess the magic number between 0 and 100')

guess=-1
attempts=0
tstart=time.time()

while(guess!=magic_num):
    attempts+=1
    guess=int(input('Enter your guess:'))

    if guess==magic_num:
        print('You found the magic number in ',attempts,' attempts')
    elif guess>magic_num:
        print('Your guess us too high')
    else:
        print('Your guess us too low')

tend=time.time()
print('It took you ',int(tend-tstart),' seconds')
