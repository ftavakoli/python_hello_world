# Removing the duplicates from the list
####### 1
numbers = [2, 3, 4, 5, 6, 2, 2, 3]
no_duplicate = []
for number in numbers:
    if number not in no_duplicate:
        no_duplicate.append(number)
print(no_duplicate)

####### 2
clean_list = []
[clean_list.append(x) for x in numbers if x not in clean_list]
print(clean_list)

####### 3

print(list(set(numbers)))
