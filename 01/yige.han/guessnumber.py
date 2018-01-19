# _*_ coding: utf-8 _*_
import random


class GuessNumber(object):
    def __init__(self, min_num=0, max_num=100, guess_times=5):
        self.min_mun = min_num
        self.max_num = max_num
        self.guess_times = guess_times
        self.random_num = random.randint(min_num, max_num)
        self.msg = ''

    def guess(self, guess_num):
        if isinstance(guess_num, int) or isinstance(guess_num, str) and guess_num.isdigit():
            guess_num = int(guess_num)
            if guess_num > self.max_num or guess_num < self.min_mun:
                self.msg = "你输入的数字超过了范围,请重新输入"
                return False
            else:
                self.guess_times -= 1
                if self.guess_times == 0:
                    self.msg = "你太笨了,我们的数字是{}, 再猜一次吧".format(self.random_num)
                    return True
                if guess_num > self.random_num:
                    self.msg = "猜大了!"
                    return False
                elif guess_num < self.random_num:
                    self.msg = "猜小了!"
                    return False
                else:
                    self.msg = "恭喜你猜对了!"
                    return True
        else:
            self.msg = "你输入的不是数字,请输入数字!"
            return False


def main():
    min_num = 0
    max_num = 100
    guess_times = 5
    guess = GuessNumber(min_num=min_num, max_num=max_num, guess_times=guess_times)
    print("这是一个猜数字的游戏,系统随机生成一个数字,根据系统猜出这个数字,你有{}次机会".format(guess_times))

    while True:
        guess_num = input("请输入一个{}到{}的数字:".format(min_num, max_num))
        result = guess.guess(guess_num)
        print(guess.msg)
        if result:
            break


if __name__ == "__main__":
    main()


'''
功能ok，底子不错，继续加油
'''
