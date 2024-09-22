import re
cadena_entrada = input()

#patron =
veri_cadena:bool = re.match(r"^123.*321$|^12321$",cadena_entrada)
if veri_cadena:
    print("ACEPTA")
else:
    print("RECHAZA")