# inicio.py
# Archivo principal del proyecto colaborativo en Python

from modulos.operaciones import sumar, restar, multiplicar, dividir
from modulos.cuento import imprimir_cuento

def menu():
    print("=== PROYECTO COLABORATIVO PYTHON ===")
    print("1. Operaciones matemáticas")
    print("2. Imprimir un cuento")
    print("3. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- OPERACIONES MATEMÁTICAS ---")
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Suma: {sumar(a, b)}")
        print(f"Resta: {restar(a, b)}")
        print(f"Multiplicación: {multiplicar(a, b)}")
        print(f"División: {dividir(a, b)}\n")

    elif opcion == "2":
        imprimir_cuento()

    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intente de nuevo.\n")
