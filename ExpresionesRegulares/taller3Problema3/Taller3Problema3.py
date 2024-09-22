import re
cadena = input().strip()

patron = r"^[ab]([ab][ab])*$"

if re.fullmatch(patron,cadena):
    print("ACEPTA")
else:
    print("RECHAZA")