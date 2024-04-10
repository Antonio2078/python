traductor = {"amor":"love","abrazo":"hug","balon":"ball","auto":"car","avion":"plane"}
palabra = ''
while palabra != "0":
    palabra = input("Ingrese la palabra a tarducir: ")
    if palabra in traductor:
        print(f"(esp) {palabra} : (eng) {traductor[palabra]}")
    elif(palabra != "0"):
        print("No se encuentra la palabra. Desea agregarla al diccionario?")
        resp = input(" S / N ")
        if resp == "S" or resp == "s":
            traductor[palabra] = input(f"Ingrese la tarduccion de: {palabra}: ")
            print("Se agrego correctamente al diccionario")

    elif( resp == 0):
        print("Cerrando diccionario")
