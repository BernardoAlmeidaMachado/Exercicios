soma = 0
for num in range(1,101):
    if (num % 3 == 0) or (num % 5 == 0):
        soma += num
print(soma)