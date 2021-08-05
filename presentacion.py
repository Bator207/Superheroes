# import click

'''
    color			text_attributes
    =======			===============
    black			bold
    red				underline
    green			blink
    yellow			reversed
    blue
    magenta
    cyan
    white
    reset
'''
colors={
    'black':30,
    'red':31,
    'green':32,
    'yellow':33,
    'blue':34,
    'magenta':35,
    'cyan':36,
    'white':37,
    'reset':39
}

background={
    'black':40,
    'red':41,
    'green':42,
    'yellow':43,
    'blue':44,
    'magenta':45,
    'cyan':46,
    'white':47,
    'reset':49
}

styles={
    'bold':1,
    'underline':4,
    'blink':5,
    'reversed':7
}

def limpiar():
    print('\033[2J')

def locate(line, column):
    print ('\033[{};{}H'.format(line,column),end='')

def clearLine(line=None, column=None):
    if line is not None and column is not None:
        locate(line,column)
    elif line is not None:
        locate(line,1)
    print('\033[K',end='')

def processParams(params):
    if 'line' in params:
        line=params['line']
        column=1
        if 'column' in params:
            column=params['column']
        locate(line,column)

    if 'color'in params and params['color'] in colors:
        print('\033[{}m'.format(colors[params['color']]),end='')
    if 'back'in params and params['back'] in background:
        print('\033[{}m'.format(background[params['back']]),end='')
    if 'style'in params and params['style'] in styles:
        print('\033[{}m'.format(styles[params['style']]),end='')


def Print(cadena,**params):
    processParams(params)
    if 'nl' in params and params['nl']:
        print(cadena)
    else:
        print(cadena, end='')

    if 'nr'not in params:
        Reset()
    # locate(line,column)
    # if delEnd:
    #     clearLine()
    # print(cadena,end='')

def Input(msg,**params):
    processParams(params)

    if 'dirty' not in params:
        clearLine()
    return input(msg)
    # locate(line,column)
    # if delEnd:
    #     clearLine()
    # return input(msg)

def Format(estilo=0,fuente=39,fondo=39):
    print('\033[{};{};{}m'.format(estilo,fuente,fondo),end='')

def Reset():
    Format(0)