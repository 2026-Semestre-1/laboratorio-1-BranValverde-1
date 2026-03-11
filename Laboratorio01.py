"""
Nombre: calculadora
Entradas: operacion, op1, op2
Salidas: resultado
Restricciones: debe ser un entero
"""

def calculadora(operacion, op1, op2):

    if not isinstance(operacion, int):
        return "Error: debe de ser un numero entero"
    if not isinstance(op1, int):
        return "Error: debe de ser un numero entero"
    if not isinstance(op2, int):
        return "Error: debe de ser un numero entero"

    if (operacion <= 0) or (operacion > 4):
        return "Error: la operacion no está dentro de las establecidas"

    if (operacion == 1 ):
        resultado = op1+op2
        return resultado
    
    elif (operacion == 2):
        resultado = op1-op2
        return resultado

    elif (operacion == 3):
        resultado = op1*op2
        return resultado 

    if (operacion == 4) and (op2 == 0):
        return "Error: no es posible dividir entre 0"

    elif (operacion == 4):
        return(op1 // op2)

"""
Nombre: contadorDigitos(num, digito)
Entradas: num, digito
Salidas: numero de veces que el digito aparece en num
Restricciones: deben ser enteros
        digito debe ser menor a 10 y mayor igual a 0
"""

def contadorDigitos (num, digito):
    
    if not isinstance(num, int):
        return "Error: num debe ser entero"
    if not isinstance(digito, int):
        return "Error: digito debe ser entero"
    if (digito > 10) or (digito < 0):
        return "Error: el valor de digito no está entre los parametros"

    if num < 0:
        num= -num
        
    contador= 0

    while num > 0:
        if num % 10 == digito:
            contador += 1
        num //= 10

    return contador





"""
Nombre: sumatoriaV2
Entradas: inicio, fin, distancia, excepcion)
Salidas: sumatoria
Restricciones: Todos parámetros deben ser de tipo entero,
Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0.
Los valores de inicio y fin deben ser positivos
Si la distancia es un número negativo, el valor de fin debe ser menor a inicio
Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio
Si excepcion es igual a cero, se debe ignorar este valor, lo contrario, todo número dentro de la secuencia entre inicio y ** final** sea divisible por esta excepcion debe omitirse en la suma
"""

def sumatoriaV2 (inicio, fin, distancia, excepcion):
    
    if not isinstance(inicio, int) or inicio<0:
        return "Error: inicio debe ser entero positivo"
    if not isinstance(fin, int) or fin<0:
        return "Error: fin debe ser entero positivo"
    if not isinstance(distancia, int):
        return "Error: distancia debe ser entero"
    if not isinstance(excepcion, int):
        return "Error: excepcion debe ser entero"
    if distancia == 0 (distancia >= 10 or distancia <= -10):
        return "Error: el valor de distancia no está entre los parametros"
    if (excepcion >= 10) or (excepcion < 0):
        return "Error: el valor de excepcion no está entre los parametros"
    if (distancia<0) and fin>inicio:
        return "El valor de fin debe de ser menor a inicio"
    if (distancia>0) and fin<inicio:
        return "El valor de fin debe de ser mayor a inicio"

    return sumatoriaV2Aux (inicio, fin, distancia, excepcion)

def sumatoriaV2Aux (inicio, fin, distancia, excepcion):
    suma = 0
    while (distancia > 0 and inicio <= fin) or  (distancia < 0 and inicio >=  fin):
        if excepcion == 0 or inicio % excepcion != 0:
            suma += inicio
        inicio *= distancia

    return suma
            


    







