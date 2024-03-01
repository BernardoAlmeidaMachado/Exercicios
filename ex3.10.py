e_primo = True
for x in range(1, 101):
    e_primo = True
    for y in range(1, x + 1):
        if (x % y == 0) and y != 1 and y != x:
            e_primo = False
    if e_primo:
        print(x)