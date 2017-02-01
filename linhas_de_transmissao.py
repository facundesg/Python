# -*- coding: utf-8 -*-
#Script em Python para plotar curvas de tensao em linhas de transmissao sem perdas
#Gabriel Facundes Carneiro - 2017

from pylab import *

def transient(ponto):

	E = 225.
	Rg = 50.
	Rl = 150.
	R0 = 75.
	#posicao
	x = ponto
	eixoX = arange(10.)

	gamaG = 0.
	gamaL = 0.
	V1p = 0.
	V = arange(40.) #tensao nos terminais
	Vt =arange(10.) #tensao no ponto desejado

	#calcula a tensao entrando na linha
	V1p = E*R0/(Rg + R0)

	gamaG = (Rg - R0)/(Rg + R0)
	gamaL = (Rl - R0)/(Rl + R0)

	V[0] = V1p
	p = 1
	while p < 30:
		if p%2 == 1:
			V[p] = V[p-1] * gamaL
		elif p%2 == 0:
			V[p] = V[p-1] * gamaG
		p = p+1

	#calculando a tensao em um ponto especifico

	Vt[0] = V[0]
	i = 1

	if (x > 0) and (x < 1):
		for k in eixoX:
			eixoX[k] = eixoX[k] + x
			
		T = 1
		
		while i < 10:
			Vt[i] = Vt[i-1] + V[i]
			i = i+1
			
	elif x == 0:
		T = 2    
		while i < 10:
			Vt[i] = Vt[i-1] + V[2*i] + V[(2*i)-1]
			i = i+1
			
	elif x == 1:
		for k in eixoX:
			eixoX[k] = eixoX[k] + x
		T = 2    
		while i < 10:
			Vt[i] = Vt[i-1] + V[2*i] + V[(2*i)-1]
			i = i+1
			
	return Vt, eixoX


H0, eixo0 = transient(0)
H05, eixo05 = transient(0.5)
H1, eixo1 = transient(1)

subplot(2,2,1)
bar(eixo0,H0,width=1)
xticks([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10])    

subplot(2,2,2)
bar(eixo05,H05,width=1)
xticks([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10])    

subplot(2,2,3)
bar(eixo1,H1,width=1)
xticks([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10])    

show()  
    

