valor1=int(input("Ingrese el primer número:"));
valor2=int(input("Ingrese el primer número:"));
valor3=int(input("Ingrese el primer número:"));
if valor1 > valor2 and valor1 > valor3:
    mensa = valor1;
elif valor2 > valor1 and valor2 > valor3:
    mensa = valor2;
else:
    mensa = valor3;

print("El mayor de los tres valores es:", mensa);