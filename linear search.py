marks = [10,4,25,7,17,2]

def isfound(number, marks):
    if number in marks:
        return 1
    return 0

print isfound(17,marks)