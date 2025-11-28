# for recursion 
# 假定有一個樓梯，你從第0階要爬到第n階，
# 每次你只能選擇爬1階或者爬2階，這樣稱做一步。
# 請寫出一個函式名為cs，給定n的値以後(n > 0)，
# 計算出從第0階爬到第n階的方法共有幾種不同的變化？
# 例：
# cs(1) = 1 (1)
# cs(2) = 2 (1+1, 2)
# cs(3) = 3 (1+2, 2+1, 1+1+1)
# cs(4) = 5 (1+1+2, 2+2, 1+2+1, 2+1+1, 1+1+1+1)
# 請分別給出遞迴解和迭代解。

# think
# 一定有一個(1*n)
# 除了cs(1)、cs(2)之外
# cs(n) = cs(n-1)+cs(n-2)


# def cs(n):
#     return 方法數
a=1
b=2
# n=a*x+b*y
# 1, recursion:
def cs(n):
    res = cs(n-1)+cs(n-2) if n>=3 else n
    return res

# def cs(n):
#     # 1st part, 檢查參數
#     try:        
#     except:
#         print('n必須是大於等於0的整數')
#     # 2nd part, 定義遞迴函式
#     def cs_cal()
#         res = cs(n-1)+cs(n-2) if n>=3 else n
#         return res
    
print(cs(5))  # 8
print(cs(1))
print(cs(0))
print(cs(-2))

# 2, iteration:
def csi(n):
    # 先排除1、2
    if  0<= n <=2:
        return n
    else:
        for i in range(3, n+1):
            

