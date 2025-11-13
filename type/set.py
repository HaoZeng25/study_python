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




