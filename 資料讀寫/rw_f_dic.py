# 處理字典用 DicWriter/DicReader
import csv
# write
# with open('student_dic.csv', 'w', newline='', encoding= 'utf-8') as f:
#     field = ['姓名', '數學', '英文', '物理'] # 第一個row做為欄位名稱
#     csvw = csv.DictWriter(f, delimiter= ' ', fieldnames= field)
#     csvw.writeheader()  # 寫入欄位名稱
#     csvw.writerow({'姓名':'阿明', '數學':55, '英文':70, '物理':55})
#     csvw.writerow({'姓名':'小美', '數學':90, '英文':88, '物理':100})
#     csvw.writerow({'姓名':'HowHow','數學':80, '英文':60, '物理':40})

# read
# with open('student_dic.csv', 'r', encoding= 'utf-8') as f:
#     # DictReader 將第一row當作雷為名稱，所以就省略了，不需要再指定欄位名稱
#     csvr = csv.DictReader(f, delimiter=' ')
#     student = [row for row in csvr]
#     print(student)

# 完善:因為讀未知檔案的時候，無法保證csv能正常運作，所以用try-except包起來，做例外處理
try:
    with open('student_dic.csv', 'w', newline='', encoding= 'utf-8') as f:
        field = ['姓名', '數學', '英文', '物理'] # 第一個row做為欄位名稱
        csvw = csv.DictWriter(f, delimiter= ' ', fieldnames= field)
        csvw.writeheader()  # 寫入欄位名稱
        csvw.writerow({'姓名':'阿明', '數學':55, '英文':70, '物理':55})
        csvw.writerow({'姓名':'小美', '數學':90, '英文':88, '物理':100})
        csvw.writerow({'姓名':'HowHow','數學':80, '英文':60, '物理':40})

    with open('student_dic.csv', 'r', encoding= 'utf-8') as f:
        # DictReader 將第一row當作雷為名稱，所以就省略了，不需要再指定欄位名稱
        csvr = csv.DictReader(f, delimiter=' ')
        student = [row for row in csvr]
        print(student)

except csv.Error as e:
    print(f'CSV檔案錯誤: {e}')