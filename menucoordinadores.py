from datos import cargar_datos, guardar_datos

ruta_trainers = "ruta_trainer.json"
ruta_aprobados = "aprobados.json"
ruta_inscritos = "a_inscritos.json"

def presentar_coordinadores():
    with open("presentacion_coordinadores.txt", "r") as portada:
        print(portada.read())

def coordinador(datos_inscritos, datos_aprobados):
    presentar_coordinadores()
    try:
        eleccion_opci = int(input("¿Qué deseas hacer el día de hoy? "))
        if eleccion_opci == 1:
            doc = input("Digite el documento del estudiante: ")
            if doc in datos_inscritos:
                estudiante = datos_inscritos[doc]
                if estudiante["resultado pruebas"] >= 60: 
                    datos_aprobados["aprobados"][doc] = estudiante
                    with open("p_aprobo.txt", "r") as aprobo:
                        print(aprobo.read())
                    print("¡Disfruta tu experiencia en Campus-Lands!")
                    print("Los datos han sido guardados en:", ruta_aprobados)
                else: 
                    print("Lo siento, no has aprobado.")
            else: 
                print("Usted no está inscrito en Campus-Lands.")
                
        elif eleccion_opci == 2:
            doc = input("Digite el documento del estudiante: ")
            if doc in datos_aprobados["aprobados"]: 
                datos_aprobados["aprobados"][doc]["Estado"] = "aprobado"
                print("El estado del estudiante ha sido actualizado.")
            else:
                print("El estudiante no está en la lista de aprobados.")
                
        elif eleccion_opci == 5:
            for id_tr, name_tr in datos_trainers["trainers"].items():
                print(f"Id: {id_tr}, Nombre: {name_tr}")
                
        elif eleccion_opci == 6:
            print("¡Hola!")
            
        else:
            print("Opción no válida.")
            
    except ValueError:
        print("Por favor, ingrese un número válido.")

datos_trainers = cargar_datos(ruta_trainers)
datos_aprobados = cargar_datos(ruta_aprobados)
datos_inscritos = cargar_datos(ruta_inscritos)

coordinador(datos_inscritos, datos_aprobados)

guardar_datos(datos_trainers, ruta_trainers)
guardar_datos(datos_aprobados, ruta_aprobados)
guardar_datos(datos_inscritos, ruta_inscritos)
        
    


























