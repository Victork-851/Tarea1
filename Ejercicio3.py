num1=int(input("ingrese el primer numero: "));
num2=int(input("Ingrese el segundo numero: "));
num3=int(input("ingrese el tercer numero: "));
total = num1 +num2 + num3;
if total % 7 == 0:
    mensj=total,("es multiplo de 7: ");
else:
    mensj=total,("no es multiplo de 7: ");
print(mensj);