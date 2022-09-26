#condicionales  if elif else
#Nos permiten evaluar expresiones booleanas que d e cumplirse realizenuna accion y en caso de que no entonces realizen otra.
#evaluar si una persona es mayor de edad
age = int(input('ingresa tu edad '))
genre=input("ingresa tu genero")

if age<2:
    print("eres un bebe")
elif age < 12:
   print("eres un nino")
elif age < 18:
   print("eres un joven")
elif age < 50:
   print("eres un adulto")
else:
    print("eres muy mayor")
else