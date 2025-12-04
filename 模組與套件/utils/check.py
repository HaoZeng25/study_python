def getlucky():
    from random import random
    print("You are lucky today!")
    return int(random()*7 +1)  #取1~7之間的亂數