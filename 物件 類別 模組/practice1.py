# (1)
# 在上述的例子當中，請為類別新增一個字典，名稱為score，
# 將該字典用來儲存{'科目':'分數'}的各科成績，並修改__init__()的函式，
# 在產生阿明及小美時，同時輸入各科成績，
# 如未輸入則預設為0分(也就是缺考)。
# 阿明的成績分別為：數學55/英文70/物理55
# 小美的成績分別為：數學90/英文88/物理100

# (2)
# 承上題，請新增一名Student，其name為'HowHow'，
# 數學成績為80，英文成績為60，物理成績為40。

# (3)
# 請為Student新增一個方法，讓兩個Student可以互相比較，
# 名稱為compare()。
# 例如A.compare(B)，假設：
# A的總分高於B -> A的名字 + '贏了！'
# A的總分等於B -> '什麼？竟然平手？！'
# A的總分小於B -> '可...可惡，難道，這就是' + B的名字 + '真正的實力嗎？'

class Student():
    # 初始化函式
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def readyName(self):
        print('聽清楚了，我的名字是' + self.name + '!!!')
        print('我的分數可是:' + str(self.score)+ '喔!')

    # 讓兩個student可以比較成績
    def compare(self, b):
        # b 是從外部傳入的另一個Student物件，也就是要比較的對象 (PS:self是自己)
        diff = sum(self.score.values()) - sum(b.score.values())
        # diff 是自己和對方的總分差距

        if diff > 0:
            print(self.name + '贏了!')
        elif diff == 0:
            print('What! 竟然平手?')
        elif diff < 0: 
            print('可...可惡，難道，這就是' + b.name + '真正的實力嗎？')

# 呼叫時同時給予成績(注意要對應科目，程式才會知道)，成績若複數個，可以用list
ming = Student( '小明',{'數學':55,  '英文':70, '物理':55}) #小明是學生
mei = Student('小美', {'數學':90,  '英文':88, '物理':100})
howhow = Student('HowHow', {'數學':80,'英文':60,'物理':40})

# 驗證結果
print(ming.name, ming.score)
print(mei.name, mei.score)
print(howhow.name, howhow.score)
ming.readyName()
print('--比較成績--\n')
print('\n阿明 vs HowHow')
ming.compare(howhow)
print('\n阿明 vs 小美')
ming.compare(mei)
print('\n小美 vs HowHow')
mei.compare(howhow)