# obj
# 以python的角度來說，任何東西都是物件
# 物件有自己的方法，有一些屬於他的變數(屬性)
# 為了"簡化"
# 創建物件(object)之前，要先創建類別(class)
# 考慮處禮物標的共通性

class Student():
    pass #pass表示暫時不做任何事情，但是將來必須填補

class Student():
    def __init__(self, name):
        self.name = name  # name是屬性
    # 一個obj被初始畫的時候，最先呼叫的是init函式
    # 必須是self開頭
    # self指這個物件本體 (類似js的this)

    # name在第一個位置，代表呼叫student的時候，第一個傳入的將是name

    def readyName(self):
        print('聽清楚了，我的名字是' + self.name + '!!!')


ming = Student('小明') #小明是學生
mei = Student('小美')  #小美也是學生，但是和小明"不同"
# 小明和小美都是obj
print(ming.name)
print(mei.name)
ming.readyName()
mei.readyName()
