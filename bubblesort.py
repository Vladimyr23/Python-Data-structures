marks = [10,4,25,7,17,2]
top=len(marks)
i=0
for i in range (0,top):
    for j in range (0,top-1):
        if marks[j]>marks[j+1]:
            temp=marks[j+1]
            marks[j+1]=marks[j]
            marks[j]=temp
        j=j+1
    i=i+1
print (marks)




