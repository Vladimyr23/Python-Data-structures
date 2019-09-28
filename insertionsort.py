marks = [10,4,25,7,17,2]
top=len(marks)


for i in range(1,top):
    temp = marks[i]
    j=i
    while j>0 and marks[j-1] > temp:
        marks[j] = marks [j-1]
        j=j-1
    marks[j]=temp
print marks
