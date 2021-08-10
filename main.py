from config import *

def comprobarNombre(nom,dic):
    letra=nom[0].upper()
    if letra in dic:
        return dic[letra]
    else:
        print('{} no es una letra'.format(nom[0]))

def comprobarNumero(strNumero,dic):
    try:
        numero=int(strNumero)
        if numero in dic.keys():
            return dic[numero]
    except:
        print('{} no es un numero'.format(strNumero))

def ultimoNumero(strNumero):
    try:
        return int(strNumero[-1])
    except:
        print('{} no es un numero'.format(strNumero))

def frase(sh,co,ar,sp):
    return ('Soy {} {}, mi poder es el {} y voy a luchar contra la injusticia con mi {}!!'.format(sh,co,sp,ar))

if __name__=='__main__':
    superheroe=''
    nom=input('Introduce tu nombre: ')
    cognom=input('Introduce tu apellido: ')
    diaN=input('Introduce el dia que naciste: (Formato númerico)')
    mesN=input('Introduce el mes que naciste: (Formato númerico)')
    anyN=input('Introduce el año que naciste: (Formato númerico)')

    superheroe+=comprobarNombre(nom,nombre)
    superheroe+=' '
    superheroe+=comprobarNombre(cognom,apellido)
    arma=comprobarNumero(diaN,dia)
    superpoder=comprobarNumero(mesN,mes)
    traje=comprobarNumero(ultimoNumero(anyN),any)
    print(frase(superheroe,traje,arma,superpoder))