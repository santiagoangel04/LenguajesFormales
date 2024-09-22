import re

patron = r"^(01|10)|([01][01][01])*$"
s
cancelar = True

while cancelar:
    print("""
        1) Seguir 
        2) Salir
    """)
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            cadena_to_verify = input("Ingrese la cadena: ")

            if re.match(patron,cadena_to_verify):
                print("ACEPTADA")
            else:
                print("rechazada".upper())
        case 2:
            cancelar = False

