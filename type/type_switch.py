# 型態可以輕易轉換
# 如:
a=1
int(a)
# int()會無條件捨棄
# int()只會計算，不會直接修改變數本身
b=3.14
print(int(b))
print(b)

int(a)
float(a)

# int + float = float
c = a + b
print(c)

# int, str()
int('50'+'2')