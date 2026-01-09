# 要讀寫一個file之前，要先"打開"它
# 2方法，基本上只是語法不同，以及一個需要手動close
# 方法一: 用open函式打開
file = open(name, mode)
# ...接著就可以用file來使用打開的檔案
file.close()  # 用完要記得關閉檔案

# 方法二 : 用with open() as ...語法
with open(name, mode) as file
# ...接著就可以用file來使用打開的檔案
# 離開with區域，file會自動關閉
