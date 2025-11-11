# list
# 一系列有序的資料集合
# 無須拘泥type，可以混合不同型別的資料
lt = []
llt = list()
lt, llt # ([], []), 因為兩者皆為空串列
lt = lt = ['my', 'dict', 'doesn\'t', 'have', 'the', 'word', 'giving', 'up.', 9527, True]
# list 未規定型別限制，可放入任意型別資料
type(lt)
lt[:-2]
md = ' '.join(lt[:-2])
print(md)
print(md.split(' '))
# 用split()可以將字串轉回list串列
# 用負的索引值(如:[-1])倒回去數，不會是-0開始，而是-1開始

lt3=[[1,2],[3,4,5],[6,7,9,0],'X','D']
lt[0]
lt[0][1]
lt[0][2] # 會出錯，因為lt[0]只有兩個元素，超出範圍會報 out of range 錯誤
# lt.append(element)
# lt.expend([e1,e2,...]) 將多個元素加入串列，與append不同的是，append是將整個元素當作一個加入串列，而expend是將多個元素逐一加入串列
# lt.insert(index,element)
# del lt[index]
# lt.remove(name)  挑除，尋找符合name的element並刪除
# lt.pop()  彈出串列最後一個元素並回傳該元素
# lt.pop(index)  彈出串列指定index的元素並回傳
# lt.index(name) 搜尋。回傳name在串列中的index位置
# xx in lt  判斷xx是否在串列中，回傳True或False
# lt2= sorted(lt) 回傳排序後的新串列lt2，原串列lt不變，要注意排序時，串列內的元素必須是可比較的，如str和int不可混合排序
# lt.sort() 將原串列lt排序，無回傳值