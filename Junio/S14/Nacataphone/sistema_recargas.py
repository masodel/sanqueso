# archivo: sistema_recargas.py
import os

def guardar_registro(texto):
    with open("registro_recargas.txt", "a") as file:
        file.write(texto + "\n")

def cargar_usuarios():
    usuarios = {}
    if os.path.exists("Nusuarios.txt"):
        with open("Nusuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(",")
                usuarios[usuario] = clave
    return usuarios

def inicio_sesion():
    cont = 1
    while cont < 4:
        print("\n---- INICIO DE SESIÓN ----")
        usuarios = cargar_usuarios()
        usuario = input("Número de teléfono: ")
        clave_ingresada = input("Nombre (clave): ")
        if usuarios.get(usuario) == clave_ingresada:
            print("\nAcceso permitido")
            return True, usuario, clave_ingresada
        else:
            print(f"\nUsuario o clave incorrecta. Tiene {3-cont} intentos.\n")
            cont += 1
    print("\nAcceso denegado. Se excedieron los intentos.\nSaliendo del programa...\n")
    return False, None, None

def registrar():
    while True:
        print("\n---- REGISTRO DE USUARIO ----")
        usuarios = cargar_usuarios()
        while True:
            try:
                usuario = int(input("Numero de telefono: "))
                if len(str(usuario)) != 8:
                    print("\nEl numero de telefono debe tener 8 digitos.\n")
                    continue
                if str(usuario) in usuarios:
                    print("\nEl usuario ya existe. Por favor, elija otro.\n")
                    continue
                else:
                    break
            except ValueError:
                print("Ingrese un número.")
                continue
        clave = input("Nombre (clave): ")
        with open("Nusuarios.txt", "a") as i:
            i.write(f"{usuario},{clave}\n")
            print("\nUsuario registrado con exito.\n")
            break

def inicio():
    while True:
        print("\n---- BIENVENIDO ----")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")
        try:
            opcion=int(input("Ingrese una de las opciones: "))
            if opcion == 1:
                exito, usuario, clave = inicio_sesion()
                if exito:
                    intento=1
                    break
                else:
                    intento=0
                    break
            elif opcion == 2:
                registrar()
                exito, usuario, clave = inicio_sesion()
                if exito:
                    intento=1
                    break
                else:
                    intento=0
                    break
            elif opcion == 3:
                print("\nSaliendo del programa.\n")
                intento=0
                break
        except ValueError:
            print("Opción inválida, ingrese un número.")
            continue
    if intento == 1:
        return True, usuario, clave
    else:
        return False, None, None
        
def menu_principal():
    print("\n---- MENU PRINCIPAL ----\n")
    print("Sistema de recargas Nacataphone")
    print("1. Nacatapacks")
    print("2. Internet")
    print("3. Minutos y SMS ilimitados")
    print("4. Larga Distancia")
    print("5. Salir")
    try:
        return int(input("Ingrese una de las opciones: "))
    except:
        return 0

def submenu_nacatapacks(saldo, usuario, clave):
    print("\nNacatapacks")
    print("1. Nacata4")
    print("2. Nacata3")
    print("3. Nacata2")
    print("4. Nacata1")
    print("5. Volver")
    try:
        op1 = int(input("Ingrese que Nacatapack desea: "))
    except:
        op1 = 0

    if op1 == 5:
        return saldo
    if op1 < 1 or op1 > 5:
        print("Opción inválida, intente más tarde")
        return saldo

    packs = {
        1: ("2000mb + 180min + RRSS GRATIS x 8 días", 100),
        2: ("1000mb + 180min + RRSS GRATIS x 6 días", 70),
        3: ("500mb + 60min + RRSS GRATIS x 4 días", 40),
        4: ("200mb + 30min + RRSS GRATIS x 2 días", 20)
    }
    descripcion, costo = packs[op1]
    print(descripcion)
    print("1. Activar")
    print("2. Volver")
    try:
        op1_1 = int(input("Ingrese una de las opciones: "))
    except:
        op1_1 = 0

    if op1_1 == 1:
        if saldo >= costo:
            saldo -= costo
            print(f"Su Nacata{op1} ha sido activado. Saldo restante: C${saldo}")
            guardar_registro(f"Nacata{op1} activado por C${costo} - {usuario}, {clave}\n")
        else:
            print("Saldo insuficiente para activar este paquete.")
    elif op1_1 == 2:
        print("Operación cancelada, volviendo al menú principal.")
    else:
        print("Opción inválida, intente más tarde")

    return saldo

def submenu_internet(saldo, usuario, clave):
    print("\nInternet")
    print("1. Nav3")
    print("2. Nav2")
    print("3. Nav1")
    print("4. Volver")
    try:
        op2 = int(input("Ingrese que Nav desea: "))
    except:
        op2 = 0

    if op2 == 4:
        return saldo
    if op2 < 1 or op2 > 4:
        print("Opción inválida, intente más tarde")
        return saldo

    packs = {
        1: ("Whatsapp + Musica ILIMITADA x 15D", 90),
        2: ("Whatsapp + Musica ILIMITADA x 10D", 60),
        3: ("Whatsapp + Musica ILIMITADA x 5D", 30)
    }
    descripcion, costo = packs[op2]
    print(descripcion)
    print("1. Activar")
    print("2. Volver")
    try:
        op2_1 = int(input("Ingrese una de las opciones: "))
    except:
        op2_1 = 0

    if op2_1 == 1:
        if saldo >= costo:
            saldo -= costo
            print(f"Su Nav{op2} ha sido activado. Saldo restante: C${saldo}")
            guardar_registro(f"Nav{op2} activado por C${costo} - {usuario}, {clave}\n")
        else:
            print("Saldo insuficiente para activar este paquete.")
    elif op2_1 == 2:
        print("Operación cancelada, volviendo al menú principal.")
    else:
        print("Opción inválida, intente más tarde")

    return saldo

def submenu_min_sms(saldo, usuario, clave):
    print("\nMin y SMS ILIMITADOS")
    print("1. Habla3")
    print("2. Habla2")
    print("3. Habla1")
    print("4. Volver")
    try:
        op3 = int(input("Ingrese que Habla desea: "))
    except:
        op3 = 0

    if op3 == 4:
        return saldo
    if op3 < 1 or op3 > 4:
        print("Opción inválida, intente más tarde")
        return saldo

    packs = {
        1: ("Min+SMS ILIMITADOS + Whatsapp x 15D", 80),
        2: ("Min+SMS ILIMITADOS + Whatsapp x 10D", 50),
        3: ("Min+SMS ILIMITADOS + Whatsapp x 5D", 25)
    }
    descripcion, costo = packs[op3]
    print(descripcion)
    print("1. Activar")
    print("2. Volver")
    try:
        op3_1 = int(input("Ingrese una de las opciones: "))
    except:
        op3_1 = 0

    if op3_1 == 1:
        if saldo >= costo:
            saldo -= costo
            print(f"Su Habla{op3} ha sido activado. Saldo restante: C${saldo}")
            guardar_registro(f"Habla{op3} activado por C${costo} - {usuario}, {clave}\n")
        else:
            print("Saldo insuficiente para activar este paquete.")
    elif op3_1 == 2:
        print("Operación cancelada, volviendo al menú principal.")
    else:
        print("Opción inválida, intente más tarde")

    return saldo

def submenu_larga_distancia(saldo, usuario, clave):
    print("\nLarga Distancia")
    print("1. 30 Min Usa")
    print("2. 20 Min CostaRica")
    print("3. Volver")
    try:
        op4 = int(input("Ingrese que opcion desea: "))
    except:
        op4 = 0

    if op4 == 3:
        return saldo
    if op4 < 1 or op4 > 3:
        print("Opción inválida, intente más tarde")
        return saldo

    packs = {
        1: ("30 Min a USA y Canada x 2 dias", 35),
        2: ("20 Min a Costa Rica 2 dias", 25)
    }
    descripcion, costo = packs[op4]
    print(descripcion)
    print("1. Activar")
    print("2. Volver")
    try:
        op4_1 = int(input("Ingrese una de las opciones: "))
    except:
        op4_1 = 0

    if op4_1 == 1:
        if saldo >= costo:
            saldo -= costo
            nombre_pack = "30 Min Usa" if op4 == 1 else "20 Min Costa Rica"
            print(f"Su {nombre_pack} ha sido activado. Saldo restante: C${saldo}")
            guardar_registro(f"{nombre_pack} activado por C${costo} - {usuario}, {clave}\n")
        else:
            print("Saldo insuficiente para activar este paquete.")
    elif op4_1 == 2:
        print("Operación cancelada, volviendo al menú principal.")
    else:
        print("Opción inválida, intente más tarde")

    return saldo

def volver_menu():
    # Función vacía para mantener estructura, ya no pide enter
    pass