#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
	
# EI
proc_EI_L2H1 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_EI_L2H1.stdin.write("set autoscale \n")
proc_EI_L2H1.stdin.write("set title 'Erreur L2H1 en espace pour EI'\n")
proc_EI_L2H1.stdin.write("set xlabel 'log(h)'\n")
proc_EI_L2H1.stdin.write("set ylabel 'log(erreur)'\n")
proc_EI_L2H1.stdin.write("plot 'convergence_EI_P1b_0.005_L2H1.gp' u (log($1)):(log($2)) w line lc rgb 'red' t 'EI'\n")
proc_EI_L2H1.stdin.write("replot 'convergence_EI_P2_0.005_L2H1.gp' u (log($1)):(log($2)) w line lc rgb 'green' t 'P2'\n")
proc_EI_L2H1.stdin.write("replot x+5.5 w line lc rgb 'blue' t 'ordre 1'\n")
proc_EI_L2H1.stdin.write("replot 2*x+2 w line lc rgb 'magenta' t 'ordre 2'\n")
proc_EI_L2H1.stdin.write("set term postscript enhanced color\n")
proc_EI_L2H1.stdin.write('set output "convergence_EI_0.005_L2H1.eps"\n')
proc_EI_L2H1.stdin.write("replot\n")
proc_EI_L2H1.stdin.write("unset output\n")
proc_EI_L2H1.stdin.write('quit\n') #close the gnuplot window

proc_EI_LinfL2 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_EI_LinfL2.stdin.write("set autoscale \n")
proc_EI_LinfL2.stdin.write("set title 'Erreur LinfL2 en espace pour EI'\n")
proc_EI_LinfL2.stdin.write("set xlabel 'log(h)'\n")
proc_EI_LinfL2.stdin.write("set ylabel 'log(erreur)'\n")
proc_EI_LinfL2.stdin.write("plot 'convergence_EI_P1b_0.005_LinfL2.gp' u (log($1)):(log($2)) w line lc rgb 'red' t 'EI'\n")
proc_EI_LinfL2.stdin.write("replot 'convergence_EI_P2_0.005_LinfL2.gp' u (log($1)):(log($2)) w line lc rgb 'green' t 'EI'\n")
proc_EI_LinfL2.stdin.write("replot 2*x-0.5 w line lc rgb 'blue' t 'ordre 2'\n")
proc_EI_LinfL2.stdin.write("set term postscript enhanced color\n")
proc_EI_LinfL2.stdin.write('set output "convergence_EI_0.005_LinfL2.eps"\n')
proc_EI_LinfL2.stdin.write("replot\n")
proc_EI_LinfL2.stdin.write("unset output\n")
proc_EI_LinfL2.stdin.write('quit\n') #close the gnuplot window
