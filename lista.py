print("Ingrese su nombre")
name= str(input(""))
print("Ingrese su sexo biologico (F o M)")
gender=str(input(""))

if gender=="F":
    if name.lower()<"m":
        input("Su grupo es A")
    else:
        input("Su grupo es B")
else:
    if name.lower()<"n":
        input("Su grupo es A")
    else:
        input("Su grupo es B") 