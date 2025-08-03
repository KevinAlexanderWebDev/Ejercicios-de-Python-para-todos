# Modulo 4, ejercicio 16: Cajero Automático Simulado
# Objetivo: Simular un cajero donde el usuario tiene un saldo inicial y puede retirar dinero hasta que decida salir o el saldo se agote.

print(
    """Cajero Automático Personalizado: 
      -Insertar tarjeta aquí: --   --"""
)

password = input(
    """Introduce la contraseña: 
    **** """
)

PASSWORD_TRUE = "1234"

saldo_inicial = 120000

if password == PASSWORD_TRUE:

    print(f"Bienvenido a Isis VA, usted cuenta actualmente con: ${saldo_inicial}.")

    while True:

        retiro = int(input("¿Cuánto dinero desea retirar?: "))

        if retiro > saldo_inicial:

            print(f"Error: No cuentas con dinero suficiente: {saldo_inicial}")
            continue

        seguir = input(
            f"Vas a retirar: ${retiro}. ¿Desea confirmar la transacción?: (s/n). "
        )

        if seguir != "s":
            continue
        saldo_inicial -= retiro
        print(f"Dinero disponible: ${saldo_inicial}")

        finalizar = input(
            "Desea continuar retirando?: ('f' para finalizar | 'c' para continuar)"
        )

        if finalizar == "t":
            print(
                f"""Comprobante: 
                Usted ha retirado: ${retiro}
                Le restan: ${saldo_inicial}"""
            )
            print("Operación finalizada. Que tenga buen día.")
            break
        elif finalizar != "c":
            print("Entrada inválida. Por favor, ingresa 'c' o 'f'.")
else:
    print("Contraseña Incorrecta. Prueba Otra Vez.")
