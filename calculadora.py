import math

# ==========================================
# FUNCIONES PARA FIGURAS PLANAS (ÁREA Y PERÍMETRO)
# ==========================================

def datos_cuadrado():
    print("\n--- Cuadrado ---")
    lado = float(input("Ingresa el valor del lado: "))
    
    area = lado ** 2
    perimetro = 4 * lado
    
    print(f"-> El área del cuadrado es: {area:.2f}")
    print(f"-> El perímetro del cuadrado es: {perimetro:.2f}")

def datos_rectangulo():
    print("\n--- Rectángulo ---")
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    
    area = base * altura
    perimetro = 2 * (base + altura)
    
    print(f"-> El área del rectángulo es: {area:.2f}")
    print(f"-> El perímetro del rectángulo es: {perimetro:.2f}")

def datos_triangulo():
    print("\n--- Triángulo ---")
    base = float(input("Ingresa la base (para el área): "))
    altura = float(input("Ingresa la altura (para el área): "))
    
    # Para el perímetro requerimos los tres lados
    print("\nPara calcular el perímetro, ingresa los 3 lados del triángulo:")
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    
    print(f"\n-> El área del triángulo es: {area:.2f}")
    print(f"-> El perímetro del triángulo es: {perimetro:.2f}")

def datos_circulo():
    print("\n--- Círculo ---")
    radio = float(input("Ingresa el radio: "))
    
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    
    print(f"-> El área del círculo es: {area:.2f}")
    print(f"-> El perímetro del círculo (longitud) es: {perimetro:.2f}")


# ==========================================
# FUNCIONES PARA SÓLIDOS (VOLUMEN)
# ==========================================

def volumen_cubo():
    print("\n--- Volumen del Cubo ---")
    arista = float(input("Ingresa el valor de la arista (lado): "))
    volumen = arista ** 3
    print(f"El volumen del cubo es: {volumen:.2f}")

def volumen_esfera():
    print("\n--- Volumen de la Esfera ---")
    radio = float(input("Ingresa el radio: "))
    volumen = (4/3) * math.pi * (radio ** 3)
    print(f"El volumen de la esfera es: {volumen:.2f}")

def volumen_cilindro():
    print("\n--- Volumen del Cilindro ---")
    radio = float(input("Ingresa el radio de la base: "))
    altura = float(input("Ingresa la altura: "))
    volumen = math.pi * (radio ** 2) * altura
    print(f"El volumen del cilindro es: {volumen:.2f}")

def volumen_cono():
    print("\n--- Volumen del Cono ---")
    radio = float(input("Ingresa el radio de la base: "))
    altura = float(input("Ingresa la altura: "))
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    print(f"El volumen del cono es: {volumen:.2f}")


# ==========================================
# MENÚ PRINCIPAL DEL SISTEMA
# ==========================================

def menu():
    while True:
        print("\n====================================")
        print("   GEOMETRIC CALC - MENÚ PRINCIPAL  ")
        print("====================================")
        print("1. Calcular Figuras Planas (Área y Perímetro)")
        print("2. Calcular Sólidos (Volumen)")
        print("3. Salir")
        
        opcion_principal = input("Selecciona una opción (1-3): ")
        
        if opcion_principal == "1":
            print("\n--- FIGURAS PLANAS ---")
            print("1. Cuadrado\n2. Rectángulo\n3. Triángulo\n4. Círculo")
            sub_opcion = input("Selecciona la figura (1-4): ")
            
            if sub_opcion == "1": datos_cuadrado()
            elif sub_opcion == "2": datos_rectangulo()
            elif sub_opcion == "3": datos_triangulo()
            elif sub_opcion == "4": datos_circulo()
            else: print("Opción no válida.")
                
        elif opcion_principal == "2":
            print("\n--- SÓLIDOS REGULARES ---")
            print("1. Cubo\n2. Esfera\n3. Cilindro\n4. Cono")
            sub_opcion = input("Selecciona el sólido (1-4): ")
            
            if sub_opcion == "1": volumen_cubo()
            elif sub_opcion == "2": volumen_esfera()
            elif sub_opcion == "3": volumen_cilindro()
            elif sub_opcion == "4": volumen_cono()
            else: print("Opción no válida.")
                
        elif opcion_principal == "3":
            print("\n¡Gracias por usar la calculadora geométrica! Hasta pronto.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu()