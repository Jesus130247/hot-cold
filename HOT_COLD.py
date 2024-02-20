#hot or cold game
import random
ans = random.randint(1,10)
print("In this game, you will guess for a number between 1-10. \nThe game will return 'warmer' or 'colder', depending on if your guess is closer, or further away than your previous guess")
print(ans)
i = 0
while i == 0:
    choice = int(input("what is your guess? "))
    if choice == ans:
        print("that's right!")
        i = 1
    else:
        print("wrong!")
        i = 1
while i == 1:
    choice2 = int(input("try again: "))
    if choice2 == ans:
        print('Right!')
        i = 2
    elif abs(ans-choice2) < abs(ans-choice):
        print('warmer')
        choice = choice2
    elif abs(ans-choice2) > abs(ans-choice):
        print('colder')
        choice = choice2
    else:
        print('close')
        choice = choice2