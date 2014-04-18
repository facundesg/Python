# -*- coding: utf-8 -*-
#GABRIEL FACUNDES CARNEIRO - 2014

#FUNÇÕES PARA CALCULAR OS PARAMETROS DE UM TRAFO DE DOIS ENROLAMENTOS
#A PARTIR DOS ENSAIOS CC E CA

from math import sqrt

def fazEnsaioCC(S, Pmed, Vmed, Vnom):
    Vcc = Vmed * Vnom                      #Tensao de curto é a tensao em porcentagem * tensao nominal
    In = S/Vnom                            #Corrente de nominal é a potencia total do trafo sobre a tensao nominal
    Rcc = Pmed/(In*In)                     #Resistencia de curto é a potência ativa sobre o quadrado da corrente de curto(nominal)
    Zcc = Vcc/In                           #Impedancia de curto é a tensao de curto sobre a corrente de curto(nominal)
    Xcc = sqrt(Zcc*Zcc - Rcc*Rcc)          #Reatancia é a raiz da impedancia e resistencia
    
    Zcc = complex(Rcc,Xcc)
    return Zcc

def fazEnsaioCA(S, Pmed, Imed, Vnom):
    In = S/Vnom                            #Corrente em aberto(nominal) é a potencia total do trafo sobre a tensao nominal
    Ica = Imed * In                        #Corrente em aberto é o produto da corrente em aberto pela corrente nominal
    Gca = Pmed/(Vnom*Vnom)                 #Condutancia em aberto é a potencia em aberto sobre a tensao nominal
    Yca = Ica/Vnom                         #Admitancia em aberto é a corrente em aberto sobre a tensao nominal
    Bca = sqrt(Yca*Yca - Gca*Gca)          #Susceptancia é a raiz da admitancia e condutancia
    
    Zca = complex(Gca,-1*Bca)
    return Zca
