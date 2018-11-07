#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from const import *

# https://en.wikipedia.org/wiki/Planck%27s_law
def plancksLaw(wav, T):
    a = (2*h*c**2)/(wav**5)
    b = (h*c)/(wav*kB*T)
    sr = a*1/(np.exp(b)-1)   #Spectral Radiance: 
    return sr

# https://en.wikipedia.org/wiki/Hawking_radiation#Emission_process
def blackHoleTemperature(M):
    a = (hbar*c**3)/(8*np.pi*G*kB)
    temperature = a/M
    return temperature

def blackHoleTemperatureInSolarMass(M):
    temperature = blackHoleTemperature(M*MS)
    return temperature

def planckPeak(wav, intensity):
    lambdaPeack = wav[np.argmax(intensity)]
    return lambdaPeack

def schwarzschildRadius(M):
    rS = (2*G*M)/(c**2)
    return rS

def schwarzschildMass(rS):
    M = (c**2*rS)/(2*G)
    return M

def predictedLambdaMax(T):
    b = (h*c)/(4.9651*kB)
    lambdaMax = b/T
    return lambdaMax

#Stefan–Boltzmann–Schwarzschild–Hawking black hole radiation power law
def SBSHPow(M):
    power = (hbar*c**6)/(15360*np.pi*G**2*(M*MS)**2)
    return power

def printBHInfo(M, plot=False):
    start = 1e-2*M
    end = 1e+6*M
    step = (end-start)/(3e6-1)
    wav = np.arange(start, end, step)
    temperature = blackHoleTemperatureInSolarMass(M)
    intensity = plancksLaw(wav, temperature)
    maxLambda_calc = planckPeak(wav, intensity)
    maxLambda_pred = predictedLambdaMax(temperature)
    radius = schwarzschildRadius(M*MS)
    ratio = maxLambda_calc/radius
    power = SBSHPow(M)
    
    print "\nBH " + str(M) + " solar mass:" 
    print "Temperature:    " + str(temperature) + " K" 
    print "Planck peak:    " + str(maxLambda_calc) +  " m"
    print "Max lambda:     " + str(maxLambda_pred) +  " m"
    print "Radius:         " + str(radius) + " m"
    print "lambda/radius:  " + str(ratio)
    print "Radiated power: " + str(power) + " W.kg².M⁻²"
    if plot:
        plt.xlabel('$\lambda$ (m)')
        plt.ylabel('Spectral Radiance (sr$^{-1}$.m$^{-2}$.nm$^{-1}$)')
        plt.title('Planck\'s law')
        plt.plot(wav, intensity)
        plt.show()
