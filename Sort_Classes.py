#-------------------------------------------------------------------------------
# Name:        Sorting with classes
# Purpose:
#
# Author:      Osnovnoy
#
# Created:     20/09/2016
# Copyright:   (c) Osnovnoy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from List import List


def main():
    search=""
    next=""

    while next != "n":
        next = raw_input("Create a list? n to quit")
        if next != "n":

            #List making
            list=List()
            print list.toString()

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


if __name__ == '__main__':
    main()
