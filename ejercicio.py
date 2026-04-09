carreras = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas = [
    ("Juan", "Pérez", 38, 0),
    ("Carlos", "Santana", 29, 1),
    ("Raúl", "Sosa", 19, 2)
]   

estudiantes = []


for _ in range(5):
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = int(input("Ingresa tu edad: "))
    carrera = int(input("Ingresa tu carrera: "))
    persona = (nombre, apellido, edad, carrera)
    personas.append(persona)
    numero_carrera = persona[3]
    nombre_carrera = carreras[numero_carrera]
    print("")

for persona in personas:
    nombre = persona[0]
    apellido = persona[1]
    edad = persona[2]
    numero_carrera = persona[3]

    nombre_carrera = carreras[numero_carrera]

    estudiante = {
  "nombre": nombre,
  "apellido": apellido,
  "edad": edad,
  "carrera": nombre_carrera
 
}
    estudiantes.append(estudiante)
    print(estudiante["nombre"], estudiante["apellido"], "tiene", estudiante["edad"], 
    "años y estudia", estudiante["carrera"])
