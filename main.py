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
        print('{} no es un numero'.format(numero))

    # try:
    #     numero=int(strNumero)
    #     if numero in dia.keys():
    #         return dia[numero]
    #     else:
    #         print('{} no es un numero'.format(numero))
    # except:
    #     pass





if __name__=='__main__':
    superheroe=''
    arma=''
    # sh=SuperHeroe()
    nom=input('Introduce tu nombre: ')
    cognom=input('Introduce tu apellido: ')
    dia=input('Introduce el dia que naciste: ')

    superheroe+=comprobarNombre(nom)
    superheroe+=' '
    superheroe+=comprobarApellido(cognom)
    print(superheroe)
    arma=comprobarDia(dia)
    print(arma)

