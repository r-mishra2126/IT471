"""def Merge(dict1, dict2): 
    return(dict2.update(dict1)) 
      
# Driver code 
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 
  
# This return None 
print(Merge(dict1, dict2)) 
  
# changes made in dict2 
print(dict2)""" 

def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 

dict1={'id_no':1, 'name':'jack', "age":25, 'work':'engineer', 'nation': 'Britain', 6:[5,6,7]}
dict2={'control':2, 'subname':'ashok', "no":35, 'occup':'scientist', 'country': 'India', 5:[4,3,2]}
dict3 = Merge(dict1, dict2) 
print(dict3) 
