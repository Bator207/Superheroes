from config import *
from datetime import datetime
from presentacion import *

# Función que te devuelve la frase del superheroe
def frase(sh,co,ar,sp):
    return ('Soy {} {}, mi poder es el {} y voy a luchar contra la injusticia con mi {}!!'.format(sh,co,sp,ar))

# Función para sacar la primera y comprobar que sea correcta
def comprobarNombre(dic,frase):
    salida=False
    while not salida:
        cadena=Input(frase,line=1,column=5)
        if cadena == '':
            Print('ERROR!!!! No puede ser vació',line=25,column=1,style='bold',color='yellow', back='red')
            continue
        letra=cadena[0].upper()
        if letra in dic:
            salida=True
            clearLine(25)
        else:
            Print('{} no es una letra'.format(cadena[0]),line=25,column=1,style='bold',color='yellow', back='red')
    return dic[letra]

# Función donde se pide la fecha de nacimiento
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
            # Comprobamos si es un número
            try:
                numero=int(cadena)
            except:
                Print('{} no es un número'.format(cadena),line=25,column=1,style='bold',color='yellow', back='red')
                continue
            # Comprobamos que sea año
            if i == 'año':
                # Comprobamos si la longitud del año es de 4 o diferente de 0
                if len(cadena)==4 and cadena!='0':
                    # Comprobamos que el año este entre 1920 y año actual
                    if numero>=1920 and numero<=actual.year:
                        # Agregamos el año a la fecha
                        fecha.append(numero)
                        nacimiento=True
                    else:
                        Print("ERROR!!!! Año incorrecto",line=25,column=1,style='bold',color='yellow', back='red')
                        continue
                else:
                    Print('ERROR!!!! No puede ser 0 o tener una longitud diferente de 4 digitos',line=25,column=1,style='bold',color='yellow', back='red')
                    continue
            # Comprobamos que sea mes
            elif i == 'mes':
                # Comprobamos si la longitud del mes es menor o igual a 2 o diferente de 0
                if len(cadena)<=2 and cadena!='0':
                    # Comprobamos que el numero este en el rango de los meses
                    if numero in mes:
                        # Comprobamos si es el año actual
                        if fecha[0]==actual.year:
                            # Comprobamos que el mes sea menor o igual al actual
                            if numero<=actual.month:
                                # Agregamos el mes a la fecha
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
                    Print('ERROR!!!! No puede ser 0 o tener una longitud mayor de 2 a digitos',line=25,column=1,style='bold',color='yellow', back='red')
                    continue
            # Comprobamos que sea el Día
            elif i == 'dia':
                #Falta comprobar que esta en el rango
                if len(cadena)<=2 and cadena!='0':
                    # Comprobamos que el numero este en el rango de los Días
                    if numero in dia and numero<=meses[fecha[1]]:
                        # Comprobamos si es el mes actual
                        if fecha[1]==actual.month:
                            # Comprobamos que el Día sea menor o igual al actual
                            if numero<=actual.day:
                                # Agregamos el Día a la fecha
                                fecha.append(numero)
                                nacimiento=True
                            else:
                                Print('ERROR!!!! Día incorrecto',line=25,column=1,style='bold',color='yellow', back='red')
                                continue
                        else:
                            fecha.append(numero)
                            nacimiento=True
                    else:
                        Print('ERROR!!!! Día incorrecto',line=25,column=1,style='bold',color='yellow', back='red')
                        continue
                else:
                    Print('ERROR!!!! No puede ser 0 o tener una longitud mayor de 2 a digitos',line=25,column=1,style='bold',color='yellow', back='red')
                    continue
            else:
                Print('ERROR!!!!',line=25,column=1,style='bold',color='yellow', back='red')
                continue
    return fecha

# Sacamos el ultimo número 
def ultimoNumero(strNumero):
    strNumero=str(strNumero)
    return int(strNumero[-1])

# Pasamos la información para sacar el arma, el superpoder y el traje del superheroe
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
    Print(frase(superheroe,sh[2],sh[0],sh[1]),line=5,column=5,style='bold',color='red', back='green')