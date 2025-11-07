# 變數是一個箱子
# 箱子用來儲存資料
# 為了知道在找哪一個'箱子'，會為北個箱子貼上標籤並取名，這個標籤名就是變數名稱

# "=" 是賦值運算子，將等號右邊的資料'存放'進左邊的變數箱子中
# 並非數學中的等號
# 如 : a = 10 是將右邊的資料 10 放入變數 a 的箱子中

top = 1
bottom = 100
h = 100

res = (top + bottom ) *h //2 
print(res)

bottom = 200.0
res = (top + bottom ) *h /2
tb = type(bottom)
print(tb)
tr = type(res)
print(tr)
print(tb,tr)

# 兩個變數之間放上等號，等同於將同一個箱子貼上兩個標籤
a=5
b=a
# id() 取得變數所指向箱子的記憶體位址
id(a)
id(b)
# 變數 a 和 b 指向同一個箱子

pi = 3.14
width = 7.77
print(pi * width)
print("周長是:" + str(2*width*pi))
print("面積 : " + str(width*width*pi))