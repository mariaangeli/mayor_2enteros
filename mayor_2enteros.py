# programa para verificar cual de 2 números enteros es el mayor 

print("------------------------------------------")
print("------------MAYOR 2 ENTEROS---------------")
print("------------------------------------------")



# input 
x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))

# processing 
if x == y:
    print("los numeros son iguales...")

else:
    if x > y:
        mayor = x
    else:
        mayor = y
        #ouput
    print ("El mayor entre " + str(x) + " y " + str(y) + " es: " + str(mayor))

         
         

