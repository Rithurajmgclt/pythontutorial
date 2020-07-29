list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
list2=[33,55,332,150,223]
list3=[]
for item in list1:
	if item  not in list2:
		list3.append(item)
		
print(list3)		
  
