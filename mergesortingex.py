"""
 We continually copy the smaller value between left[i] and right[j] into
 the result list and advance that value's index
"""
def merge(left, right):
    result = []
    i ,j = 0, 0
    while(i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result += left[i:]
    result += right[j:]
    return result
"""
Boundary condition: If an input has less than two elements, it simply returns
the input because there is no need to sort less than two elements.
Recursive condition: If an input has more than one elements, it divides
the input into two sublists and recursively run mergesort() methods to sort
each sublist. Then it merges two sublists using merge() method.
"""
def mergesort(list):
    print list
    if len(list) < 2:
        return list
    else:
        middle = len(list) / 2
        left = mergesort(list[:middle])
        right = mergesort(list[middle:])
        return merge(left, right)

#main program entry
print mergesort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5])
