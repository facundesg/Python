#SCRIPT PARA CALCULAR OS MODOS QUE SE PROPAGAM EM UM GUIA DE TRANSMISSAO VAZIO
#GABRIEL FACUNDES CARNEIRO - 2013

from pylab import *

#comprimento em milimetros
def freqC(aa,bb,m,n):
    A = m/aa
    B = n/bb
    Fc = 150000000000.0 * sqrt( (A*A) + (B*B) )
    
    return Fc

#f = frequencia do sinal
#a = comprimento a
#b = comprimento b
#L = modo limite
def modos(f,a,b,L):
    i = 0
    j = 1
    while(j<L):
        if (f > freqC(a,b,i,j)):
            print "Propaga o modo TE%d%d" % (i,j)
        j = j + 1
    
    i = 1
    j = 0
    while(i<L):
        if (f > freqC(a,b,i,j)):
            print "Propaga o modo TE%d%d" % (i,j)
        i = i + 1

    i = 1
    j = 1
    while(i<L):
        while(j<L):
            if (f > freqC(a,b,i,j)):
                print "Propaga os modos TE%d%d e TM%d%d" % (i,j,i,j)
            j = j + 1
        i = i + 1
            

