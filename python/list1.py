list1 = [1, 2, 8, 9, 7] 
  
ag = [(val, pow(val, 2)) for val in list1] 

print(ag) 

ag2 = [(val, pow(val, 3)) for val in list1] 

print(ag2)

ag3 = [(val, pow(val, 1/2)) for val in list1] 

print(ag3)
