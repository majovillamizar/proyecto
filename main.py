presentacion=open("presentacion_menu.txt", "r")
asegurar=(presentacion.read())
print(asegurar)

eleccion=int(input("ingrese el numero de la opcion deseada"))

if eleccion==1:
    import menucamper
elif eleccion==2:

    print("numero ingresado no valido")

