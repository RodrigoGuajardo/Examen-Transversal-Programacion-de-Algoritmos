import datetime
print("Ingrese su nombre y apellido por favor.")
nombre=input("Nombre: ")
apellido=input("Apellido: ")
pisos = 10
departamentos_por_piso = 4
total_departamentos = pisos * departamentos_por_piso
precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}
venta_departamentos = [['-' for _ in range(departamentos_por_piso)] for _ in range(pisos)]
compradores = []
def mostrar_menu():
    print("**********MENU**********")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
def comprar_departamento():
    print("===== Comprar Departamento =====")
    piso = int(input("Ingrese el numero de piso (1-10): "))
    tipo = input("Ingrese el tipo de departamento (A, B, C, D): ")
    tipo = tipo.upper()
    
    if piso < 1 or piso > pisos or tipo not in precios:
        print("¡Error! Piso o tipo de departamento invalido.")
        return
    
    departamento = tipo + str(piso)
    if venta_departamentos[piso-1][ord(tipo)-ord('A')] != '-':
        print("Lo sentimos, el departamento", departamento, "no esta disponible.")
        return
    
    run = input(f"Ingrese el RUN del comprador (sin guiones ni puntos \nen caso de terminar en k Remplace por un 10): ")
    if not run.isdigit():
        print("¡Error! RUN invalido.")
        return
    
    venta_departamentos[piso-1][ord(tipo)-ord('A')] = 'X'
    compradores.append((run, departamento))
    print("La operación se ha realizado correctamente.")
def mostrar_departamentos_disponibles():
    print("===== Departamentos Disponibles =====")
    for piso in range(pisos):
        for tipo in precios:
            estado = venta_departamentos[piso][ord(tipo)-ord('A')]
            departamento = tipo + str(piso+1)
            print("Departamento", departamento, ":", "Disponible" if estado == '-' else "Vendido")
def ver_listado_compradores():
    print("===== Listado de Compradores =====")
    compradores_ordenados = sorted(compradores, key=lambda x: x[0])
    for comprador in compradores_ordenados:
        print("RUN:", comprador[0], "- Departamento:", comprador[1])
def mostrar_ventas_totales():
    print("===== Ventas Totales =====")
    total_ventas = sum(precios[tipo] for fila in venta_departamentos for tipo in fila if tipo == 'X')
    print("Ganancias totales:", total_ventas, "UF")
def salir():
    print("Adios!!!")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print("Fecha actual:", datetime.datetime.now().strftime("%Y-%m-%d"))
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")
        
        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_departamentos_disponibles()
        elif opcion == '3':
            ver_listado_compradores()
        elif opcion == '4':
            mostrar_ventas_totales()
        elif opcion == '5':
            salir()
            break
        else:
            print("¡Error! Opcion incorrecta, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
