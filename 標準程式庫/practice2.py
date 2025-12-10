# 給定兩個字串s跟t，已經知道t的組成是將s的字母打亂以後進行重組，再隨機加上一個字母。
# 請用前面所學，找出被加上的那個字母。

# 方法2 : 用collections.Counter
# Counter可以計算每個字母的出現次數，且支援減法
# 前提是已知t、s

# 假設t 和 s 已知如下:
s = 'abcd'
t = 'abcde'

import collections
def find_dif(s, t):
    count_s = collections.Counter(s)
    count_t = collections.Counter(t)

# 相減會直接剩下多出來的字母
    diff = count_t - count_s

# 取得剩下來字母的key
    return list(diff.keys())[0]

print(find_dif(s,t))