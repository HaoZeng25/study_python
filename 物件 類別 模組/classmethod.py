class Student():
    cnt = 0  # 類別變數，屬於整個class。此處的目的:用來記錄學生人數
    def __init__(self, name, score):
        Student.cnt += 1  # 每建立一個物件，計數器就加1
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

    @classmethod
    def getCount(cls):
        # cls 代表這個類別本身(Student)
        print('目前的學生總數：%d' % cls.cnt)


print('Before Start')
Student.getCount()  # 呼叫類別方法，查看目前學生數量

ming = Student( '小明',{'數學':55,  '英文':70, '物理':55})
ming.readyName()
Student.getCount()  # 1

mei = Student('小美', {'數學':90,  '英文':88, '物理':100})
mei.readyName()
Student.getCount()  # 2

howhow = Student('HowHow', {'數學':80,'英文':60,'物理':40})
howhow.readyName()
Student.getCount()  # 3

print('--比較成績--\n')
print('\n阿明 vs HowHow')

ming.compare(howhow)
print('\n阿明 vs 小美')
ming.compare(mei)
print('\n小美 vs HowHow')
mei.compare(howhow)