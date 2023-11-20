num1=int(input("ingrese el primer numero: "));
num2=int(input("Ingrese el segundo numero: "));
num3=int(input("ingrese el tercer numero: "));
sum = num3+num2+num1
promedio=sum//3
if promedio % 2 == 0:
    mensaje=promedio,("es Par");
else:
    mensaje=promedio,("es inpar");
print(mensaje)