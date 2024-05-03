import pandas as pd

#Lista de calificaciones dada
calificaciones = [
    {"nombre": "Juan", "matematicas": 85, "ciencias": 90, "historia": 75},
    {"nombre": "Maria", "matematicas": 70, "ciencias": 80, "historia": 85},
    {"nombre": "Pedro", "matematicas": 95, "ciencias": 75, "historia": 90},
    {"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia": 80},
    {"nombre": "Luis", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Sofia", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Carlos", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Elena", "matematicas": 70, "ciencias": 75, "historia": 85},
    {"nombre": "Javier", "matematicas": 80, "ciencias": 85, "historia": 90},
    {"nombre": "Laura", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Diego", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Paula", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Carmen", "matematicas": 70, "ciencias": 75, "historia": 85}
    
    
]
#Se convierte la lista en un DataFrame
df = pd.DataFrame(calificaciones)
#Se oculta la comlumna nombre
df_calif = df.drop(columns=['nombre'])
#Calcular el promedio de calificaciones para las asignaturas
promedio = df_calif.mean()
#Estudiantes con las calificaciones más altas en las asignaturas
calif = df.max()
#Crea un DataFrame con el nombre del estudiante y el promedio de las notas
calif_max = df[df == calif].dropna(axis=0, how='all')
frec_calif = df.melt(var_name='Asignatura', value_name='Calificacion')

print("Promedio de calif por asignatura: ")
print(promedio)
print()


print("Estudiantes con las calificaciones mas altas: ")
print(calif_max)
print()

#Calcula el porcentaje de estudiantes que aprobaron cada asignatura
ap_asignatura = df.apply(lambda col: (col >= 60).sum() / len(col) * 100)

print("Porcentaje de estudiantes que aprobaron las asignaturas : ")
print(ap_asignatura)
print()

frec_calif = frec_calif.groupby(['Asignatura', 'Calificacion']).size().reset_index(name='Frecuencia')

print("DataFrame con la frecuencia de cada calificacion:")
print(frec_calif)
