# 政府資料開放平臺上有提供不少的免費取用的資料，
# 請將 https://data.gov.tw/dataset/6224 的JSON格式檔案下載下來。
# 請用上面示範的方式將其打開並存成一個Python的資料結構，命名為bs，
# 這中間可能會遇到讀取的問題，是JSON檔文字編碼的錯誤，
# 請在打開檔案時額外給入 encoding="utf-8" 的參數。
# bs是一個什麼？(字串？串列？字典？)
    # list 清單
# 請利用前面所學，將所有位在'臺北市'的書店資訊存成一個串列，名為taipei。
# taipei中特色書店點閱數超過2000的店家是哪幾家呢？請列出其名字。

# 打開file
# 轉成python物件，命名bs
# 注意編碼問題
# bs的資料型態
# 將所有 位置='臺北市' 的書店存成串列，命名taipei
    # address includes '臺北市'
    # 
# 篩選出 點閱數>2000 的店家，存成python資料，列出名字

import json
# 打開
with open('govbook.json', 'r', encoding = 'utf-8')as f:
    bs = json.load(f)
    print(type(bs))

    # test bs是否正確
    # print(bs)
    print(len(bs))  

    # 先將空白taipei宣告出來
    # "走過"找到整張清單 => "遍歷" => 用loop
    # 找到所有有'cityName'屬性的書店物件
    # 確定'cityName'屬性含有'臺北市'字串的書店物件
    # 將這些符合條件的對應物件(書店)，整個放入一個串列(也就是前面宣告的taipei)
    taipei = []
    for bookshop in bs: # 遍歷此串列的第一層元素(命名bookshop，即代表每個書店物件)，一個一個的bookshop被從bs拿出來，執行下面的動作
        if bookshop.get('cityName') and '臺北市' in bookshop['cityName']:
            taipei.append(bookshop)            
        
    print(type(taipei))
    print(taipei)
    print(len(taipei))  
    
    # [Bonus]為了方便閱讀，我想產生一個新的json檔案，將taipei放進去

    # 新增json檔案
    # 打開json檔案
    # 將taipei寫入
    with open('taipei_bookstore.json', 'w', encoding='utf-8') as f:
        json.dump(taipei, f, ensure_ascii=False, indent=4)

