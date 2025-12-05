# 給定兩個字串s跟t，已經知道t的組成是將s的字母打亂以後進行重組，再隨機加上一個字母。
# 請用前面所學，找出被加上的那個字母。

s = 'abcde'
# t = s打亂重組+隨機字母 -> 轉換成數字候用random?
# 找出的方法: Counter()?

# ASCII Code:
# ord(): 將字元轉換成對應 AS code
# chr(): 將AS code 轉換成對應字元

ls = []
ls[0]= 'a'
