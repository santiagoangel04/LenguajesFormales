import re

cadena = input()
patron = r"^[012]2[012]*1[012]$|12"
verification = re.match(patron,cadena)
if verification:
    print("ACEPTA")
else:
    print("RECHAZA")