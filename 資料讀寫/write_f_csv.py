# 這次是嘗試將student.csv讀回來，使用csv 的 reader
import csv
with open('student.csv', 'r', encoding='utf-8') as f:
    csvr = csv.reader(f, delimiter=' ') 
    student_from_file = [row for row in csvr] # 讀取所有row，並存在list中

print(student_from_file)
# rs : [['姓名', '數學', '英文', '物理'], ['阿明', '55', '70', '55'], ['小美', '90', '88', '100'], ['HowHow', '80', '60', '40']]
