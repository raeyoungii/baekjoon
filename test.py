from collections import OrderedDict

dic = OrderedDict([('1', 0), ('2', 0), ('3', 0), ('4', 0), ('5', 0), ('6', 0), ('7', 0), ('8', 0), ('9', 0)])
dic['3'] = 4
n = 3
if dic[n] > 2:
    print(dic)