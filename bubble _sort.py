#-------------------------------------------------------------------------------
# Name:        bubble_sort
# Purpose:
#
# Author:      Osnovnoy
#
# Created:     06/09/2016
# Copyright:   (c) Osnovnoy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

element=''
list=[]
j=1
while element != "end":
    element = raw_input ("Please input the element value \n or end to display array elements and start search")
    if element != "end":
        element=int(element)
        list.append(element)
top=len(list)
i=0
print (list)
while j!=0:
    j=0
    while i < (top-1):
        if list[i] > list[i+1]:
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp
            j=j+1
    print (i)
    print (list[i])
    print (list[i+1])
    i=i+1
print (list)

