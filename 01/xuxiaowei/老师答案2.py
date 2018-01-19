#encoding: utf-8

import random


rand = random.randint(0, 100)

guess_count = 0
guess_max_count = 5

while True:
    guess = input('请输入猜测的数字:')
    guess = int(guess)
    guess_count += 1
    
    if guess > rand:
        print('太大啦!还有', guess_max_count - guess_count, '次机会')
    elif guess < rand:
        print('太小啦!还有', guess_max_count - guess_count, '次机会')
    else:
        print('恭喜你！')
        break
        
    if guess_count >= guess_max_count:
        print('太笨了, 下次再来')
        break
   
