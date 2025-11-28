lt = [1, -5, 3, 2, 4, 10, 100]

for num  in lt:
    print(num)
    
print('-----')

index = 0
while index < len(lt):
    print (lt[index])
    index +=1

print('-----')

# dict也會產生可迭代物件，可以按順序用key value對應取出
shrimp = {'炸鳳尾蝦':['蝦子','核果','油'],'雲龍炸蝦':['蝦子','核果','油','豆皮','醬汁']}

for name, ingre in shrimp.items():
    print(name, ingre)

print('-----')

# range產生可迭代物件，(start, stop, step)
range(7)    # 只給一個數字表示是stop
range(2,7)  # 兩個數字表示是start, stop
range(2,10,3) # 三個數字表示是start, stop, step

list(range(7))  # 把range物件轉成list
list(range(2,7))
list(range(1,5,-1)) # step為負數表示遞減
list(range(1,5,2))

list(range(10, -88, -10)) # 由10開始，每次減10，直到小於-88停止

for i in range(0, len(lt), 2):
    print(lt[i])
    # 從index 0 開始，每次間隔2，直到len(lt)-1 止，因為stop的位置不算

print('-----')