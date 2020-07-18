# Weight converter Kg <=> lbs
weight = float(input("Weight: "))
weight_unit = input("(L)bs or (K)g: ").lower()
if weight_unit == "l":
    converted = weight * 0.45
    print(f'You are {converted} pounds')
else:
    converted = weight/0.45
    print(f'You are {converted} pounds')




