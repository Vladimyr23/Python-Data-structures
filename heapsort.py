marks = [10,4,25,7,17,2]
top=len(marks)
def heap_sort(marks):
    first=0
    last=top-1
    create_heap(marks,first,last)
    for i in range(last,first,-1):
        marks[i], marks[first]=marks[first],marks[i]
        establish_heap_property(marks,first,i-1)


def create_heap(marks, first, last):
    i=last/2
    while i>=first:
        establish_heap_property(marks,i,last)
        i=i-1

def establish_heap_property(marks, first, last):
    while 2*first+1<=last:
        k=2*first+1
        if k<last and marks[k]<marks[k+1]:
            k=k+1
        if marks[first]>= marks[k]:
            break
        marks[first],marks[k]= marks[k], marks[first]
        first=k

heap_sort(marks)
print (marks)



