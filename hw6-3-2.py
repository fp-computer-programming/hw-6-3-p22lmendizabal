# author: LM (AMDG) 11/15/21
number = list(input("enter a list of numbers: "))
print(number)
numbercopy = number.copy()
numbercopy.sort()
if number == numbercopy:
    print(str(number) + "is sorted.")
else:
    number.sort()
    print(str(number) + "Original list was not sorted")