#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from bigfloat import *
from const import *
from func import *

if __name__ == "__main__":
    import argparse, os, sys
    parser = argparse.ArgumentParser(description='Process the command line options')
    parser.add_argument('-d', '--debug', action='store_true', help='Enter debug mode')
    parser.add_argument('-p', '--plot', action='store_true', help='Do plots')
    parser.add_argument('-v', '--verbose', action='store_true', help='Whether to print verbose output')

    args = parser.parse_args()

    wavNM = np.arange(1e-9, 3e-6, 1e-9)
    wavMM = np.arange(1e-3, 3e-1, 1e-6)
    wavM = np.arange(1e0, 1e3, 1e0)
    
    if args.debug:
        intensity5000 = plancksLaw(wavNM, 5000.)
        intensity1 = plancksLaw(wavMM, 1)
        # Smallest BH
        smallest_mass = schwarzschildMass(lP)/MS
        highest_temp = blackHoleTemperatureInSolarMass(smallest_mass)
        mCMB = massFromTemperature(2.7)/MS
        m46963 = massFromLambda(46963)
        print "=== DEBUG "
        print "5000K Peak at:             " + str(planckPeak(wavNM, intensity5000)*1e+9) +  " nm"
        print "1K Peak at:                " + str(planckPeak(wavMM, intensity1)*1e+3) +  " mm"
        print "Mass of t=2.7K m: " + str(mCMB) + " Solar Masses"
        print "Mass of wavelen = 46963 m: " + str(m46963) + " Solar Masses"
        print "========= \n"

    if args.plot:
        startM = 1e-10
        endM = 1e-5
        stepM = (endM-startM)/(3e6-1)
        BHmasses = np.arange(startM,endM, stepM)
        
        print "=== PLOT "
        # Black Hole: Temperature vs Mass
        plt.xlabel('Mass (Solar Mass)')
        plt.ylabel('Temperature (K)')
        plt.title('Black Hole: Temperature vs Mass')
        plt.xscale('log')
        plt.yscale('log')
        plt.plot(BHmasses,blackHoleTemperatureInSolarMass(BHmasses))
        plt.show()
    
    if args.debug:
        print ">Planck lenght black hole"
        printBHInfo(schwarzschildMass(lP)/MS, args.plot)
        print ">Primordial black hole"
        printBHInfo(1e-19, args.plot)
        print ">5K black hole"
        printBHInfo(massFromTemperature(5)/MS, args.plot)
        print ">Moon mass black hole"
        printBHInfo(3.69e-8, args.plot)
        #printBHInfo(1e-6, args.plot)
        print ">1 Solar mass black hole" 
        printBHInfo(1, args.plot)
        #printBHInfo(1e+6, args.plot)
        print ">Milky way's black hole"
        # https://en.wikipedia.org/wiki/Supermassive_black_hole#In_the_Milky_Way
        printBHInfo(4.1e+6, args.plot)
        print ">Supermassive black hole"
        printBHInfo(1e+11, args.plot)