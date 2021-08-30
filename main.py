from config import *
from datetime import datetime
from presentacion import *

# Función que te devuelve la frase del superheroe
def frase(sh,co,ar,sp):
    return ('Soy {} {}, mi poder es el {} y voy a luchar contra la injusticia con mi {}!!'.format(sh,co,sp,ar))

# Funcion para sacar la primera y comprobar que sea correcta
def comprobarNombre(dic,frase):
    salida=False
    cadena=Input(frase,line=1,column=5)
    while not salida:
        if cadena == '':
            Print('ERROR!!!! No puede ser vacio',line=25,column=1,style='bold',color='yellow', back='red')
            cadena=Input(frase,line=1,column=5)
        clearLine(25)
        letra=cadena[0].upper()
        if letra in dic:
            salida=True
        else:
            Print('{} no es una letra'.format(cadena[0]),line=25,column=1,style='bold',color='yellow', back='red')
            cadena=Input(frase,line=1,column=5)
        clearLine(25)
    return dic[letra]

# Funcion donde se pide la fecha de nacimiento
def pedirFecha():
    fecha=[]
    tipo=('año','mes','dia')
    for i in range (3):
        frase='Introduce el {} que naciste: (Formato númerico) '.format(tipo[i])
        strNumero=Input(frase,line=1,column=5)
        cadena=__comprobarNumero(frase,tipo[i],strNumero)
        fecha.append(cadena)
    return fecha

# Función para comprobar la fecha
def __comprobarNumero(frase,tipo,cadena):
    salida=False
    while not salida:
        if cadena == '':
            Print('ERROR!!!! No puede ser vacio',line=25,column=1,style='bold',color='yellow', back='red')
            cadena=Input(frase,line=1,column=5)
        clearLine(25)
        if tipo=='dia' or tipo=='mes':
            if len(cadena)<=2 and cadena!='0':
                try:
                    numero=int(cadena)
                    salida=True
                except:
                    Print('{} no es un número'.format(cadena),line=25,column=1,style='bold',color='yellow', back='red')
                    cadena=Input(frase,line=1,column=5)
                clearLine(25)
            else:
                Print('ERROR!!!! El {} no puede tener mas de 2 números y no ser 0'.format(tipo),line=25,column=1,style='bold',color='yellow', back='red')
                cadena=Input(frase,line=1,column=5)
            clearLine(25)
        if tipo=='año':
            if len(cadena)==4 and cadena!='0':
                try:
                    numero=int(cadena)
                    salida=True
                except:
                    Print('{} no es un número'.format(cadena),line=25,column=1,style='bold',color='yellow', back='red')
                    cadena=Input(frase,line=1,column=5)
                clearLine(25)
            else:
                Print('ERROR!!!! El año tiene que tener 4 números o no ser 0',line=25,column=1,style='bold',color='yellow', back='red')
                cadena=Input(frase,line=1,column=5)
            clearLine(25)
    return numero

def ultimoNumero(strNumero):
    strNumero=str(strNumero)
    return int(strNumero[-1])

def comprobarFecha(fecha):
    actual=datetime.now()
    nacimiento=False
    while not nacimiento:
        if fecha[0]>1900 and fecha[2]<=(actual.year-1):
            nacimiento=True
        elif fecha[2]<=actual.year:
            if fecha[1]<=actual.month:
                if fecha[2]<=actual.day:
                    # Fecha correcta
                    nacimiento=True
                else:
                    # Fecha incorrecta, volver a comprobar de nuevo dia
                    Print('Todavia no has nacido',line=25,column=1,style='bold',color='yellow', back='red')
                    strNumero=Input('Introduce el {} que naciste: (Formato númerico) '.format('dia'),line=1,column=5)
                    fecha[2]=__comprobarNumero('Introduce el {} que naciste: (Formato númerico)'.format('dia'),'dia',strNumero)
                clearLine(25)
            else:
                # Fecha incorrecta, volver a comprobar de nuevo mes
                Print('Todavia no has nacido',line=25,column=1,style='bold',color='yellow', back='red')
                strNumero=Input('Introduce el {} que naciste: (Formato númerico) '.format('mes'),line=1,column=5)
                fecha[1]=__comprobarNumero('Introduce el {} que naciste: (Formato númerico)'.format('mes'),'mes',strNumero)
            clearLine(25)
        else:
            # Fecha incorrecta, volver a comprobar de nuevo mes
            Print('Todavia no has nacido',line=25,column=1,style='bold',color='yellow', back='red')
            strNumero=Input('Introduce el {} que naciste: (Formato númerico) '.format('año'),line=1,column=5)
            fecha[0]=__comprobarNumero('Introduce el {} que naciste: (Formato númerico)'.format('año'),'año',strNumero)
        clearLine(25)
    return fecha

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
    f=comprobarFecha(f)
    sh=armaTrajeSuperpoder(f)
    Print(frase(superheroe,sh[2],sh[0],sh[1]),line=5,column=5)