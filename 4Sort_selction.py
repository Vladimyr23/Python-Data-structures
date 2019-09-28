#-------------------------------------------------------------------------------
# Name:        4SortsSelection
# Purpose:
#
# Author:      Osnovnoy
#
# Created:     13/09/2016
# Copyright:   (c) Osnovnoy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def list_making(list):
    #List making
    element=''
    list=[]
    j=1
    while element != "end":
        element = raw_input ("Please input the element value \n or end to display array elements and start sorting")
        if element != "end":
            element=int(element)
            list.append(element)
    return list

def insertion(list):
    #insertion sort
    i=0
    j=0
    top=len(list)
    for i in range(1,top):
        temp = list[i]
        j=i
        while j>0 and list[j-1] > temp:
            list[j] = list[j-1]
            j=j-1
        list[j]=temp
    return list

def selection(list):
    #selection sort
    top=len(list)
    i=0
    j=0
    for i in range(0,top):
        min=i
        for j in range(i+1,top):
            if list[j] < list[min]:
                min=j
        list[i], list[min]= list [min], list[i]
    return list

def bubble_s(list):
    #bubble sort
    top=len(list)
    i=0
    for i in range (0,top):
        for j in range (0,top-1):
            if list[j]>list[j+1]:
                temp=list[j+1]
                list[j+1]=list[j]
                list[j]=temp
            j=j+1
        i=i+1
    return list

def merge_s(list):
    #merge sort
    top=len(list)

    def merge_sort(list):
        merge_sort_r(list, 0, top-1)

    def merge (list, first, last, sred):
        helper_list =[]

        i=first
        j=sred+1
        while i<= sred and j<=last:
            if list[i]<= list[j]:
                helper_list.append(list[i])
                i=i+1
            else:
                helper_list.append(list[j])
                j=j+1
        while i <=sred:
            helper_list.append(list[i])
            i=i+1
        while j<= last:
            helper_list.append(list[j])
            j=j+1
        for k in range(0, last-first+1):
            list[first+k]=helper_list[k]

    def merge_sort_r(list, first, last):
        if first<last:
            sred=((first+last)/2)
            merge_sort_r(list, first,sred)
            merge_sort_r(list, sred+1,last)
            merge(list,first,last,sred)

    merge_sort(list)
    return list

search=""
next=""

while next != "n":
    next = raw_input("Create a list? n to quit")
    if next != "n":

        #List making
        list=list_making(list)
        print list

        #sort select
        search=raw_input("Please input i for insertion, s for selection, \n b for bubble sort, m for merge or q to quit")

        #insertion search result
        if search == "i":
            sorted_list = insertion(list)
            print sorted_list
            print ("The list was sorted. Create another list?")


        #selection search result
        elif search == "s":
            sorted_list = selection(list)
            print sorted_list
            print ("The list was sorted. Create another list?")


        #bubble search result
        elif search == "b":
            sorted_list = bubble_s(list)
            print sorted_list
            print ("The list was sorted. Create another list?")


        #merge search result
        elif search == "m":
            sorted_list = merge_s(list)
            print sorted_list
            print ("The list was sorted. Create another list?")

        #Quit
        elif search == "q":
            break

        #Incorrect input
        else:
            print ("Please enter i, s, b, m or q only")
    else:
        break
