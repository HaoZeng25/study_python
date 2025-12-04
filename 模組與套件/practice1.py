# 請利用random.randint(a,b)或random.random()，
# 將前面的題目中要猜的數字改成隨機的1~100(含)之間的整數

# 承上題，1~100當中有一些數假設有我們想避開，不想被成為要猜的數字的話，
# 若給定該串列avoid_lt = [4, 14, 44, 94]，
# 請參照上面的說明，使用random.choice(seq)來處理。
# (random.choice()方法可以從一個序列型態的東西seq中隨機取出一個值)
# (序列是有順序的元素的集合統稱，比如list, tuple, range)
# 提示：可以先新增一個數列並去處掉不要的元素再做random.choice()

import random
from random import random as rd

# 猜數字遊戲，Ans: 隨機1~100之間的整數
# ans = int(rd()*100+1)
# guess = 0
# l=1
# r=100
def catch_num():
    ans = int(rd()*100+1)
    guess = 0
    l=1
    r=100

    while ans != guess:
        guess = int(input('請在'+ str(l)+ '到'+str((r))+ '之間猜一個數:'))
        
        if guess < ans:
            print('比答案小')
            l = guess+1

        elif guess > ans:
            print('比答案大')
            r = guess-1
    print('恭喜猜中')



# 猜數字遊戲，Ans: 避開avoid_lt的隨機1~100之間的整數
def catch_num2():
    avoid_lt = [4, 14, 44, 94]
    # 建立一個新的數列，將avoid_lt的數字去掉
    # 針對ans去處理，避免掉avoid_lt的元素
    num_lt  = [i for i in range(1,101) if i not in avoid_lt]
    ans = random.choice(num_lt)

    guess = 0
    l=1
    r=100

    while ans != guess:
        guess = int(input('請在'+ str(l)+ '到'+str((r))+ '之間猜一個數:'))
        
        if guess < ans:
            print('比答案小')
            l = guess+1

        elif guess > ans:
            print('比答案大')
            r = guess-1
    print('恭喜猜中')

# catch_num()
catch_num2()