# author: LM (AMDG) 11/15/21
number = input("enter elements of the list: ")
print(number)
lst1 = number.split()
lenght= len(lst1)
print(lst1)
question = input("What part of the list do you want? Middle or end? ")
if question == "middle":
    print(lst1[1:-1])
elif question == "end":
    print(str(lst1[0]) + " " + str(lst1[lenght -1]))
    