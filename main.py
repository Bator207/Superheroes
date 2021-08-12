from config import *
from datetime import datetime

def frase(sh,co,ar,sp):
    return ('Soy {} {}, mi poder es el {} y voy a luchar contra la injusticia con mi {}!!'.format(sh,co,sp,ar))

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

def comprobarNumero(dic,frase,tipo):
    salida=False
    cadena=input(frase)
    while not salida:
        if cadena == '':
            print('ERROR!!!! No puede ser vacio')    
            cadena=input(frase) 
        if tipo=='D':
            if len(cadena)<=2 and cadena!='0':
                try:
                    numero=int(cadena)
                    salida=True
                except:
                    print('{} no es un número'.format(cadena))
                    cadena=input(frase)
            else:
                print('ERROR!!!! No puede tener mas de 2 números y no ser 0')    
                cadena=input(frase)
        if tipo=='A':
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

def comprobarFecha(d,m,a):
    actual=datetime.now()
    if a==actual.year:
        if m<=actual.month:
            if d<=actual.day:
                #fecha correcta
                print('fecha introducida {} {} {}'.format(d,m,a))
                print('fecha actual {} {} {}'.format(actual.day,actual.month,actual.year))
            else:
                print('Todavia no has nacido')
                # comprobar de nuevo dia
                print('fecha introducida {} {} {}'.format(d,m,a))
                print('fecha actual {} {} {}'.format(actual.day,actual.month,actual.year))
        else:
            print('llegaste a else mes')
            #comprobar de nuevo mes
            print('fecha introducida {} {} {}'.format(d,m,a))
            print('fecha actual {} {} {}'.format(actual.day,actual.month,actual.year))
    elif a>1900 and a<actual.year:
        # fecha correcta, comprobar nombres
        print('llegaste a elif año')
        print('fecha introducida {} {} {}'.format(d,m,a))
        print('fecha actual {} {} {}'.format(actual.day,actual.month,actual.year))
    else:
        # comprobar año
        print('llegaste a else año')
        print('fecha introducida {} {} {}'.format(d,m,a))
        print('fecha actual {} {} {}'.format(actual.day,actual.month,actual.year))


if __name__=='__main__':
    fecha=[]
    comprobarFecha(13,8,2021)
    # superheroe="{} {}".format(comprobarNombre(nombre,'Introduce tu nombre: '),comprobarNombre(apellido,'Introduce tu apellido: '))
    # f=comprobarNumero(dia,'Introduce el dia que naciste: (Formato númerico)','D')
    # fecha.append(f)
    # f=comprobarNumero(mes,'Introduce el mes que naciste: (Formato númerico)','D')
    # fecha.append(f)
    # f=comprobarNumero(any,'Introduce el año que naciste: (Formato númerico)','A')
    # fecha.append(f)
    # print(fecha)
    # print(frase(superheroe,traje,arma,superpoder))