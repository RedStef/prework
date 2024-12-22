x = "12a34b56c78"

"""
# vytisknout kazde druhe cislo
print(x[::2])
# vytisknout kazde treti cislo
print(x[::3])
# vytisknout list pozpatku
print(x[::-1])

#vypise jednotlive znaky
jen_cisla2 = [char for char in x]
print(jen_cisla2)

# vyhazet pismena pomoci replace

# jen_cisla1 = x.replace("a", "").replace("b", "").replace("c", "")
#print(jen_cisla)
"""

jen_cisla = "+".join([char for char in x if char.isdigit()])
print(jen_cisla)

jen_cisla = "+".join([char for char in x if char.isinstance(x,str)])