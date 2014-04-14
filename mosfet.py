# -*- coding: utf-8 -*-
#GABRIEL FACUNDES CARNEIRO
#2014

#MODELADOR DE TRANSISTORES MOSFET

from pylab import *

class nMos:
    def __init__(self,vvth,vvg,vvd,vvs):
        self.vth = vvth
        self.vg  = vvg
        self.vd  = vvd
        self.vs  = vvs
        self.vgs = self.vg - self.vs
        self.vds = self.vd - self.vs                            
    
    #tipo do mos
    mosType = 'n'  
    
    #Parametro de transcondutância
    #kn = un*Cox
    kn = 194.0E-6
    W  = 8.0E-6
    L  = 0.8E-6
    
    #Corrente no canal
    def calcCurrent(self):
        iD = self.kn*self.W*(1/self.L)*((self.vgs - self.vth)*self.vds - (self.vds*self.vds)/2)
        return iD
    
    #Estado de operacao
    def State(self):         
        print('NMOS!')                
        if(self.vgs < self.vth):
            print('Corte')
        else:
            if(self.vds == self.vgs - self.vth):
                print('Limiar')
                    
            elif(self.vds < self.vgs - self.vth):
                print('Triodo')
                
            elif(self.vds > self.vgs - self.vth):
                print('Saturação')     
    
    #plota a curva caracteristica do mosfet em relacao a vds
    def plotVds(self):
        xx = arange(0,5,0.01)
        gg = arange(self.vth,self.vth+3,0.5)
        y = zeros(xx.size)
        
        for j in gg:
            for i in range(0, xx.size):
                if(xx[i] <= (j - self.vth)):
                    y[i] = self.kn*self.W*(1/self.L)*((j - self.vth)*xx[i] - (xx[i]*xx[i])/2)
                elif(xx[i] > (j - self.vth)):
                    y[i] = 0.5*self.kn*self.W*(1/self.L)*(j - self.vth)*(j - self.vth)
            plot(xx,y)        

    #plota a curva caracteristica do mosfet em relacao a vgs
    def plotVgs(self):
        gg = arange(0,self.vth+3,0.01)
        y = zeros(gg.size)
        #vvds = self.vgs - self.vth #vds em saturacao
        
        for i in range(0, gg.size):
            if(gg[i] >= self.vth):
                y[i] = 0.5*self.kn*self.W*(1/self.L)*(gg[i] - self.vth)*(gg[i] - self.vth)
        
        plot(gg,y)                                        
                                                                                                
class pMos:
    def __init__(self,vvth,vvg,vvd,vvs):
        self.vth = vvth
        self.vg  = vvg
        self.vd  = vvd
        self.vs  = vvs        
    mosType = 'p'

    def State(self):
        self.vgs = self.vg - self.vs
        self.vds = self.vd - self.vs    
        print('PMOS!')                
        if(self.vgs > self.vth):
            print('Corte')
        else:
            if(self.vds == self.vgs - self.vth):
                print('Limiar')
                    
            elif(self.vds > self.vgs - self.vth):
                print('Triodo')
                
            elif(self.vds < self.vgs - self.vth):
                print('Saturação')             


ummos = nMos(2,5,3,0)
subplot(121)
ummos.plotVds()
xticks(arange(0,5.5,0.5))
grid()

subplot(122)
ummos.plotVgs()
xticks(arange(0,5.5,0.5))
grid()

show()
