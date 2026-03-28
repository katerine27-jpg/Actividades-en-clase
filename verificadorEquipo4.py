

equipo = "Equipo 4"
integrantes = ["Katerine Castro", "Omar Poot", "Angel Mota"]


print(f"Equipo: {equipo}")

print(f"Integrantes: {', '.join(integrantes)}\n")


#lista de contraseñas 
contraseñas = ["kateine", "katerine123", "katerine123!", 
               "kat", "omarcini"]

for i, c in enumerate(contraseñas, start=1):
    print(f"{i}. {c}")

#verificar cada contraseña parte 3
def verificar_contraseña(contraseña):
    if len(contraseña) < 6:
        return "débil"
    
    tiene_numero = any(char.isdigit() for char in contraseña)
    if tiene_numero:
        return "fuerte"
    else:   
         return "media"
    
#parte 4
# recorre y evalua cada contraseña en la lista
for c in contraseñas:
    resultado = verificar_contraseña(c)
    print(f"Contraseña: {c} - {resultado}")
#contadores para cada tipo de contraseña
débil = 0
media = 0
fuerte = 0

# recorre y evalua cada contraseña en la lista
for c in contraseñas:
    resultado = verificar_contraseña(c)
    print(f"Contraseña: {c} - {resultado}")
    
    
    if resultado == "débil":
        débil += 1
    elif resultado == "media":
        media += 1
    elif resultado == "fuerte":
        fuerte += 1



#imprime el conteo de cada tipo de contraseña
print("\nContador:")
print(f"Débil: {débil}")
print(f"Media: {media}")
print(f"Fuerte: {fuerte}")