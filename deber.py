#Declaramos nuestra lista 3D


tem_ciudad = [
    [  #Ciudad 1
    [21,12,13,14,17,25,22],
    [18,17,15,27,21,24,25],
    [15,19,18,21,22,26,27],
    [17,17,29,29,27,29,18]
],
    [ #Ciudad 2
    [22,21,17,18,19,23,22],
    [27,23,21,15,19,17,14 ],
    [22,23,22,27,30,22,25],
    [24,25,32,15,25,24,17]
    ],
[ #Ciudad 3
    [27,25,24,22,27,31,26],
    [21,27,23,22,17,19,17],
    [34,22,31,24,21,28,25],
    [21,24,25,36,24,25,29]
    ]
]

#Declaramos las variables
semana = 0
dia = 0

suma = 0



#Creamos los bucle for para recorrer nuestra lista de temepraturas
for ciudades in range(len(tem_ciudad)): #Recorremos toda la lista
    if ciudades == semana: #Creamos una condición para comparar si la variable semana es igual al recorrido de ciudades
        for semanas in range(len(tem_ciudad[ciudades])): # Recorremos las semanas dentro de ciudades
            if semanas == dia :#Creamos una condición para comparar si la variable dias es igual al recorrido de semanas
                 promedio = 0 #Iniciamos el promedio en 0
                 for dias in range(len(tem_ciudad[ciudades][semanas])):  #Recorremos los numeros dentro de ciudades y semanas.
                    suma+= tem_ciudad[ciudades][semanas][dias]  #Sumamos las temperaturas
                    promedio = suma / len(tem_ciudad[ciudades][semanas]) #Calculamos el promedio y dividimos para

                 print(f"El promedio de la temperatura de la ciudad {semana} de la semana {dia} es {promedio}")  #Imprimimos