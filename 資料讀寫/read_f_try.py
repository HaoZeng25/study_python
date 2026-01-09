# 由於讀寫file有可能出錯，所以會使用try...except的機制來給予錯誤應對措施
try:
    with open('poem.txt', 'x') as f: 
        f.write('窗外的麻雀\n')
except FileExistsError:
    print('檔案已存在!')
