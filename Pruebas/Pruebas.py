from io import open

texto=open("grupos.txt","r") # Leemos el fichero
lista=texto.readlines()
texto.close()
print(lista)

print("Hola mundo")