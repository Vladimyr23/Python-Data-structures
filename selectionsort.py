marks = [10,4,25,7,17,2]
top=len(marks)


for i in range(0,top):
    min=i
    for j in range(i+1,top):
        if marks[j] < marks[min]:
                min=j
    marks[i], marks[min]= marks [min], marks[i]
print marks