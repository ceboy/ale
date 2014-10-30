#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
	
# EI
proc_L2H1 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_L2H1.stdin.write("set autoscale \n")
proc_L2H1.stdin.write("set title 'Erreur L2H1 en temps'\n")
proc_L2H1.stdin.write("set xlabel 'log(pas)'\n")
proc_L2H1.stdin.write("set ylabel 'log(erreur)'\n")
proc_L2H1.stdin.write("plot 'convergence_16_P2_LinfL2.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2'\n")
proc_L2H1.stdin.write("replot 2*x+2 w line t 'ordre 2'\n")
proc_L2H1.stdin.write("set term postscript enhanced color\n")
proc_L2H1.stdin.write('set output "convergence_temps_16_L2H1.eps"\n')
proc_L2H1.stdin.write("replot\n")
proc_L2H1.stdin.write("unset output\n")
proc_L2H1.stdin.write('quit\n') #close the gnuplot window

proc_LinfL2 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_LinfL2.stdin.write("set autoscale \n")
proc_LinfL2.stdin.write("set title 'Erreur LinfL2 en temps'\n")
proc_LinfL2.stdin.write("set xlabel 'log(pas)'\n")
proc_LinfL2.stdin.write("set ylabel 'log(erreur)'\n")
proc_LinfL2.stdin.write("plot 'convergence_16_P2_LinfL2.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2'\n")
proc_LinfL2.stdin.write("replot 2*x+2 w line t 'ordre 2'\n")
proc_LinfL2.stdin.write("set term postscript enhanced color\n")
proc_LinfL2.stdin.write('set output "convergence_temps_16_LinfL2.eps"\n')
proc_LinfL2.stdin.write("replot\n")
proc_LinfL2.stdin.write("unset output\n")
proc_LinfL2.stdin.write('quit\n') #close the gnuplot window

proc_L2H1 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_L2H1.stdin.write("set autoscale \n")
proc_L2H1.stdin.write("set title 'Erreur L2H1 en temps'\n")
proc_L2H1.stdin.write("set xlabel 'log(pas)'\n")
proc_L2H1.stdin.write("set ylabel 'log(erreur)'\n")
proc_L2H1.stdin.write("set xrange [-2.8:-1.4] \n")
proc_L2H1.stdin.write("plot 'convergence_16_P2_LinfL2.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2'\n")
proc_L2H1.stdin.write("replot 2*x+1.8 w line t 'ordre 2'\n")
proc_L2H1.stdin.write("set term postscript enhanced color\n")
proc_L2H1.stdin.write('set output "convergence_temps_16_L2H1b.eps"\n')
proc_L2H1.stdin.write("replot\n")
proc_L2H1.stdin.write("unset output\n")
proc_L2H1.stdin.write('quit\n') #close the gnuplot window

proc_LinfL2 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_LinfL2.stdin.write("set autoscale \n")
proc_LinfL2.stdin.write("set title 'Erreur LinfL2 en temps'\n")
proc_LinfL2.stdin.write("set xlabel 'log(pas)'\n")
proc_LinfL2.stdin.write("set ylabel 'log(erreur)'\n")
proc_LinfL2.stdin.write("set xrange [-2.8:-1.4] \n")
proc_LinfL2.stdin.write("plot 'convergence_16_P2_LinfL2.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2'\n")
proc_LinfL2.stdin.write("replot 2*x+1.8 w line t 'ordre 2'\n")
proc_LinfL2.stdin.write("set term postscript enhanced color\n")
proc_LinfL2.stdin.write('set output "convergence_temps_16_LinfL2b.eps"\n')
proc_LinfL2.stdin.write("replot\n")
proc_LinfL2.stdin.write("unset output\n")
proc_LinfL2.stdin.write('quit\n') #close the gnuplot window