# dict 字典
# 與list有些類似，但是表示方式是 key:value 配對(pair, 鍵值對)
# - 建立、宣告
# 	- `dict()` 或 `{}`
# 	- 每個key和value的對應使用冒號:來分隔
# 	- 每組key:value之間，使用逗號來分開

# dict的操作方法很多跟list類似

>>> dic0=dict()
>>> dic0
{}
>>> dic1={}
>>> dic1
{}
>>> dic={'xd': 1, '放棄': False, [1,5,9]: 3}
Traceback (most recent call last):
  File "<python-input-244>", line 1, in <module>
    dic={'xd': 1, '放棄': False, [1,5,9]: 3}
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
>>> dic={'xd': 1, '放棄': False, 3.33: 3}
>>> dic
{'xd': 1, '放棄': False, 3.33: 3}
>>> dic['XD']
Traceback (most recent call last):
  File "<python-input-247>", line 1, in <module>
    dic['XD']
    ~~~^^^^^^
KeyError: 'XD'
>>> dic['xd]
  File "<python-input-248>", line 1
    dic['xd]
        ^
SyntaxError: unterminated string literal (detected at line 1)
>>> dic['xd']
1
>>> dic['xd',3.33]
Traceback (most recent call last):
  File "<python-input-250>", line 1, in <module>
    dic['xd',3.33]
    ~~~^^^^^^^^^^^
KeyError: ('xd', 3.33)
>>> dic[0]
Traceback (most recent call last):
  File "<python-input-251>", line 1, in <module>
    dic[0]
    ~~~^^^
KeyError: 0
>>> dict(1)
Traceback (most recent call last):
  File "<python-input-252>", line 1, in <module>
    dict(1)
    ~~~~^^^
TypeError: 'int' object is not iterable
>>> dict.value(1)
Traceback (most recent call last):
  File "<python-input-253>", line 1, in <module>
    dict.value(1)
    ^^^^^^^^^^
AttributeError: type object 'dict' has no attribute 'value'. Did you mean: 'values'?
>>> lol=[('易大師','我的劍，就是你的劍。'),('犽宿','死亡如風，常伴吾身。'),('阿祈爾','蘇\瑞瑪！你的王已經歸來了！')]
>>> diclol=dict(lol)
>>> tul=(['a','b'],['c','d'],['e','f'],['g','h'])
>>> type(tul)
<class 'tuple'>
>>> type({tul})
Traceback (most recent call last):
  File "<python-input-258>", line 1, in <module>
    type({tul})
         ^^^^^
TypeError: unhashable type: 'list'
>>> type(dict(tul))
<class 'dict'>
>>> tul
(['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h'])
>>> chs=['ab','cd','13']
>>> dict(chs)
{'a': 'b', 'c': 'd', '1': '3'}
>>> chs
['ab', 'cd', '13']
>>> diclol['伊澤瑞爾'] = '是時候展現真正的技術了！'
>>> diclol
{'易大師': '我的劍，就是你的劍。', '犽宿': '死亡如風，常伴吾身。', '阿祈爾': '蘇瑞瑪！你的王已經歸來了！', '伊澤瑞爾': '是時候展現真正的技術了！'}
>>> dicchs=dict(chs)
>>> dicchs['a']='XD'
>>> dicchs
{'a': 'XD', 'c': 'd', '1': '3'}
>>> dict1
Traceback (most recent call last):
  File "<python-input-269>", line 1, in <module>
    dict1
NameError: name 'dict1' is not defined. Did you mean: 'dic1'?
>>> dict
<class 'dict'>
>>> dic
{'xd': 1, '放棄': False, 3.33: 3}
>>> dic2
Traceback (most recent call last):
  File "<python-input-272>", line 1, in <module>
    dic2
NameError: name 'dic2' is not defined. Did you mean: 'dic0'?
>>> dic2={}
>>> dic2.update(dic)
>>> dic2
{'xd': 1, '放棄': False, 3.33: 3}
>>> dic1
{}
>>> del dic2[3.33]
>>> dic2
{'xd': 1, '放棄': False}
>>> dic2.clear()
>>> dic2
{}
>>> 'xd' in dic
True
>>> 'XD' in dic
False
>>> dic.keys()
dict_keys(['xd', '放棄', 3.33])
>>> list(dic.kets())
Traceback (most recent call last):
  File "<python-input-284>", line 1, in <module>
    list(dic.kets())
         ^^^^^^^^
AttributeError: 'dict' object has no attribute 'kets'. Did you mean: 'keys'?
>>> list(dic.keys())
['xd', '放棄', 3.33]
>>> dic(dic.keys())
Traceback (most recent call last):
  File "<python-input-286>", line 1, in <module>
    dic(dic.keys())
    ~~~^^^^^^^^^^^^
TypeError: 'dict' object is not callable
>>> tuple(dic.keys())
('xd', '放棄', 3.33)
>>> tuple(dic.keys())[1]
'放棄'
>>> tuple(dic.keys())[1].insert('k')
Traceback (most recent call last):
  File "<python-input-289>", line 1, in <module>
    tuple(dic.keys())[1].insert('k')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'insert'
>>> tuple(dic.keys())[1] in dic
True
>>> tuple(dic.keys())[1] in dic2
False
>>> tuple(dic.keys())[1] in dicchs
False
>>> tuple(dic.keys())[1].values
Traceback (most recent call last):
  File "<python-input-293>", line 1, in <module>
    tuple(dic.keys())[1].values
AttributeError: 'str' object has no attribute 'values'
>>> tuple(dic.keys()).values
Traceback (most recent call last):
  File "<python-input-294>", line 1, in <module>
    tuple(dic.keys()).values
AttributeError: 'tuple' object has no attribute 'values'
>>> dic.values
<built-in method values of dict object at 0x000002484ADA0C40>
>>> dic.values()
dict_values([1, False, 3])
>>> diclol['國動'] = '社 社 社社社 社社 社會搖'
>>> diclol
{'易大師': '我的劍，就是你的劍。', '犽宿': '死亡如風，常伴吾身。', '阿祈爾': '蘇瑞瑪！你的王已經歸來了！', '伊澤瑞爾': '是時候展現真正的技術了！', '國動': '社 社 社社社 社社 社會搖'}
>>> diclolfame = {'國動':'還敢下來阿冰鳥!', '統神':'他的手怎麼可以穿過我的叭叭啊！'}
>>> diclol.update(diclolfame)
>>> diclol
{'易大師': '我的劍，就是你的劍。', '犽宿': '死亡如風，常伴吾身。', '阿祈爾': '蘇瑞瑪！你的王已經歸來了！', '伊澤瑞爾': '是時候展現真正的技術了！', '國動': '還敢下來阿冰鳥!', '統神': '他的手怎麼可以穿過我的叭叭啊！'}
>>> del diclol['統神']
>>> diclol
{'易大師': '我的劍，就是你的劍。', '犽宿': '死亡如風，常伴吾身。', '阿祈爾': '蘇瑞瑪！你的王已經歸來了！', '伊澤瑞爾': '是時候展現真正的技術了！', '國動': '還敢下來阿冰鳥!'}
>>> '統神' in diclolfame
True
>>> dicchs
{'a': 'XD', 'c': 'd', '1': '3'}
>>> dicchs = {'a': 123, 'c': 428, '1': '3', 'eee': 11}
>>> dicchs
{'a': 123, 'c': 428, '1': '3', 'eee': 11}
>>> dicchs.clear()
>>> dicchs
{}
>>> '統神' in diclol
False
>>> dicn
Traceback (most recent call last):
  File "<python-input-311>", line 1, in <module>
    dicn
NameError: name 'dicn' is not defined. Did you mean: 'dic0'?
>>> dicn = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> dicn.keys
<built-in method keys of dict object at 0x000002484ADA28C0>
>>> dicn.keys()
dict_keys(['a', 'b', 'c', 'd'])
>>> dicn.keys()
dict_keys(['a', 'b', 'c', 'd'])
>>> dicn.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
>>> dict_items
Traceback (most recent call last):
  File "<python-input-317>", line 1, in <module>
    dict_items
NameError: name 'dict_items' is not defined
>>> dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
Traceback (most recent call last):
  File "<python-input-318>", line 1, in <module>
    dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
    ^^^^^^^^^^
NameError: name 'dict_items' is not defined
>>> dico=dicn
>>> dico
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> dico['a']
1
>>> dico['a']='XD'
>>> dico['a']
'XD'
>>> dicn['a']
'XD'
>>> dicn
{'a': 'XD', 'b': 2, 'c': 3, 'd': 4}
>>> dico
{'a': 'XD', 'b': 2, 'c': 3, 'd': 4}
>>> dico.clear()
>>> dico=dicn.copy()
>>> dico
{}
>>> dicn={'a': 'XD', 'b': 2, 'c': 3, 'd': 4}
>>> dico
{}
>>> dicn
{'a': 'XD', 'b': 2, 'c': 3, 'd': 4}
>>> dico=dicn.copy()
>>> dico
{'a': 'XD', 'b': 2, 'c': 3, 'd': 4}
>>> dicn
{'a': 'XD', 'b': 2, 'c': 3, 'd': 4}
>>> dico['a']
'XD'
>>> dico['a']=1
>>> dico
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> dicn
{'a': 'XD', 'b': 2, 'c': 3, 'd': 4}