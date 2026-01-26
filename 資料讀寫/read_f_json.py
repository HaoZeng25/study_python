# 對於程式開發，有些較為複雜的資料，如有大量"層級"的資料，csv難以應付，例如:巢狀結構、清單、布林值等
# 這時候可以使用json模組來處理較為複雜的資料

# Python提供的json模組在進行dump/dumps方法時，
# 預設所有輸進來的內容全都是ASCII Code，所以像中文、日文、韓文等非ASCII字元都會被轉換成\uXXXX的形式
import json

how_school = {
  "校長": "How哥",
  "工友": "林阿嘉",
  "class": {
    "A": {
      "teacher": "蔡阿嘎",
      "students": {
        "阿明": {"數學":55, "英文":70, "物理":55},
        "HowHow": {"數學":80, "英文":60, "物理":40}
      }
    },
    "B": {
      "teacher": "二伯",
      "students": {
        "小美": {"數學":90, "英文":88, "物理":100},
        "蔡哥": {"數學":50, "英文":50, "物理":40}
      }
    }
  }
}

# dumps方法 : 將Python物件轉換成JSON字串
how_json = json.dumps(how_school, ensure_ascii = False)
# print(how_json)

# loads方法 : 將JSON字串轉換成Python物件
how2 = json.loads(how_json)
# print(how2)

# 寫入json
classA = how2['class']['A']
with open('classA.json', 'w', encoding= 'utf-8') as f:
  json.dump(classA, f)

with open('classA.json', 'w', encoding= 'utf-8') as f:
  json.dump(classA, f, ensure_ascii= False, indent= 4)  # indent參數可以讓json檔案內容更好閱讀

# Next, 讀出json內容
with open('classA.json', 'r', encoding= 'utf-8') as f:
  readclassA = json.load(f)
  print(readclassA)

  # json當中的每個object必須要是獨一無二的，也就是不可以重名！
# 其實這點對照一下Python的字典應該就清楚了

reapeted_json = '{"數學": 80, "數學": 50, "數學": 30}'
json.loads(reapeted_json)  # 會得到{'數學': 30}，也就是最後一個數學的值，因為後面會覆蓋前面的值