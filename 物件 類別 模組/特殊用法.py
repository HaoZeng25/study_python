# 自己重新定義運算子
class nmod3():
    def __init__(self, num):
        self.num = num
        
    def __eq__(self, n2): # 定義 "=="這個運算子為是否除以3的餘數相同
        return self.num % 3 == n2.num % 3   # 回傳布林值(True/False)
        
a = nmod3(11) # 除以3餘2
b = nmod3(18) # 除以3餘0
c = nmod3(17) # 除以3餘2

print(a == b)
print(a == c)
print(b == c)


# 額外
# 這些都是兩個物件相比，我們假定後面的物件叫b。
# __eq__ => self == b
# __ne__ => self != b
# __lt__ => self < b
# __gt__ => self > b
# __add__ => self + b
# __mul__ => self * b # 原來字串的乘法是這麼弄出來的XD
# __len__ => len(self) # 可以定義什麼是你的物件的"長度"
# ...(其他有需要再Google即可XD)