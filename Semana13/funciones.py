tem_ciudades = [
    [  #Ciudad 1
    [25,26,13,24,11,12,12],
    [20,15,10,17,11,14,15],
    [25,29,28,11,12,26,17],
    [19,16,19,9,27,29,18]
],
    [ #Ciudad 2
    [22,21,17,8,19,23,22],
    [27,23,23,25,29,27,17 ],
    [24,26,12,27,10,12,15],
    [21,15,12,25,25,24,17]
    ],
[ #Ciudad 3
    [17,15,14,27,17,11,29],
    [26,17,13,28,27,29,27],
    [30,11,12,14,26,27,25],
    [18,23,31,26,26,15,19]
    ]
]

#Creamos nuestra fucnión la cual ponemos  como parametro temperatura, ciudad y semana
def calcular_prom (temperatura,ciudad,semana):



    #Creamos un  for en el cual vamos a recorrer la ciudad y la semana
    suma = 0 # Declaramos nuestra variable y la inicializamos en 0
    for temp in range (len(temperatura[ciudad][semana])):
        suma+= temperatura[ciudad][semana][temp]   #Sumamos nuestra lista con la ciudad y semana que se vaya escojer

    promedio = suma / len(temperatura[ciudad][semana]) # Dividimos  nuestra suma para la longitud de la semana que escojimos en este caso para 7

    return f"La ciudad {ciudad} en su semana {semana} tiene un promedio de {promedio: .2f} °C" # Retornamos el promedio

#Imprimimos nuestra
print("\nTEMPERATURAS ")
for i in tem_ciudades :  #Mostramos nuestra lista de temperaturas
    print(i)

print("")
#Llamamos a nuestra funcion
mostrar = (calcular_prom(tem_ciudades,1,1))
print(mostrar)  #Mostramos en pantalla


