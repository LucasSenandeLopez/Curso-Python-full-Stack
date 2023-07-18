import numpy as np 
"""Para trabajar con matrices (ndarrays de 2 dimensiones)
usar NumPy es la forma más sencilla"""
try:
    n = int(input("Introduzca un número entero positivo: ")) 
    """De esta manera podemos introducir el número desde la terminal. 
    Al hacerlo mediante la combinación de try-except y la función int(),
    se detecta si lo inroducido es un número entero. Si lo es, el programa 
    funciona sin saltar la excepción pero de introducir cualquier otro tipo de dato
    saltará la exepción
    """ 
    gnrtdmat = np.random.randint(0,10,(n,n))
    """Creamos la matriz con la función randint del módulo random de NumPy, en
    ella introducimos como argumentos los naturales con los que se va a rellenar; ç
    el valor inicial y final (no contado) y el tamaño del ndarray a generarse"""    
    rowsum = list(np.sum(gnrtdmat,axis=1))
    colsum = list(np.sum(gnrtdmat,axis=0))
    """La función sum de numpy te permite sumar todos los valores de un array
    con o sin respecto a un eje, en este caso seleccionamos como eje el 1 (columnas)
    y 0 (filas) respectivamente para que se obtenga el resultado de sumar toda la
    fla y toda la columna respectivamente"""
    print("La matriz es:")
    print(gnrtdmat)
    print(f"La suma de las filas en una lista es: {rowsum}")
    print(f"La suma de las columnas en una lista es: {colsum}")    
except ValueError:
    print("El número debe ser un entero positivo")




