# 一個class可以不只計成一個class

# class C(A,B):
#     pass

# 若互相衝突(如:重名的方法)，則會以先來者得(由左至右)的順序來決定使用哪一個父類別的方法
class A():
    def __init__(self):
        self.name = 'A'
        print('A')
        print('Name = ' + self.name)

class B():
    def __init__(self):
        self.name = 'B'
        print('B')
        print('Name = ' + self.name)

class C(A, B):
    pass
    
test = C()