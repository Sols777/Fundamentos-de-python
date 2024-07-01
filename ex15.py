list1 = [2, 3.75, 0.04, 59.34, 6,7,7.777]

ints = [ val for val in list1 if isinstance(val, int)]
print(ints)

divSete = [val for val in list1 if val%7 == 0 and val<=1000]
print(divSete)

threeinList = [val for val in list1 if val<=1000 and  '3' in str(val)]
print(threeinList)
