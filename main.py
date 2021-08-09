from config import *

# class SuperHeroe():
#     def __init__(self):
#         self.superheroe=''
#         self.traje=''
#         self.superpoder=''
#         self.arma=''
        

def comprobarNombre(nom):
    letra=nom[0].upper()
    if letra in nombre:
        return nombre[letra]
    else:
        print('{} no es una letra'.format(nom[0]))

def comprobarApellido(nom):
    letra=nom[0].upper()
    if letra in apellido:
        return apellido[letra]
    else:
        print('{} no es una letra'.format(nom[0]))

def comprobarDia(strNumero):
    try:
        numero=int(strNumero)
        if numero in dia.keys():
            return dia[numero]
    except:
        print('{} no es un numero'.format(strNumero))

def comprobarMes(strNumero):
    try:
        numero=int(strNumero)
        if numero in mes.keys():
            return mes[numero]
    except:
        print('{} no es un numero'.format(strNumero))

def comprobarAny(strNumero):
    try:
        numero=int(strNumero[-1])
        if numero in any.keys():
            return any[numero]
    except:
        print('{} no es un numero'.format(strNumero))

if __name__=='__main__':
    superheroe=''
    # sh=SuperHeroe()
    nom=input('Introduce tu nombre: ')
    cognom=input('Introduce tu apellido: ')
    diaN=input('Introduce el dia que naciste: (Formato númerico)')
    mesN=input('Introduce el mes que naciste: (Formato númerico)')
    anyN=input('Introduce el año que naciste: (Formato númerico)')

    superheroe+=comprobarNombre(nom)
    superheroe+=' '
    superheroe+=comprobarApellido(cognom)
    print(superheroe)
    arma=comprobarDia(diaN)
    print(arma)
    superpoder=comprobarMes(mesN)
    print(superpoder)
    traje=comprobarAny(anyN)
    print(traje)