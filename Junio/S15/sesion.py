import os
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
        clave_ingresada = input("Nombre: ")
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
        clave = input("Nombre: ")
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
            opcion=int(input("|\nIngrese una de las opciones: "))
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
            else:
                print("\nOpción inválida, intente de nuevo.")
                continue
        except ValueError:
            print("Opción inválida, ingrese un número.")
            continue
    if intento == 1:
        return True, usuario, clave
    else:
        return False, None, None