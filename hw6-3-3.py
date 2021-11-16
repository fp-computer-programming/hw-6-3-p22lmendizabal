# auhor: LM (AMDG) 11/15/21
numbers = input("enter a list of 5 numbers with spaces: ")
print(numbers)
numberls = list(numbers)
numberls.sort()
numberls[0:4] = []
print(numberls)
total = (int(numberls[0]) + int(numberls[1]) + int(numberls[2]) + int(numberls[3]) + int(numberls[4]))
print("The total sum of the numbers is " + str(total))