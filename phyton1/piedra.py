import random 
user=input("Elige: piedra, papel o tijera:\n")
aleatorio= random.randint(1,3)
if aleatorio ==1:
    machine = "piedra"
elif aleatorio == 2:
        machine = "papel"
else:
    aleatorio:"tijera"

print (f"El usuario eligio {user} y la maquina eligio {machine} ")
if machine=='piedra' and 'tijera':
    print("gana el usuario")
elif machine=='piedra' and 'papel':
        print ("Gana la maquina")
elif machine=='piedra' and 'piedra':
        print ("Empateee!")
elif machine=='papel' and 'piedra':
        print ("Gana la maquina")
elif machine=='papel' and 'tijera':
        print ("Gana la maquina")
elif machine=='papel' and 'papel':
        print ("Empateee!")
elif machine=='tijera' and 'piedra':
        print ("Gana la maquina")
elif machine=='tijera' and 'papel':
        print ("Gana el usuario")
elif machine=='papel' and 'papel':
        print ("Empatee!")






