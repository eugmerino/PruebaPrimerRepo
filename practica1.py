primerValor = input("Ingrese el primer valor: ")
segundoValor = input("Ingrese el segundo valor: ")

print("1. sumar, 2. multiplicar")
operacion = input("Operacion: ")
if(int(operacion) == 1):
    print(int(primerValor) + int(segundoValor))
elif (int(operacion) == 2):
    print(int(primerValor) * int(segundoValor))
else:
    print("Error manco.")
    #comentario para git