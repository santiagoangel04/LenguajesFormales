count_a,count_b,count_c = 0,0,0

cadena_verificar = input()
for character in cadena_verificar:
    """
    if character is 'a':
        count_a
    por fin en python esta el swithc case
    se puede hacer asi con el if pero no es mas comodo con match
    """
    match character:
        case 'a':
            count_a +=1
        case 'b':
            count_b +=1
        case 'c':
            count_c +=1

total_contenido = count_a+count_b+count_c
print("ACEPTA" if total_contenido%2 == 0 else"RECHAZA")