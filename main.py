from config import *
from datetime import datetime
from presentacion import *

# Función que te devuelve la frase del superheroe
def frase(sh,co,ar,sp):
    return ('Soy {} {}, mi poder es el {} y voy a luchar contra la injusticia con mi {}!!'.format(sh,co,sp,ar))

# Funcion para sacar la primera y comprobar que sea correcta
def comprobarNombre(dic,frase):
    salida=False
    while not salida:
        cadena=Input(frase,line=1,column=5)
        if cadena == '':
            Print('ERROR!!!! No puede ser vacio',line=25,column=1,style='bold',color='yellow', back='red')
            continue
            # cadena=Input(frase,line=1,column=5)
        # clearLine(25)
        letra=cadena[0].upper()
        if letra in dic:
            salida=True
            clearLine(25)
        else:
            Print('{} no es una letra'.format(cadena[0]),line=25,column=1,style='bold',color='yellow', back='red')
            # cadena=Input(frase,line=1,column=5)
    return dic[letra]

# Funcion donde se pide la fecha de nacimiento
def pedirFecha():
    fecha=[]
    tipo=('año','mes','dia')
    actual=datetime.now()

    for i in tipo:
        nacimiento=False
        frase='Introduce el {} que naciste: (Formato númerico) '.format(i)
        while not nacimiento:
            cadena=Input(frase,line=1,column=5)
            clearLine(25)
            try:
                numero=int(cadena)
            except:
                Print('{} no es un número'.format(cadena),line=25,column=1,style='bold',color='yellow', back='red')
                continue
            if i == 'año':
                if len(cadena)==4 and cadena!='0':
                    if numero>=1920 and numero<=actual.year:
                        fecha.append(numero)
                        nacimiento=True
                    else:
                        Print("ERROR!!!! Año incorrecto",line=25,column=1,style='bold',color='yellow', back='red')
                        continue
                else:
                    Print('ERROR!!!! No puede ser 0 o tener una longuitud diferente de 4 digitos',line=25,column=1,style='bold',color='yellow', back='red')
                    continue
            elif i == 'mes':
                if len(cadena)<=2 and cadena!='0':
                    if numero in mes:
                        if fecha[0]==actual.year:
                            if numero<=actual.month:
                                fecha.append(numero)
                                nacimiento=True
                            else:
                                Print('ERROR!!!! Mes incorrecto',line=25,column=1,style='bold',color='yellow', back='red')
                                continue
                        else:
                            fecha.append(numero)
                            nacimiento=True
                    else:
                        Print('ERROR!!!! Mes incorrecto',line=25,column=1,style='bold',color='yellow', back='red')
                        continue
                else:
                    Print('ERROR!!!! No puede ser 0 o tener una longuitud mayor de 2 a digitos',line=25,column=1,style='bold',color='yellow', back='red')
                    continue
            else:
                #Falta comprobar que esta en el rango
                if len(cadena)<=2 and cadena!='0':
                    if numero in dia:
                        if fecha[1]==actual.month:
                            if numero<=actual.day:
                                fecha.append(numero)
                                nacimiento=True
                            else:
                                Print('ERROR!!!! Dia incorrecto',line=25,column=1,style='bold',color='yellow', back='red')
                                continue
                        else:
                            fecha.append(numero)
                            nacimiento=True
                    else:
                        Print('ERROR!!!! Dia incorrecto',line=25,column=1,style='bold',color='yellow', back='red')
                        continue
                else:
                    Print('ERROR!!!! No puede ser 0 o tener una longuitud mayor de 2 a digitos',line=25,column=1,style='bold',color='yellow', back='red')
                    continue
    return fecha

def ultimoNumero(strNumero):
    strNumero=str(strNumero)
    return int(strNumero[-1])

def armaTrajeSuperpoder(fecha):
    sh=[]
    sh.append(dia[fecha[2]])
    sh.append(mes[fecha[1]])
    un=ultimoNumero(fecha[0])
    sh.append(any[un])
    return sh

if __name__=='__main__':
    limpiar()
    superheroe="{} {}".format(comprobarNombre(nombre,'Introduce tu nombre: '),comprobarNombre(apellido,'Introduce tu apellido: '))
    f=pedirFecha()
    sh=armaTrajeSuperpoder(f)
    Print(frase(superheroe,sh[2],sh[0],sh[1]),line=5,column=5)