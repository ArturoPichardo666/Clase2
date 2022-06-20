n=True
suma=0
while n:
    print("Escribe un numero")
    n=int(input())
    suma = suma + n
    print("La suma es", suma)
    
    if suma >=1000:
        n=False