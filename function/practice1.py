# 1.請使用兩個迴圏，將1~10之間的偶數兩兩相乘並放到一個空的list中。
# (所以這個list應該會有2 * 2, 2 * 4, 2 * 6, 2 * 8, 2 * 10, 4 * 2, 4 * 4, ..., 10 * 10)

# 2.請改用列表生成式來完成1的問題。

# 3.請用while, if else等，寫出一個猜數字的遊戲，遊戲的答案為37，
# 請在開始時提示使用者猜1~100範圍中的數字，
# 並依據使用者的答案，逐步將範圍縮小，直到猜中答案，則印出恭喜訊息並離開迴圏。
# (先不考慮使用者會亂輸入的問題，並且要告訴使用者這次猜的比答案大還是小)

# 1
my_list = []
# for i in range(2,11,2):
for i in range(2,11,2):
    for j in range(2,11,2):
        my_list.append(i * j)    

print(my_list)

# 1-1 嘗試包成一個函式
"""
計算指定範圍內數字兩兩相乘的結果
    start: 起始值 (包含)
    stop:  結束值 (不包含)
    step:  間隔 (步長)
"""
def multi_num(start,stop,step):
    my_list = []                # local my_list
    for i in range(start,stop,step):
        for j in range(start,stop,step):
            my_list.append(i * j) 

    return my_list

print('嘗試包成一個函式: \n', multi_num(2,11,2))    # 偶數
print('嘗試包成一個函式: \n', multi_num(1,11,2))    # 奇數

print("-------------------")

# 2 list comprehension
my_list2 = []
my_list =  [i * j for i in range(2,11,2)   for j in range(2,11,2)]
print('list comprehension: \n', my_list)
# 2-1 嘗試包成一個函式
def multi_num2(start,stop,step):
    my_list =  [i * j for i in range(start,stop,step)   for j in range(start,stop,step)]
    return my_list
print('嘗試包成一個函式(list comprehension): \n', multi_num2(2,11,2))    # 偶數

print("-------------------")

#3 猜數字遊戲，Ans:37
ans = 37
min_val = 1
max_val = 100
print("猜數字遊戲開始! \n")

while True:
    # print ("請在{}~{}之間猜一個數字:".format(min_val, max_val))
    print (f"請在{min_val}~{max_val}之間猜一個數字:\n")

    try:
        user_input = int(input())
    except ValueError:
        print("請輸入有效的數字!")
        continue

    if user_input == ans:
        print(f"恭喜猜中!答案是{ans}")
        # 重複印出string 6次
        for _ in range(6):
            print('777')        
        break

    elif user_input < ans:
        print(f"遺憾，答案比你猜的{user_input}更大!")

        # 縮小範圍--更新min_val
        if user_input > min_val:
            min_val = user_input +1
    
    else:
        print(f"遺憾，答案比你猜的{user_input}更大!")

        if user_input < max_val:
            max_val = user_input -1


# num 第二種寫法
print("-------------------\n")
print("第二種，猜數字遊戲開始! \n")
guess = 0
l=1
r=100
while ans != guess:
    guess = int(input('請在'+ str(1)+ '到'+str(r)+'之間猜一個數:'))

    if guess < ans:
        print('比答案小')
        l = guess+1

    elif guess > ans:
        print('比答案大')
        r = guess-1
print('恭喜猜中')