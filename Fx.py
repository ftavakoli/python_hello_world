# print F using nested for loop
# XXXXX
# XX
# XXXXX
# XX
# XX

numbers = [5, 2, 5, 2, 2]
for item in numbers:
    output = ''
    for i in range(item):
        output += 'X'
    print(output)