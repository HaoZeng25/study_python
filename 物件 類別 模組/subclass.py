# subclass 子類別
# derived class 衍生類別
# 使用"繼承"(inheritance)的概念，讓一個新類別可以繼承(extend)另一個已存在的類別

# 定義 :
# 只要在類別名稱後的括號內，填入要繼承的類別名稱即可
# class SubclassName(SuperclassName):

class Car():
    def whoami(self):
        print('I\'m a car!')

class Tesla(Car):
    def __init__(self):
        # super().__init__()  # 呼叫父類別的建構子
        self.pilotmode = 1 # ON:1, OFF:0
    
    def whoami(self):
        print('I\'m a Tesla, not a trash car!')

    def autopilot_switch(self):
        self.pilotmode ^= 1 # ^= 是 XOR(互斥或)，所以會在 0 和 1 間切換
        if self.pilotmode == 0:
            print('Autopilot mode switch OFF')
        else:
            print('Autopilot mode switch ON')

car = Car()
tla = Tesla()
car.whoami()
tla.whoami()
print('---')
tla.autopilot_switch()
tla.autopilot_switch()