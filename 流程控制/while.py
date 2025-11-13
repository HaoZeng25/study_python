# while
# break
# continue

while True :
    mode = input('請問你要選擇甚麼模式? 1. 簡單 2. 困難 3. 專家，請輸入[1,2,3]')
    if mode == '3':
        print('\n選擇專家模式的難關，請拉兄弟下水')
        break
    elif mode == '1' or mode == '2':
        print('你看看隔壁小明，都選專家模式，你可以不要給我丟臉嗎?')

# 特殊用法
# while else，當while正常跑完，沒有跳break，就會接續跑else
mode = ''
while mode != '3' :
    mode = input('請問你要選擇甚麼模式? 1. 簡單 2. 困難 3. 專家，請輸入[1,2,3]')
    if mode == '3':
        print('\n選擇專家模式的難關，請拉兄弟下水')
    elif mode == '1' or mode == '2':
        print('你看看隔壁小明，都選專家模式，你可以不要給我丟臉嗎?\n')
    else:
        print('不想玩別玩')
        break
else : 
    print('請確認兄弟在水下了')