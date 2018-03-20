# -*- coding: utf-8 -*-
import re
patron = re.compile("^\d*$")

class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            print ("la pila esta vacia")
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

variables=[]
posicion= 0



def postfijo(lista):
    p=Pila()
    tam=len(lista)
    bandera=True
    for x in range(tam):
        var=lista[x]
        if (esOperador(var)==True):
            p.apilar(int(operar(lista[x],p.desapilar(),p.desapilar())))
        else:
            if (esVariable(var)==True):
                if (buscar(var)==True):
                    var=variables[posicion+1]
                    p.apilar(int(var))
                else: 
                    print('no encontro', var)
                    return False
            else:
                if (esNumero(var)==True):
                    p.apilar(int(var))
                else:
                    print('caracter invalido comprobo todo para', var)
                    return False

    return p.desapilar()


def esOperador(v):
    if v=="+":
        return True
    if v=="-":
        return True
    if v=="/":
        return True
    if v=="*":
        return True
    return False
    
def esNumero(v):
    
    try:
	v = int(v)
        return True
    except ValueError:
        return False
    #if type(v) != int:
     #   raise TypeError,  v+ "v debe ser del tipo int"
#	return False
 #   else:
#	return True 








def esVariable(v):
    if(esNumero(v)==False):
    
		
	
	try:
 	    if(len(v)==1):
	    	if ord(v)>=65 and ord(v)<=90:
                    return True
             	else:	
	    
	    	    return False
	    else:
		print ("ay mama")
		return False
	except ValueError:
	    return False	
       
    
def operar(o, y, x):
    if o=="+":
        z=x+y
    if o=="-":
        z=x-y
    if o=="*":
        z=x*y
    if o=="/":
        z=x/y
    return z

def agregarVariable(var,val):
    variables.append(var)
    variables.append(val)

def buscar(v):
    tam=len(variables)
    for i in range(tam):
        if v == variables[i]:
            posicion=i
            return True
    return False

def comprobar(lista):
    tam=len(lista)
    print (tam)
    if lista[tam-1]=='='or lista[tam-1]=="=\r":
        if esVariable(lista[tam-2])==True:
            if(postfijo(lista[0:tam-2])==False):
                return False
            else:
                agregarVariable(lista[tam-2], postfijo(lista[0:tam-2]))
        else:
            return "algún dato es erroneo"
    else:
        print "no se iguala a nada"
            
def start ():
    f=open('prueba1.txt','r')
    lista=[y.split(' ') for y in [x.strip('\n') for x in (f.readlines())]]
    print (lista)
    for i in range(len(lista)):
        if (comprobar(lista[i])==False):
            break
        else:
            print (variables)    
start()

