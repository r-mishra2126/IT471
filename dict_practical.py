dict1={'id_no':1, 'name':'jack', "age":25, 'work':'engineer', 'nation': 'Britain', 6:[5,6,7]}
dict2={'id_no':2, 'name':'ashok', "age":35, 'work':'scientist', 'nation': 'India', 6:[5,6,7]}
print(dict1)
print(dict2)

#update the item at 4th location
dict1['work']= 'doctor'
dict2['work']= 'physicist'
print(dict1)
print(dict2)

#display item from 1 to 3
keys = ('id_no','name','age')
d1={k : dict1[k] for k in keys}
print(d1)
keys = ('id_no','name','age')
d2={k : dict2[k] for k in keys}
print(d2)

#insert item at first location
from pprint import pprint
from collections import OrderedDict


def insert_key_value(a_dict, key, pos_key, value):
    new_dict = OrderedDict()
    for k, v in a_dict.items():
        if k==pos_key:
            new_dict[key] = value  # insert new key
        new_dict[k] = v
    return new_dict


mydict = OrderedDict([('id_no',1), ('name','jack'), ("age",25) , ('work','engineer'), ('nation', 'Britain'), (6,[3,4,2])])
my_new_dict = insert_key_value(mydict, "Phone", "id_no", "1234")
pprint(my_new_dict)

#print key and values separately
print ("Dict value are : ") 
for i in dict1 : 
    print(dict1[i]) 

print ("Dict keys are : ") 
for i in dict1 : 
    print(i)
    
print ("Dict value are : ") 
for i in dict2 : 
    print(dict2[i]) 

print ("Dict keys are : ") 
for i in dict2 : 
    print(i) 

#comparing two dictionaries
common_pairs = dict()
for key in dict1:
    if (key in dict2 and dict1[key] == dict2[key]):
        common_pairs[key] = dict1[key]
print(common_pairs)

#adding two dictionaries

def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 

dict4={'id_no':1, 'name':'jack', "age":25, 'work':'engineer', 'nation': 'Britain', 6:[5,6,7]}
dict5={'control':2, 'subname':'ashok', "no":35, 'occup':'scientist', 'country': 'India', 5:[4,3,2]}
dict3 = Merge(dict4, dict5) 
print(dict3)

#delete item from dictionary and deleting whole dict

dict1.pop('name')
dict2.pop('nation')
print(dict1)
print(dict2)

dict1.clear()
dict2.clear()
print(dict1)
print(dict2)
del dict1
del dict2

print(dict1)
print(dict2)

