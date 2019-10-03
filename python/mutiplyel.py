def edc(myList) : 
       
    result = 1
    for x in myList: 
         result = result * x  
    return result  
      
list1 = [1, 2, 3]  
list2 = [3, 2, 4] 
print(edc(list1)) 
print(edc(list2))
