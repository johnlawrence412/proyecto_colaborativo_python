from matematicas import suma, resta, multiplicacion, division, potencias
from cuento import imprimir_cuento
from utilidades import en_mayusculas

def main():
    print("=== Bienvenido al Proyecto Colaborativo en Python ===")
    
    print("\nOperaciones Matemáticas:")
    print("Suma:", suma(5, 3))
    print("Resta:", resta(10, 7))
    print("Multiplicación:", multiplicacion(4, 5))
    print("División:", division(8, 2))
    print("Potencia:", potencias(2, 3))
    
    print("\nCuento:")
    imprimir_cuento()
    
    print("\nTexto en mayúsculas:")
    print(en_mayusculas("colaborar es aprender juntos"))

if __name__ == "__main__":
    main()
