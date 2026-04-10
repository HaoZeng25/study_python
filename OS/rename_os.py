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

# copy, move  & rename
import shutil
# shutil.copy(A, B) # 複製檔案A到B
# shutil.move(A, B) # 移動檔案A 到路徑B並'更名'
shutil.copy('OS/os.py', 'OS/copy_os.py')
shutil.move('OS/copy_os.py', 'OS/move_os.py')

# 更名/重新命名
# os.rename(A , B) # 將檔案A更名as B
os.rename('OS/move_os.py', 'OS/rename_os.py')
