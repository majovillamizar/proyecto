from datos import *
presentacion_camper=open("presentacion_campers.txt", "r")
aseguradora=(presentacion_camper.read())
print(aseguradora)

ruta_inscritos = "a_inscritos.json"
datos_inscritos= cargar_datos(ruta_inscritos)

ruta_notas="notas.json"
datos_notas=cargar_datos(ruta_notas)

eleccion = int(input("Ingrese el numero de la accion que desea ejecutar"))
if eleccion == 1:
    inscri_boni=open("p_inscripccion.txt","r")
    real=inscri_boni.read()
    print(real)
    
    doc = input("ponga tarjeta de identidad: ")
    camper = {} 
        
    camper["nombre"] =input("ponga nombre: ")
    camper["apellido"] =input("ponga apellido: ")
    camper["telefono"] = input("ponga telefono: ")
    camper["direccion"] = input("ponga direccion: ")
    camper["acudiente"] = input("ponga su acudiente: ")
    camper["estado"] = "Inscrito"
        
    horario=open("p_horario_pruebas.txt", "r")
    ahora=(horario.read())
    
    print(ahora)
    
    camper["horario"]= input("Elija un horario disponible para realizar la prueba☛")
        
    datos_inscritos[doc] = camper
    print("Has sido registrado exitosamente")
        
elif eleccion == 2:
    ti=input("ingrese su numero de documento")
    a= datos_notas
    print (a)
else:
    ("opcion invalida")
        
guardar_datos(datos_inscritos, ruta_inscritos)
        