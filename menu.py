from radio import radio
from sales import sales
from streaming import streaming 
from artista import artista

while True:

    print("**BIENVENIDOS AL BILLBOARD HOT 100**")
    print("1.-'Contar los puntos de una canción' 2.-'Salir del programa'")

    opcionInicial = int(input("Elija la opcion: "))
    
    if opcionInicial == 1:
        
        nombre = input("Ingrese el nombre del cantante: ")         
        a = artista(nombre)
        a.agregar()

        try:
            streamYT = int(input("Ingrese el número de stream en YouTube de la canción: "))
        except:
            print("**SOLO DEBE CONTENER NUMEROS**")
            streamYT = int(input("Ingrese el número de stream en YouTube de la canción: "))
        try:
            remix = int(input("Ingrese el número de stream de los remix(s): "))
        except:
            print("**SOLO DEBE CONTENER NUMEROS**")
            remix = int(input("Ingrese el número de stream de los remix(s): "))
        try:
            streamDePaga = int(input("Ingrese el número de stream que tuvo en plataformas de paga: "))
        except:
            print("**SOLO DEBE CONTENER NUMEROS**")
            streamDePaga = int(input("Ingrese el número de stream que tuvo en plataformas de paga: "))
        s = streaming(streamYT, remix, streamDePaga)
        s.agregar()

        try:
            radioPop = int(input("Ingrese el número de veces que se paso por la radio Pop: "))
        except:
            print("**SOLO DEBE CONTENER NUMEROS**")
            radioPop = int(input("Ingrese el número de veces que se paso por la radio Pop: "))
        try:
            radioAC = int(input("Ingrese el número de veces que se paso por la radio AC: "))
        except:
            print("**SOLO DEBE CONTENER NUMEROS**")
            RadioAC =  int(input("Ingrese el número de veces que se paso por la radio AC: "))
        r = radio(radioPop, radioAC)
        r.agregar()

        try:
            digitalSales = int(input("Ingrese el número de ventas digitales obtenidas: "))
        except:
            print("**SOLO DEBE CONTENER NUMEROS**")
            digitalSales = int(input("Ingrese el número de ventas digitales obtenidas: "))
        try:
            fisicalSales = int(input("Ingrese el número de ventas fisicas obtenidas: "))
        except:
            print("**SOLO DEBE CONTENER NUMEROS**")
            fisicalSales = int(input("Ingrese el número de ventas fisicas obtenidas: "))
        sa = sales(digitalSales, fisicalSales)
        sa.agregar()

        print ("El nombre del Artista es: ")
        a.nombreArtista()
        print ("Los puntos de streaming son: ")
        s.leerNumerosStreaming()
        print ("Los puntos de radio son: ")
        r.leerNumerosRadio()
        print ("Los puntos de ventas son: ")
        sa.leerNumerosSales()


    if opcionInicial == 2:
        break 

    


        
        

        

        


        




