marks= [10,4,25,7,17,2]

def shellsort(marks):
     "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
     gap = len(marks) // 2
     # loop over the gaps
     while gap > 0:
         # do the insertion sort
         for i in range(gap, len(marks)):
             val = marks[i]
             j = i
             while j >= gap and marks[j - gap] > val:
                 marks[j] = marks[j - gap]
                 j -= gap
             marks[j] = val
         gap //= 2

shellsort(marks)
print marks
