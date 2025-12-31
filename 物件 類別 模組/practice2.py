# 1
# 請參照之前的Student類別，
# 假設今天有一個科系要求是(數學 * 2 + 英文 * 5)的加權分數採計，
# 定義__gt__(也就是>), __eq__(也就是==)，
# 用上面的採計方式及重新定義的比較運算子來寫成新的A.compareE(B)函式，
# 假設：
# A的加權分高於B -> A的名字 + ' > ' + B的名字
# A的加權分等於B -> A的名字 + ' == ' + B的名字
# A的加權分小於B -> A的名字 + ' < ' + B的名字
# 並分別讓阿明和HowHow比較、阿明和小美比較、小美和HowHow比較，輸出結果。
# (請保留之前compare的函式及呼叫的比較，我們兩種都要比呦!)

# 2
# 承上，請使用類別方法和屬性，在每次進行比較時就將總比較次數+1，
# 並print出來，這邊的「比較」是指compare()及compareE()都算。

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