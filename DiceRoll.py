import random

diceMin = 1
diceMax = 6
rollAgain = 'y'
won = 'You WON!'
lose = 'You LOSE!'

while rollAgain == 'y' or rollAgain == 'Y':
    print('-' * 20)
    print('welcome to dice roll')
    ans = int(input('guess the number rolled (1-6): '))
    ansType = type(ans)
    if int(ans) < 1 or int(ans) > 6:
        print('ERROR: Number not in range of 1-6')
        rollAgain = 'y'
    elif ansType == type(rollAgain):
        print('That''s not a number...')
        rollAgain = 'y'
    else:
        rolled = str(random.randint(diceMin,diceMax))
        print('Dice rolling...')
        print('The number rolled is: ' + rolled + ' You chose: ' + str(ans))
        if int(ans) == int(rolled):
            print(won)
            rollAgain = input('Roll again? (Y/N) ')
        else:
            print(lose)
            rollAgain = input('Roll again? (Y/N) ')
if rollAgain == 'n' or rollAgain == 'N':
    print('Thanks for playing!')
else:
    print('ERROR: Answer not recognised - EXITING')
