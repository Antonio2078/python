usuarios_autenticados = {"admin":"123456","jose":"33126","juanita":"65473","moios":"19880"}
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if (usuario in usuarios_autenticados):
    intentos = 1
    while (intentos <= 3):
        if (usuarios_autenticados[usuario] == password):
            print("Acceso correcto")
            break
        else:
            if(intentos >= 3):
                print("Su cuenta se ha bloqueado. Intentelo nuevamente mas tarde")
                intentos += 1
            else:
                intentos += 1
                print(f"Error de contraseña. Intentos {intentos} de 3")
                password = input("Ingrese su contraseña: ")

else: 
    print("El usuario no existe")
