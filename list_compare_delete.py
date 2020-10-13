ask=[1,'a',2.2,'john',1+2j]
tell=[3,{5,6},3.45,"foot",3+4j]
ask[4]=3+4j #updates item at 5th location
print(ask)
print(tell[0:3]) #display item from 1 to 3
tell.insert(0,56)#insert item at 1st location
print(tell)
print(ask[0:3])  #display upto 3
ask.insert(5,5)  #display 5 at end
print(ask)
print(tell[-1]) # print last number of that list
del tell[2]   #3rd element is deleted
print(tell)

#COMPARING TWO LISTS

# initializing lists  
test_list1 = [1, 2, 4, 3, 5] 
test_list2 = [1, 2, 4, 6, 5] 
  
# printing lists 
print ("The first list is : " + str(test_list1)) 
print ("The second list is : " + str(test_list2)) 
  
# sorting both the lists 
test_list1.sort() 
test_list2.sort() 
  
# using == to check if  
# lists are equal 
if test_list1 == test_list2: 
    print ("The lists are identical") 
else : 
    print ("The lists are not identical") 

#ADDING TWO LISTS

# Initializing lists 
test_list3 = [1, 4, 5, 6, 5] 
test_list4 = [3, 5, 7, 2, 5] 
  
# using + operator to concat 
test_list3 = test_list3 + test_list4 
  
# Printing concatenated list 
print ("Concatenated list using + : "
                   + str(test_list3))
#DELETE A LIST
del(ask)
print(ask)
