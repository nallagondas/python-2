# Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

commaSeparatedNumbers = input("Enter Comma Seperated Numbers")
# printing the string as is
print(commaSeparatedNumbers)

lst = commaSeparatedNumbers.split(",");
# printing list generated from split function.
print(lst)

# this is a new list which contains the values as int
newLst = []

for val in lst:
    newLst.append(int(val))

# printing the new list with numbers.
print(newLst)