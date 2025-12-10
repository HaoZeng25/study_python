# 給定兩個字串s跟t，已經知道t的組成是將s的字母打亂以後進行重組，再隨機加上一個字母。
# 請用前面所學，找出被加上的那個字母。

# t = s打亂重組+隨機字母 -> 轉換成數字候用random?
# 找出的方法: Counter()?

# 我的想法:
# 將s變成list(記得最後變回string)，用地三方函式庫打亂順序:
# - random.shuffle() 原地打亂
# - random.sample() 創建一個新的
# 隨機字母: string.ascii_letters
# letters = string.ascii_letters
# random_letter = random.choice(letters)
# t = random.sample(s, len(s)).append(random_letter)
# 找出隨機字母: return random_letter

# my 方法
import random, string
s = 'abcd'
letters = string.ascii_letters
random_letter = random.choice(letters)
# t = random.sample(s, len(s)).append(random_letter)
# append不會回傳值，所以先產生list再賦值
t_list = random.sample(s, len(s))
t_list.append(random_letter)    # 原地修改
# 題目要求'隨機'位置，所以再打亂一次
random.shuffle(t_list)
t = ''.join(t_list)

print(t)
print('隨機字母:'+ random_letter)

# ASCII Code:
# ord(): 將字元轉換成對應 AS code
# chr(): 將AS code 轉換成對應字元

