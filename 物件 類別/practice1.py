# 在上述的例子當中，請為類別新增一個字典，名稱為score，
# 將該字典用來儲存{'科目':'分數'}的各科成績，並修改__init__()的函式，
# 在產生阿明及小美時，同時輸入各科成績，
# 如未輸入則預設為0分(也就是缺考)。
# 阿明的成績分別為：數學55/英文70/物理55
# 小美的成績分別為：數學90/英文88/物理100

class Student():
    def __init__(self, name, subject=0):
        self.name = name
        self.subject = subject

    def readyName(self):
        print('聽清楚了，我的名字是' + self.name + '!!!')

    # score = dict({'subject':'score'})
    score = dict({'{subject}':'{score}'})

# 呼叫時同時給予成績(注意要對應科目，程式才會知道)，成績若複數個，可以用list
ming = Student('小明') #小明是學生
mei = Student('小美')