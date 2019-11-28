newlist = []
list = [1,1,2,3,5,8,13,21,34,55,89]
for i in range(0,len(list)-1):
    if(list[i]<5):
        newlist.append(list[i])

print(newlist)
