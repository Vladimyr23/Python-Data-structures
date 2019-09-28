#-------------------------------------------------------------------------------
# Name:        List making
# Purpose:
#
# Author:      Osnovnoy
#
# Created:     20/09/2016
# Copyright:   (c) Osnovnoy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class List:
    #List making
    def __init__(self):
        element=''
        self.list=[]
        j=1
        while element != "end":
            element = raw_input ("Please input the element value \n or end to display array elements and start sorting")
            if element != "end":
                element=int(element)
                self.list.append(element)

    #return list
    def toString(self):
        info = "Here is the array - \n"
        for j in self.list:
            info = info + j.toString() + "\n"
        return info