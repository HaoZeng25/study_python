# recursion 遞迴
# 當一個函式在使用時，中途不斷呼叫自己，藉以達到某些目的或完成某些問題
# 通常狀況下，寫得正常的遞迴應該會不斷在過程中將要計算的問題進行簡化

# 計算1~100
# def cal(end=100):
#     res =0
#     for i in range(1, end+1):
#         res +=i
#     return res


# 或
def cal(end):
        return end+ cal(end-1) if end !=1 else 1

print(cal(999))