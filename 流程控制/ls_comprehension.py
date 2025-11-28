# list comprehension 列表生成式 串列生成式/串列表達式/串列解析式
# 用來快速生成列表的語法
# 透過簡潔的語法來創建和操作列表
# 語法: [expression for item in iterable if condition]
# 如
[i for i in range(9)] # 等於list(range(9))
# 將從資料撈出來的單項(i) 經過算式(expression)處理後，才放入列表中
# 也可以加上條件式(if condition)來篩選符合條件的項目
# iterable 可以是任何可迭代的物件，如列表、字串、字

ls1 = [ 2*i for i in range(9) if i % 2 == 0] # 取0~8中，能被2整除的數字，並且每個都先單獨*2再加到list
print(ls1)
# notice : 不能用'='，而要用'=='來做比較
print('-----')

# 多重for
ls2 = [[0 for i in range(3)] for j in range(4) ]
print(ls2)
print('-----')