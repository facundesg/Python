# -*- coding: utf-8 -*-

# SCRIPT QUE A PARTIR DOS DADOS DE ENSAIOS CC E CA
# CALCULA OS PARAMETROS DE UM TRAFO DE DOIS ENROLAMENTOS
# EM SEGUIDA CALCULA A REGULACAO E O RENDIMENTO
# PARA MEIA CARGA, CARGA PLENA E SEM CARGA

# GABRIEL FACUNDES CARNEIRO - 2014

from numpy import sqrt, arccos, sin, conjugate, zeros

#matriz para analisar os dados
M = zeros((8,3), 'complex')

#trafo monofasico
Pnominal = 100000. #VA
V1e = 13800. #V
V2e = 34500. #V

#autotrafo
V1a = 34500. #V
V2a = 48300. #V

#ensaio cc
Vccp = 0.1
Pcc = 1000. #W
#ensaio ca
Icap = 0.08
Pca = 500. #W

#cargas
L1 = 50000  #VA
L2 = 0      #VA
L3 = 100000 #VA
fp = 0.8

#valores no lado de alta do monofasico
#parametros pelo ensaio de curto
In = Pnominal/V2e

print("Tensão de curto circuito: ")
Vcc = Vccp * V2e
print(Vcc)

print("Corrente de curto circuito: ")
Icc = In
print(Icc)

print("Resistencia de curto circuito: ")
Rcc = Pcc/(Icc*Icc)
print(Rcc)

print("Impedancia de curto circuito: ")
Zcc = Vcc/Icc
print(Zcc)

print("Reatancia de curto circuito: ")
Xcc = sqrt(Zcc*Zcc - Rcc*Rcc)
print(Xcc)

Zcc = complex(Rcc, Xcc)

#parametros pelo ensaio ca
print("Corrente de circuito aberto: ")
Ica = Icap*In
print Ica

print("Tensao de circuito aberto: ")
Vca = V2e
print Vca

print("Condutancia de circuito aberto: ")
Gca = Pca/(Vca*Vca)
print(Gca)

print("Admitancia de circuito aberto: ")
Yca = Ica/Vca
print(Yca)

print("Susceptancia de circuito aberto: ")
Bca = sqrt(Yca*Yca - Gca*Gca)
print(Bca)

Yca = complex(Gca,-1*Bca)

######################
#Em meia carga
######################
print '\nEm meia carga'

I2conj = 50000*complex((fp),sin(arccos(fp)))/V2a
print 'Corrente no secundário'
I2 = conjugate(I2conj)
print(I2)

print 'Corrente referida ao primario'
I1 = I2*V2a/V1a
print(I1)

print 'Corrente na admitancia'
Ip1 = Yca * V1a
print(Ip1)

print 'Corrente total no gerador'
It = I1 + Ip1
print(It)

print 'Queda de tensão nos condutores'
Vin = V1a + Zcc*It
print(Vin)

#ENFIM

print 'Regulacao de tensao'
Reg = (abs(Vin) - abs(V1a))/abs(Vin)
print(Reg)

print 'Potencia de entrada'
Sin = Vin * conjugate(It)
print(Sin)

print 'Rendimento'
n = L1*fp/Sin.real
print(n)

M[0,0], M[1,0], M[2,0], M[3,0], M[4,0] = I2, I1, Ip1, It, Vin
M[5,0], M[6,0], M[7,0]                 = Reg, Sin, n

######################
#Em vazio
######################
print '\nA vazio'

I2conj = 0*complex((fp),sin(arccos(fp)))/V2a
print 'Corrente no secundário'
I2 = conjugate(I2conj)
print(I2)

print 'Corrente referida ao primario'
I1 = I2*V2a/V1a
print(I1)

print 'Corrente na admitancia'
Ip1 = Yca * V1a
print(Ip1)

print 'Corrente total no gerador'
It = I1 + Ip1
print(It)

print 'Queda de tensão nos condutores'
Vin = V1a + Zcc*It
print(Vin)

#ENFIM

print 'Regulacao de tensao'
Reg = (abs(Vin) - abs(V1a))/abs(Vin)
print(Reg)

print 'Potencia de entrada'
Sin = Vin * conjugate(It)
print(Sin)

print 'Rendimento'
n = L2*fp/Sin.real
print(n)

M[0,1], M[1,1], M[2,1], M[3,1], M[4,1] = I2, I1, Ip1, It, Vin
M[5,1], M[6,1], M[7,1]                 = Reg, Sin, n

######################
#Em plena carga
######################
print '\nPlena carga'

I2conj = 100000*complex((fp),sin(arccos(fp)))/V2a
print 'Corrente no secundário'
I2 = conjugate(I2conj)
print(I2)

print 'Corrente referida ao primario'
I1 = I2*V2a/V1a
print(I1)

print 'Corrente na admitancia'
Ip1 = Yca * V1a
print(Ip1)

print 'Corrente total no gerador'
It = I1 + Ip1
print(It)

print 'Queda de tensão nos condutores'
Vin = V1a + Zcc*It
print(Vin)

#ENFIM

print 'Regulacao de tensao'
Reg = (abs(Vin) - abs(V1a))/abs(Vin)
print(Reg)

print 'Potencia de entrada'
Sin = Vin * conjugate(It)
print(Sin)

print 'Rendimento'
n = L3*fp/Sin.real
print(n)

M[0,2], M[1,2], M[2,2], M[3,2], M[4,2] = I2, I1, Ip1, It, Vin
M[5,2], M[6,2], M[7,2]                 = Reg, Sin, n

print '\n', M