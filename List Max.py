# find the largest number in the list

numbers = [2, 5, 6, 45, 3, 44, 2, 4, 23]
largest_number = 0
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)