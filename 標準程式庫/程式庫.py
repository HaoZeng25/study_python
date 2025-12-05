# 使用函式的時候，盡量留意當前目標是甚麼，避免耗費過多時間&效能在不必要的計算

# get()，輸入key，取得某個值

# In collections 模組中
# defaultdict()
# 當key沒有被指定value時，採用 初始化給的值
# 根據初始給不同的資料型態，會給不同的值
# 未給定初值，會
from collections import defaultdict

cnt = defaultdict(int)  # int() -> 0
cnt[3] # 0
cnt['a'] = 2
cnt.get('a') # 2

# Counter()
# 計算東西出現次數
# counter產生的型態類似dict
from collections import Counter
scores = [35,70,10,20,35,70,70]
score_counter = Counter(scores) # 將list代入，產生一個counter型態的東西
# 內涵元素的計數

names = ['James', 'Michael', 'Ted', 'James', 'Leo']
print(Counter(names))

# counter之間可以做數學運算: 將對應key出現的次數做加減(小於0的會去掉)
# 使用&和 | 會向set一樣，取交集和聯集

# 上述方法都不一定按照原順序
# 若在意原順序，選用OrderedDict
from collections import OrderedDict
scores2 = OrderedDict([('James', 80), ('Andy', 70), ('Curry', 100)]) # 每組key pair要用tuple包起來

# 用loop驗證，放進去的順序和取出的順序相同
for sc in scores2:
    print(sc)

# 處裡stack 用 list
# 處裡queue(佇列)用deque
# deque()
# 一個雙向序列，可從開頭或結尾傳入或取出資料
from collections import deque
s = 'abcde'
d = deque(s) # 直接轉換成deque

d.popleft() # 從左邊"取出"，按順序，取出後會改變d，並非只是讀取
d.popleft() # 若取完了，接下來再取會抱錯
d.pop() # 從右邊取出
print(d)

d.append('XDFES')
d.appendleft('YES')
print(d)


