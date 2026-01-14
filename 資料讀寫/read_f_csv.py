# python有內建的csv模組，可以方便讀寫csv檔案
import csv
with open('student.csv', 'w', newline='', encoding='utf-8')as f:
    csvw = csv.writer(f, delimiter = ' ')  # delimiter預設是","，可以自行更改
    csvw.writerow(['姓名', '數學', '英文', '物理'])  # 一次寫一個row
    students = [
        ['阿明',   55,  70,   55],
        ['小美',   90,  88,  100],
        ['HowHow', 80,  60,   40]
    ]
    csvw.writerows(students) # 一次寫多個rows