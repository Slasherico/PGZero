numbsequence = input("Enter a series of numbers and I will find out if it is a pangram:")

numb = {}
pangram = {0,1,2,3,4,5,6,7,8,9}

for num in numbsequence:
    if num.isdigit():
        if int(num) not in numb:
            numb[int(num)] = 1

is_pangram = True
for digit in pangram:
    if digit not in numb:
        is_pangram = False

if is_pangram:
    print("The sequence is a pangram!")
else:
    print("The sequence is not a pangram.")