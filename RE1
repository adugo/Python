import re
#Diseña una función en python que reciba como parámetro una cadena de texto y devuelva True si es
#un correo electrónico y False si no lo es. No es necesario que diseñes el patrón, puedes encontrarlo
#facilmente en internet.
#Escribe un programa python que use dicha función.
def verificar_correo():
    correo=input('Correo Electronico : ')
    patron='^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}$'
    flag=re.I
    coincidencias=re.findall(patron,correo,flag)
    if (coincidencias):
        return True
    else:
        return False

def ver_fecha():

    patron= '^[0-3][0-9]-[0,1][0-9]-[0-9]{4,}$'
    fecha=input("Introduce texto: ")
    flag=re.I
    coincidencia=re.findall(patron,fecha,flag)
    return coincidencia

def main():
    comprobarcorreo=verificar_correo()
    if (comprobarcorreo):
        print ("El correo es valido")
    else:
        print ("El correo no es valido")
    comprobarfechas = ver_fecha()
    print (comprobarfechas)

if __name__ == "__main__":
    main()
