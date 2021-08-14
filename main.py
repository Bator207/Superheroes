from config import *
from datetime import datetime

# Función que te devuelve la frase del superheroe
def frase(sh,co,ar,sp):
    return ('Soy {} {}, mi poder es el {} y voy a luchar contra la injusticia con mi {}!!'.format(sh,co,sp,ar))

# Funcion para sacar la primera y comprobar que sea correcta
def comprobarNombre(dic,frase):
    salida=False
    cadena=input(frase)
    while not salida:
        if cadena == '':
            print('ERROR!!!! No puede ser vacio')    
            cadena=input(frase)
        letra=cadena[0].upper()
        if letra in dic:
            salida=True
        else:
            print('{} no es una letra'.format(cadena[0]))
            cadena=input(frase)
    return dic[letra]

# Funcion donde se pide la fecha de nacimiento
def pedirFecha():
    fecha=[]
    tipo=('dia','mes','año')
    for i in range (3):
        frase='Introduce el {} que naciste: (Formato númerico)'.format(tipo[i])
        cadena=__comprobarNumero(frase,tipo[i])
        fecha.append(cadena)
    return fecha

# Función para comprobar la fecha
def __comprobarNumero(frase,tipo):
    salida=False
    cadena=input(frase)
    while not salida:
        if cadena == '':
            print('ERROR!!!! No puede ser vacio')    
            cadena=input(frase) 
        if tipo=='dia' or tipo=='mes':
            if len(cadena)<=2 and cadena!='0':
                try:
                    numero=int(cadena)
                    salida=True
                except:
                    print('{} no es un número'.format(cadena))
                    cadena=input(frase)
            else:
                print('ERROR!!!! El {} no puede tener mas de 2 números y no ser 0'.format(tipo))
                cadena=input(frase)
        if tipo=='año':
            if len(cadena)==4 and cadena!='0':
                try:
                    numero=int(cadena)
                    salida=True
                except:
                    print('{} no es un número'.format(cadena))
                    cadena=input(frase)
            else:
                print('ERROR!!!! El año tiene que tener 4 números o no ser 0')    
                cadena=input(frase)
    return numero

def ultimoNumero(strNumero):
    try:
        return int(strNumero[-1])
    except:
        print('{} no es un numero'.format(strNumero))

def comprobarFecha(fecha):
    actual=datetime.now()
    if fecha[2]==actual.year:
        if fecha[1]<=actual.month:
            if fecha[0]<=actual.day:
                # Fecha correcta
                return fecha
            else:
                # Fecha incorrecta, volver a comprobar de nuevo dia
                print('Todavia no has nacido')
                fecha[0]=__comprobarNumero('Introduce el {} que naciste: (Formato númerico)'.format('dia'),'dia')
        else:
            # Fecha incorrecta, volver a comprobar de nuevo mes
            print('Todavia no has nacido')
            fecha[0]=__comprobarNumero('Introduce el {} que naciste: (Formato númerico)'.format('mes'),'mes')
    elif fecha[2]>1900 and fecha[2]<actual.year:
        # Fecha correcta
        return fecha
    else:
        # Fecha incorrecta, volver a comprobar de nuevo mes
        print('Todavia no has nacido')
        fecha[0]=__comprobarNumero('Introduce el {} que naciste: (Formato númerico)'.format('año'),'año')


if __name__=='__main__':
    fecha=[]
    # comprobarFecha(13,8,2021)
    # superheroe="{} {}".format(comprobarNombre(nombre,'Introduce tu nombre: '),comprobarNombre(apellido,'Introduce tu apellido: '))
    f=pedirFecha()
    f=comprobarFecha(f)
    # fecha.append(f)
    # f=comprobarNumero(mes,'Introduce el mes que naciste: (Formato númerico)','D')
    # fecha.append(f)
    # f=comprobarNumero(any,'Introduce el año que naciste: (Formato númerico)','A')
    # fecha.append(f)
    # print(frase(superheroe,traje,arma,superpoder))