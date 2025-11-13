# 練習1 料理
print('=======================')
print('練習1 料理')
# 請建立一個字典名為shrimp，當中請使用兩者的作品的名字做為key，將其做的炸蝦所使用到的材料/內容列表list做為value，還未做完成的部分不算。(如: {'炸蝦':['蝦子, '麵包粉', '雞蛋', '麵粉']} )
shrimp = {
    '炸鳳尾蝦':['蝦子', '核果','油'],
    '雲龍炸蝦':['核果','蝦子','醬汁','豆皮']
}
print(shrimp)
# 取值用print(shrimp['炸鳳尾蝦'])  # ['蝦子', '核果','油']
lee = set(shrimp['炸鳳尾蝦'])
liu= set(shrimp['雲龍炸蝦'])
print(lee)  # ['蝦子', '核果','油']
print(liu)  # ['核果','蝦子','醬汁','豆
# liu比lee多了甚麼
print(liu-lee)
# lee比liu多了甚麼
print(lee-liu)
lee.add('醬汁')
lee.add('蘋果')
lee.add('洋蔥') # 用add()，一次只能加一個element
print(lee) # {'蝦子', '核果','油','醬汁','蘋果','洋蔥'}
print(lee-liu)
shrimp['炸鳳尾蝦'] =list(lee)
print(shrimp)

# 練習2
print('===========================')
print('練習2')
lt=[1,2,3,4,5,6,7,8,9,10]
# slice
lt1 = lt[0:9:2] # 取奇數，slice也可以將0省略
lt2 = lt[1:10:2] # 取偶數

# 將lt2元素，依序加入lt1
lt1.extend(lt2) # 這會將lt2打散，將元素逐一加入lt1，會直接修改lt1，[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
# lt1.append(lt2) # 將lt2當成'1個元素'，直接加在lt1後面，[1, 3, 5, 7, 9, [2, 4, 6, 8, 10]]
print(lt1)

# 刪除多個索引
# 若先刪小再刪大，因為遞補的特性，影響運行結果
# 若反過來，先刪大的再刪小的，可避免被影響
del lt1[7]
del lt1[1]
print(lt1)
list(lt1)
print(lt1)

# 排序
lt1_1 = sorted(lt1)  # 另外產生一個新的lt，相對占用記憶體位置
lt1.sort()  # 直接修改對象lt
print(lt1)
print(lt1_1)