#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
	

proc_L2H1 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_L2H1.stdin.write("set autoscale \n")
proc_L2H1.stdin.write("set title 'Erreur L2H1 en espace'\n")
proc_L2H1.stdin.write("set xlabel 'log(h)'\n")
proc_L2H1.stdin.write("set ylabel 'log(erreur)'\n")
proc_L2H1.stdin.write("plot 'convergence_P2_0.004_L2H1.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2'\n")
proc_L2H1.stdin.write("replot 'convergence_m_P2_0.004_L2H1.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2m'\n")
proc_L2H1.stdin.write("replot 2*x-1 w line t 'ordre 2'\n")
proc_L2H1.stdin.write("set term postscript enhanced color\n")
proc_L2H1.stdin.write('set output "convergence_espace_0.004_L2H1.eps"\n')
proc_L2H1.stdin.write("replot\n")
proc_L2H1.stdin.write("unset output\n")
proc_L2H1.stdin.write('quit\n') #close the gnuplot window

proc_LinfL2 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_LinfL2.stdin.write("set autoscale \n")
proc_LinfL2.stdin.write("set title 'Erreur LinfL2 en espace'\n")
proc_LinfL2.stdin.write("set xlabel 'log(h)'\n")
proc_LinfL2.stdin.write("set ylabel 'log(erreur)'\n")
proc_LinfL2.stdin.write("plot 'convergence_P2_0.004_LinfL2.gp' u (log($1)/log(10)):(log($2)/log(10))  t 'P2'\n")
proc_LinfL2.stdin.write("replot 'convergence_m_P2_0.004_LinfL2.gp' u (log($1)/log(10)):(log($2)/log(10)) t 'P2m'\n")
proc_LinfL2.stdin.write("replot 2*x-1 w line t 'ordre 2'\n")
proc_LinfL2.stdin.write("set term postscript enhanced color\n")
proc_LinfL2.stdin.write('set output "convergence_0.004_LinfL2.eps"\n')
proc_LinfL2.stdin.write("replot\n")
proc_LinfL2.stdin.write("unset output\n")
proc_LinfL2.stdin.write('quit\n') #close the gnuplot window
