# function
# 函式，1)需要被定義 2)需要被呼叫，呼叫的前提條件，是必須讓此程式知道這個函式的存在 3)若定義在其他檔案中，需要import進來
# def function name(param1, param2):
#     """
#     This function takes two parameters and returns their sum.
    
#     Args:
#     param1 (int): The first parameter.
#     param2 (int): The second parameter.
    
#     Returns:
#     int: The sum of param1 and param2.
#     """
#     return param1, param2 
#     or 
#     return param1

# circle
def area(r):
    pi = 3.14
    return 3.14*r **2

circle1 = area(5)
print("circle area:", circle1)

print("-------------------")

# 變數指定
def area2(r, pi=3.14):
    return pi*r **2

print("circle area2-1:", area2(1, 3.14159))
print("circle area2-2:", area2(3))  # 使用預設值3.14
print("circle area2-3:", area2(pi=3.141, r=3))  # 順序會自動對應

print("-------------------")

# 可以使用外層的變數
def printAll(r, pi=3.14):
    def innerArea():
        return pi *r ** 2
    def perimeter():
        return 2 * pi *r
    
    # {} 的用法是 format，可以將多個變數按順序置入{}
    print('半徑 = {}的圓，其面積 = {}，周長 = {}'.format(r, perimeter(), innerArea()))

printAll(3, 3.14159)

print("-------------------")

# global 變數，FC內修改global變數時，養成習慣使用global關鍵字
fak = 'global' # 全域變數
def home1():
    print(fak)

def home2():
    fak = 'h2'
    print(fak)    

def home3():
    global fak # 宣告/指定使用全域變數
    fak = 'h3'
    print(fak)

print('Before:')
print(fak)
print('\nhome1:')
home1()
print('After home1:')
print(fak)

print('\nhome2:')
home2()
print('After home2:')
print(fak)

print('\nhome3:')
home3()
print('After home3:')
print(fak)


