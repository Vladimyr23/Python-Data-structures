#-------------------------------------------------------------------------------
# Name:       Linary and binary list search
# Purpose:
#
# Author:      Osnovnoy
#
# Created:     05/09/2016
# Copyright:   (c) Osnovnoy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------



list=[]
#new_list=[]
element=0
search=""
search_element=""
found = False

#Linear search function
def linear_s(list, found):
    search_element=raw_input("Please enter the element you are looking for")
    #search_element = str(search_element).lower
    #new_list = map(str, list)
    for index, value in enumerate(list):
        print index, value
        if value==search_element:
            found = True
            print ("The element " + str(value) + " has been found at position " + str(index))
    return found

#Binary search function
def binary_s(list, found):
    search_element=raw_input("Please enter the element you are looking for")
    #search_element = str(search_element).lower
    list.sort()
    #new_list = map(str, list)
    print (list)
    lo = 0
    hi = len(list) - 1
    while lo<=hi:
        mid = (lo+hi)//2
        print mid, list[mid]
        if list[mid] < search_element:
            lo = mid + 1
        elif search_element < list[mid]:
            hi = mid - 1
        else:
            found = True
            print ("The element " + str(list[mid]) + " has been found at position " + str(mid))
            break
    return found

#list making
while element != "end":
    element = raw_input ("Please input the element value \n or end to display array elements and start search")
    #element = str(element).lower
    if element != "end":
        list.append(element)

#list print
print list

#Search selection: linear or binary
while search != "q":
    search=raw_input("Please input l for linear, b for binary search or q to quit")
    #search=str(search).lower
    #Linear search result
    if search == "l":
        found_l = linear_s(list, found)
        #ind = linary(index)
        #found
        if found_l == True:
            print ("The element you were looking for has been found. Another search?")
         #not found
        else:
            print ("The entered value not found. Another search?")
    #Binary search result
    elif search == "b":
        found_l = binary_s(list, found)
        #found
        if found_l == True:
            print ("The element you were looking for has been found. Another search?")
        #not found
        else:
            print ("The entered value not found. Another search?")
    #Quit
    elif search == "q":
        break

    #Incorrect input
    else:
        print ("Please enter l, b or q only")

