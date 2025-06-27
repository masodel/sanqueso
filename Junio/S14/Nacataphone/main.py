# archivo: main.py
import sistema_recargas as sr
exito, usuario, clave = sr.inicio()

if exito:

    saldo = int(input("\n¿Cuántos córdobas tiene en su cuenta?: C$"))
    while True:
        opcion = sr.menu_principal()

        if opcion == 1:
            saldo = sr.submenu_nacatapacks(saldo, usuario, clave)
        elif opcion == 2:
            saldo = sr.submenu_internet(saldo, usuario, clave)
        elif opcion == 3:
            saldo = sr.submenu_min_sms(saldo, usuario, clave)
        elif opcion == 4:
            saldo = sr.submenu_larga_distancia(saldo, usuario, clave)
        elif opcion == 5:
            print("\nGracias por usar Nacataphone. ¡Hasta pronto!\n")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

        sr.volver_menu()