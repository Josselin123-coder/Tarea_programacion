#Creamos el diccionario en donde vamos a colocar cable - valor
informacion= {"Nombre":"Josselin", "Edad":25,"Ciudad": "Puyo","Email":"josselin@gmail.com","Profesión": "Arquitecta"}

print("\nDICCIONARIO ACTUAL\n", informacion) #Imprimimos el diccionario actual

#Creamos un menú de opciones

print("\n\nMENÚ")
print("1.Acceder al valor asociado con la clave ciudad y modifícar con una ciudad diferente",
          "\n2. Agregar una nueva clave-valor al diccionario que represente la profesion de la persona.",
          "\n3. Verifica si la clave telefono existe en el diccionario",
          "\n4. Elimina la clave edad del diccionario",
          "\n5. Mostrar diccionario" )


opcion_user=int(input("\nIngrese la opcion: "))  #Pedimos que ingrese la opcion
while opcion_user :  #Creamos un bucle while para que el usuario siga ingresando las opciones


    if opcion_user == 1 :
        print(f"Ciudad actual: {informacion["Ciudad"]}")  #Imprimimos la ciudad actual
        informacion.update({"Ciudad": "Quito"})  #Modificamos la ciudad
        print(f"Ciudad modificada: {informacion["Ciudad"]}")  #Imprimimos






    elif opcion_user == 2:
       informacion.update({"Profesión": "Ingeniero en TICS"})  #Actualizamos la profesion
       print(f"Profesión modificada: {informacion["Profesión"]}") #Imprimimos la profesión que elegimos


    elif opcion_user ==3 :
    #Verificamos si existe telefono dentro del diccionario
        if "Telefono" in informacion:
            print("Si existe el telefono")
            print(f"Telefono: {informacion["Telefono"]}")

        else:  #Sino existe se agrega el telefono
            print("Telefono añadido")
            informacion.update({"Telefono": 984025756})
        print(f"Telefono : {informacion["Telefono"]}")  #Inprimimos


    elif opcion_user == 4:
        del informacion["Edad"]  #Eliminamos edad
        print(f"{"Edad"} eliminada")

    elif opcion_user == 5 :

        print(f"\nDICCIONARIO ACTUALIZADO es: \n {informacion}")  #Imprimimos el diccionario actualizado


    elif opcion_user > 5:
        print("Saliendo...")
        opcion_user = False  #Si la opcion es mayor a 5 la opcion es un valor falso y se corta la ejecucion
        break



    print("\n MENU DE OPCIONES",
          "\n1.Acceder al valor asociado con la clave ciudad y modifícar con una ciudad diferente",
          "\n2. Agregar una nueva clave-valor al diccionario que represente la profesion de la persona.",
          "\n3. Verifica si la clave telefono existe en el diccionario",
          "\n4. Elimina la clave edad del diccionario",
          "\n5. Mostrar diccionario")


    opcion_user = int(input("\nIngrese la opcion: "))

