respuesta="s"

#FUNCION QUE SUMA DOS VALORES
def sumar(valor1=0,valor2=0):
	return valor1 + valor2 
#FUNCION QUE SUMA DOS VALORES

#FUNCION QUE RESTA DOS VALORES
def restar(valor1=0,valor2=0):
	return valor1 - valor2 
#FUNCION QUE RESTA DOS VALORES

#FUNCION QUE MULTIPLICACION DOS VALORES
def multiplicar(valor1=0,valor2=0):
	return valor1 * valor2 
#FUNCION QUE DIVIDE DOS VALORES

#FUNCION QUE DIVIDE DOS VALORES
def dividir(valor1=0,valor2=0):
	return valor1 / valor2 
#FUNCION QUE DIVIDE DOS VALORES

def menu():
	#MENU DE OPCIONES
	print("** ::::::::::::::::::::::::: **")
	print(":: Seleccione una operanción ::")
	print("** ::::::::::::::::::::::::: **")
	print("-------------------------------")
	print("| Suma:             ->  1     |")
	print("| Resta:            ->  2     |")
	print("| Multiplicación:   ->  3     |")
	print("| División:         ->  4     |") 
	print("| Salir:            ->  5     |")
	print("-------------------------------")
	print("** ::::::::::::::::::::::::: **") 
	print("\n")
	#MENU DE OPCIONES
while respuesta!="n":
    menu()
    opcion = int(input("Selecione una Opción... "))
    if opcion>0 and opcion<6:
        if opcion == 5:
            print ("HASTA LUEGO!")
            exit()
        primer_numero=int(input("Ingrese su primer valor: "))
        segundo_numero=int(input("Ingrese su segundo valor: "))
        if opcion == 1:
            suma=sumar(primer_numero, segundo_numero)
            print ("SUMA: ", suma)
        elif opcion == 2:
            resta=restar(primer_numero, segundo_numero)
            print ("RESTA: ", resta)
        elif opcion == 3:
            multiplicacion=primer_numero*segundo_numero
            print ("MULTIPLICACIÓN: ", multiplicacion)
        elif opcion == 4:
            if segundo_numero==0:
                print ("ERROR")
            else:
                division = primer_numero/segundo_numero
            print ("DIVISIÓN", division)
    respuesta=input("Desea hacer otra operacion? [s/n]: ")
if respuesta == "n":
    print ("HASTA LUEGO!") 
    exit()