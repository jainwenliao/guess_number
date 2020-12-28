import random
#首先在1-20随机选择一个数字
selected_number = random.randint(1,20)
print("I  am thinking a number between 1 and 20.")
#猜6次
for guess_number in range(1,7):
    print('Take a guess: ')
    guess = int(input())

    if guess < selected_number: 
        print('Your guess is too low.')

    elif guess > selected_number:
        print('Your guess is too high.')
    else:#猜对了就退出循环
        break
if guess == selected_number:  
    print('Good job! you guessed my number in '+str(guess_number)+' guesses!')
else:  
    print('Nope, the number I was thinking of was ' + str(selected_number))