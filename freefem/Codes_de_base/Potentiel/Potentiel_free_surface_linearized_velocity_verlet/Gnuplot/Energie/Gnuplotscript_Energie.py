#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
	
# Espace
proc_E_espace = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_E_espace.stdin.write("set autoscale \n")
proc_E_espace.stdin.write("set title 'Evolution energie en fonction du maillage'\n")
proc_E_espace.stdin.write("set xlabel 't'\n")
proc_E_espace.stdin.write("set ylabel 'Energie'\n")
proc_E_espace.stdin.write("plot 'convergence_5_0.004_P2_E.gp' u 1:2 w line t 'm: 5 ; pas : 16'\n")
proc_E_espace.stdin.write("replot 'convergence_10_0.004_P2_E.gp' u 1:2 w line t 'm: 10 ; pas :16'\n")
proc_E_espace.stdin.write("replot 'convergence_15_0.004_P2_E.gp' u 1:2 w line t 'm: 15 ; pas :16'\n")

proc_E_espace.stdin.write("set term postscript enhanced color\n")
proc_E_espace.stdin.write('set output "energie_espace.eps"\n')
proc_E_espace.stdin.write("replot\n")
proc_E_espace.stdin.write("unset output\n")
proc_E_espace.stdin.write('quit\n') #close the gnuplot window

#temps
proc_E_temps = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_E_temps.stdin.write("set autoscale \n")
proc_E_temps.stdin.write("set title 'Evolution energie en fonction du pas de temps'\n")
proc_E_temps.stdin.write("set xlabel 't'\n")
proc_E_temps.stdin.write("set ylabel 'Energie'\n")
proc_E_temps.stdin.write("plot 'convergence_16_0.04_P2_E.gp' u 1:2 w line t 'm: 16 ; pas :10'\n")
proc_E_temps.stdin.write("replot 'convergence_16_0.015_P2_E.gp' u 1:2 w line t 'm: 16 ; pas :13'\n")
proc_E_temps.stdin.write("replot 'convergence_16_0.002_P2_E.gp' u 1:2 w line t 'm: 16 ; pas :16'\n")
proc_E_temps.stdin.write("set term postscript enhanced color\n")
proc_E_temps.stdin.write('set output "energie_temps.eps"\n')
proc_E_temps.stdin.write("replot\n")
proc_E_temps.stdin.write("unset output\n")
proc_E_temps.stdin.write('quit\n') #close the gnuplot window

#convergence temps
proc_E_convtemps = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_E_convtemps.stdin.write("set autoscale \n")
proc_E_convtemps.stdin.write("set title 'Convergence en temps de l energie en fonction du pas de temps'\n")
proc_E_convtemps.stdin.write("set xlabel 'log(pas)'\n")
proc_E_convtemps.stdin.write("set ylabel 'log(Erreur)'\n")
proc_E_convtemps.stdin.write("plot 'convergence_16_P2_E.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2'\n")
proc_E_convtemps.stdin.write("set term postscript enhanced color\n")
proc_E_convtemps.stdin.write('set output "convergence_16_P2_E.eps"\n')
proc_E_convtemps.stdin.write("replot\n")
proc_E_convtemps.stdin.write("unset output\n")
proc_E_convtemps.stdin.write('quit\n') #close the gnuplot window

#convergence temps tronqué
proc_E_convtempst = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_E_convtempst.stdin.write("set autoscale \n")
proc_E_convtempst.stdin.write("set title 'Convergence en temps de l energie en fonction du pas de temps'\n")
proc_E_convtempst.stdin.write("set xlabel 'log(pas)'\n")
proc_E_convtempst.stdin.write("set ylabel 'log(Erreur)'\n")
proc_E_convtempst.stdin.write("set xrange [-2.8:-1.4] \n")
proc_E_convtempst.stdin.write("plot 'convergence_16_P2_E.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2'\n")
proc_E_convtempst.stdin.write("replot 2*x+1 w line t 'ordre 2'\n")
proc_E_convtempst.stdin.write("set term postscript enhanced color\n")
proc_E_convtempst.stdin.write('set output "convergence_16_P2_Eb.eps"\n')
proc_E_convtempst.stdin.write("replot\n")
proc_E_convtempst.stdin.write("unset output\n")
proc_E_convtempst.stdin.write('quit\n') #close the gnuplot window