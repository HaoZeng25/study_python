import os
# 可以使用目前OS的一些功能
# 如: 檔案的路徑檢查、列出檔案列表、檔案複製/移動/改名/刪除 類似powershell可以做到的一些事情

# os.path.exists() 
# 取得檔案路徑
    # 可放絕對路徑 or 相對路徑
print(os.path.exists('OS/os.py'))
print(os.path.exists('classA.json'))
print(os.path.exists('day0/fromzero.py'))
print(os.path.exists('type/dict.py')) 

print('======')

# os.path.isdir() # 判斷是否為資料夾
# os.path.isfile() # 判斷是否為檔案
print(os.path.isfile('OS/os.py'))
print(os.path.isdir('OS'))

print('======')

# 更名/重新命名
# os.rename(A , B) # 將檔案A更名as B
# os.rename('OS/move_os.py', 'OS/rename_os.py')

print('======')

# 新增 & 刪除 folder
# os.mkdir()
# os.rmdir()
# 刪除 file
# os.remove()

print('======')

# 列出folder內所有檔案和資料夾
# print(os.listdir('OS'))
    # 注意 : 只會列出第一層的檔案和資料夾，並不會列出子資料夾內的內容

print('======')

# copy, move  & rename
import shutil
# shutil.copy(A, B) # 複製檔案A到B
# shutil.move(A, B) # 移動檔案A 到路徑B並'更名'
shutil.copy('OS/os.py', 'OS/copy_os.py')
shutil.move('OS/copy_os.py', 'OS/move_os.py')

print('======')

# 遍歷整個folder內的所有檔案和資料夾
# 內容會以(dirpath, dirnames, filenames)的形式回傳
# os.wakl()
# 可以用loop 存進變數，印出來
os.walk('.')
for root, dirs, files in os.walk('.'): # os.walk()必須要給一個路徑,程式才會知道要在哪裡'走'
    print(root)
    # 印出檔案
    for f in files:
        # print(f) # 這個會印出資料夾名稱，接著印出資料夾之下的檔案名稱
        # print(os.path.join(root,f))  # 這個會印出資料夾名稱+檔案名稱，也就是每個檔案完整的路徑(基於給的root路徑)
            # print(f) 比較好閱讀
        # 避免印出git資料夾內的東西
        if not root.startswith('.git'):
            print(f)