# set
# 只有key
# 無序
# 不重複
# 建立 : set() 或 {} 注意:{}是dict，若要set，{}內要有東西

st=set()  # 空的set
print(type(st))
st.add(1)
st.add(1)
print(st)  # {1}，重複增加不影響

set('XDDD')
print(set('XDDD'))  # {'D', 'X'}，無序不重複，自動拆開，重複者被省略

# set有許多符合數學集合概念的運算
A={1,2,3,4}
B={3,4,5,6}
print(A|B)  # 聯集 {1, 2, 3, 4, 5, 6}
print(A&B)  # 交集 {3, 4}
print(A-B)  # 差集 {1, 2}；若A有的B通通都有，計算結果為空集合set()
print(A^B)  # 對稱差集 {1, 2, 5, 6}
print(A<=B)  # 檢查前者是否為後者的子集合 False；A是B的子集合才會是True

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
lt1 = lt[0:9:2] # 取奇數
lt2 = lt[1:10:2] # 取偶數

