def numero_par (n):
    if n % 2 == 0:
        print(f"{n}: o numero e par")
    else:
        print(f"{n}: o numero e impar")

num1= int(input("digite um numero: "))
num2= int(input("digite um numero: "))

for i in range (num1,num2 +1):
    numero_par(i)

