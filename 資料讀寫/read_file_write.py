import os

print('目前工作目錄:', os.getcwd())

f = open('poem.txt', 'w', encoding = 'utf-8')  # 指定編碼方式
f.write('院子落葉\n跟我的思念厚厚兩疊?')  # write寫入，結束時會回傳寫入的自述(byte數)
f.write('\n測試加第二句')
# print也可，就是將print目標指向到檔案
print('\n寫入完成',file = f, sep = '', end = '')


f.close()  # close後，才真正寫入完畢
# 注意: 寫入檔案時，若檔案已存在，會直接覆蓋掉原本的內容
# 檔案會在python工作目錄下產生

# 由於print()預設會有sep(分隔符號)和end(結束符號)，
# sep預設會是一個空格，end預設會是換行，
# 所以我們要自行將其設定為空字串，避免寫進去的東西不如預期