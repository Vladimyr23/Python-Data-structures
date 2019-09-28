marks = [2,4,7,10,17,25]

def binsearch(seq, search):
   right = len(seq)
   left = 0
   previous_centre = -1
   if search < seq[0]:
       return -1
   while 1:
       centre = (left + right) / 2
       candidate = seq[centre]
       if search == candidate:
           return centre
       if centre == previous_centre:
           return - 2 - centre
       elif search < candidate:
           right = centre
       else:
           left = centre
       previous_centre = centre

print binsearch(marks,7)

