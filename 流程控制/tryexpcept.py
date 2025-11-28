# try
    # 有可能發生例外的程式碼
# except
    # 發生例外時要執行的程式碼
    # 可能會接continue, break等控制迴圈的語法

print("-------------------\n")
print("猜數字遊戲開始! \n")
ans = 37
guess = 0
l=1
r=100
while ans != guess:
    try:
        guess = int(input('請在'+ str(1)+ '到'+str(r)+'之間猜一個數:'))
    except:
        print('錯了錯了，這裡只吃數字喔!請重新輸入:')
        continue

    if guess < ans:
        print('比答案小')
        l = guess+1

    elif guess > ans:
        print('比答案大')
        r = guess-1
print('666，恭喜猜中!')