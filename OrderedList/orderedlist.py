#Program: orderedlist.py
#File: orderedlist.py
# orderednums.py
#
# Extracts a list of integers from a text file, one per line
# and creates an ordered list using the insert() method.

# Start with an empty list.
theList = []

theFile = file ( "values.txt", "r" )
for line in theFile:
   num = int( line )

     # Find the proper position of the item.
   i = 0
   while i < len( theList ) and num > theList[ i ]:
      i = i + 1

     # Insert the item.
   theList.insert( i, num )

theFile.close()
print theList
