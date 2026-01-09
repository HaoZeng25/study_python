# 讀取file
# 讀黨比寫入更在意一次讀取的內容，也要注意編碼問題
# read(), readline(), readlines()

# read() 讀全部
f = open('poem.txt', 'r', encoding = 'utf-8')
poem = f.read()
print(poem)

f.close()

# read()可以指定要讀幾個'字元'
print('指定讀取字元數:')
f = open('poem.txt', 'r', encoding = 'utf-8')
poem = ''
word_num = 3
while True:
    next = f.read(word_num)
    if not next: # 讀到空字串時，next的值會變成False，此時該停
        break
    poem += next
print(poem)

f.close()

# readline() 讀一行
print('使用readline讀取:')
f = open('poem.txt', 'r', encoding = 'utf-8')
cnt= 0
poem = ''
while True:
    cnt +=1 # 為了數行數
    line = f.readline()
    if not line:
        break
    print('Line %d: %s' % (cnt, line), end='')  # readline讀到的行尾會有換行符號，所以print時不需要再換行
    poem += line

f.close()

# readllines() 會按行將讀出來的每一行為單位組成list
print('\n使用readlines讀取:')
f = open('poem.txt', 'r', encoding = 'utf-8')
lines = f.readlines()
print(lines)
