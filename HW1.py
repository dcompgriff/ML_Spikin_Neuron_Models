# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:04:25 2016

@author: DAN
"""

import numpy as np
import matplotlib.pyplot as plt

#%   self MATLAB file generates figure 1 in the paper by 
#%               Izhikevich E.M. (2004) 
#%   Which Model to Use For Cortical Spiking Neurons? 
#%   use MATLAB R13 or later. November 2003. San Diego, CA 
#
#
#%%%%%%%%%%%%%%% regular spiking %%%%%%%%%%%%%%%%%%%%%% 
#
#steps = 500;                  %This simulation runs for 500 steps
#
#a=0.02; b=0.25; c=-65;  d=6;
#V=-64; u=b*V;
#VV=[];  uu=[];
#tau = 0.25; tspan = 0:tau:steps;  %tau is the discretization time-step
#                                  %tspan is the simulation interval
#                                
#T1=50;            %T1 is the time at which the step input rises
#for t=tspan
#    if (t>T1) 
#        I=1.0;     % This is the input which you will change in your simulation
#    else
#        I=0;
#    end;
#    V = V + tau*(0.04*V^2+5*V+140-u+I);
#    u = u + tau*a*(b*V-u);
#    if V > 30
#        VV(end+1)=30;         %VV is the time-series of membrane potentials
#        V = c;
#        u = u + d;
#    else
#        VV(end+1)=V;
#    end;
#    uu(end+1)=u;
#end;
#plot(tspan,VV);                   %VV is plotted as the output
#axis([0 max(tspan) -90 40])
#title('Tonic Spiking');


tau = .25
steps = 500
tspan = np.linspace(0, steps, num=steps/tau, endpoint=True)
#T1 is the time interval at which the input first rises.
T1 = 50

voltageList = []
uList = []

def runSingleNeuronSpiking():
    neuron1 = SpikingNeuron()
    inputI = 0
    for time in tspan:
        if time < T1:
            inputI = 0
        else:
            inputI = 1.0
        #Stimulate the neuron.
        voltageList.append(neuron1.stimulate(inputI))
    
    #When finished, plot the function output for the time span.
    plt.plot(tspan, voltageList)
    plt.axis([0, steps, -90, 40])
    plt.title('Tonic Spiking.')
    plt.show()
    

class SpikingNeuron:
    
    def __init__(self):
        self.a = 0.02
        self.b = 0.25
        self.c = -65
        self.d = 6
        self.V = -64
        self.tau = 0.25
        self.u = self.b * self.V
    
    def stimulate(self, inputI):
        #Do an incremental membrane potential update using the differential equation times the discretization.
        #Vn+1 = Vn + deltaVn
        #deltaVn = delta_t * (dV/dt)
        self.V = self.V + self.tau*( (0.04*(self.V**2)) + (5*self.V) + 140 - self.u + inputI )  
        vOut = self.V        
        #Do an increment for the 'u' differential equation.
        self.u = self.u + self.tau*(self.a*((self.b*self.V) - self.u))
        
        #Set up a peak saturation and breakdown condition.
        if(self.V >= 30 ):
            vOut = 30
            self.V = self.c
            self.u = self.u + self.d
        
        return vOut
        
        
    
if __name__ == "__main__":
    runSingleNeuronSpiking()
    
    
    
    