#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
	
# EI
proc_EI_L2H1 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_EI_L2H1.stdin.write("set autoscale \n")
proc_EI_L2H1.stdin.write("set title 'Erreur en temps pour la norme L2H1 - Stokes'\n")
proc_EI_L2H1.stdin.write("set xlabel 'log(pas)'\n")
proc_EI_L2H1.stdin.write("set ylabel 'log(erreur)'\n")
proc_EI_L2H1.stdin.write("plot 'convergence_16_EI_P2_L2H1.gp' u (log($1)):(log($2)) w line lc rgb 'red' t 'EI'\n")
proc_EI_L2H1.stdin.write("replot x+4.5 w line lc rgb 'blue' t 'ordre 1'\n")
proc_EI_L2H1.stdin.write("set term postscript enhanced color\n")
proc_EI_L2H1.stdin.write('set output "convergence_16_EI_P2_L2H1.eps"\n')
proc_EI_L2H1.stdin.write("replot\n")
proc_EI_L2H1.stdin.write("unset output\n")
proc_EI_L2H1.stdin.write('quit\n') #close the gnuplot window

proc_EI_LinfL2 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_EI_LinfL2.stdin.write("set autoscale \n")
proc_EI_LinfL2.stdin.write("set title 'Erreur en temps pour la norme LinfL2 - Stokes'\n")
proc_EI_LinfL2.stdin.write("set xlabel 'log(pas)'\n")
proc_EI_LinfL2.stdin.write("set ylabel 'log(erreur)'\n")
proc_EI_LinfL2.stdin.write("plot 'convergence_16_EI_P2_LinfL2.gp' u (log($1)):(log($2)) w line lc rgb 'red' t 'EI'\n")
proc_EI_LinfL2.stdin.write("replot x+3 w line lc rgb 'blue' t 'ordre 1'\n")
proc_EI_LinfL2.stdin.write("set term postscript enhanced color\n")
proc_EI_LinfL2.stdin.write('set output "convergence_16_EI_P2_LinfL2.eps"\n')
proc_EI_LinfL2.stdin.write("replot\n")
proc_EI_LinfL2.stdin.write("unset output\n")
proc_EI_LinfL2.stdin.write('quit\n') #close the gnuplot window

# CN
proc_CN_L2H1 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_CN_L2H1.stdin.write("set autoscale \n")
proc_CN_L2H1.stdin.write("set title 'Erreur en temps pour la norme L2H1 - Stokes'\n")
proc_CN_L2H1.stdin.write("set xlabel 'log(pas)'\n")
proc_CN_L2H1.stdin.write("set ylabel 'log(erreur)'\n")
proc_CN_L2H1.stdin.write("plot 'convergence_16_CN_P2_L2H1.gp' u (log($1)):(log($2)) w line lc rgb 'red' t 'CN'\n")
proc_CN_L2H1.stdin.write("replot 2*x+5 w line lc rgb 'blue' t 'ordre 2'\n")
proc_CN_L2H1.stdin.write("set term postscript enhanced color\n")
proc_CN_L2H1.stdin.write('set output "convergence_16_CN_P2_L2H1.eps"\n')
proc_CN_L2H1.stdin.write("replot\n")
proc_CN_L2H1.stdin.write("unset output\n")
proc_CN_L2H1.stdin.write('quit\n') #close the gnuplot window

proc_CN_LinfL2 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_CN_LinfL2.stdin.write("set autoscale \n")
proc_CN_LinfL2.stdin.write("set title 'Erreur en temps pour la norme LinfL2 - Stokes'\n")
proc_CN_LinfL2.stdin.write("set xlabel 'log(pas)'\n")
proc_CN_LinfL2.stdin.write("set ylabel 'log(erreur)'\n")
proc_CN_LinfL2.stdin.write("plot 'convergence_16_CN_P2_LinfL2.gp' u (log($1)):(log($2)) w line lc rgb 'red' t 'CN'\n")
proc_CN_LinfL2.stdin.write("replot 2*x+3 w line lc rgb 'blue' t 'ordre 2'\n")
proc_CN_LinfL2.stdin.write("set term postscript enhanced color\n")
proc_CN_LinfL2.stdin.write('set output "convergence_16_CN_P2_LinfL2.eps"\n')
proc_CN_LinfL2.stdin.write("replot\n")
proc_CN_LinfL2.stdin.write("unset output\n")
proc_CN_LinfL2.stdin.write('quit\n') #close the gnuplot window

# BDF2
proc_BDF2_L2H1 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_BDF2_L2H1.stdin.write("set autoscale \n")
proc_BDF2_L2H1.stdin.write("set title 'Erreur en temps pour la norme L2H1 - Stokes'\n")
proc_BDF2_L2H1.stdin.write("set xlabel 'log(pas)'\n")
proc_BDF2_L2H1.stdin.write("set ylabel 'log(erreur)'\n")
proc_BDF2_L2H1.stdin.write("plot 'convergence_16_BDF2_P2_L2H1.gp' u (log($1)):(log($2)) w line lc rgb 'red' t 'BDF2'\n")
proc_BDF2_L2H1.stdin.write("replot 2*x+2 w line lc rgb 'blue' t 'ordre 2'\n")
proc_BDF2_L2H1.stdin.write("set term postscript enhanced color\n")
proc_BDF2_L2H1.stdin.write('set output "convergence_16_BDF2_P2_L2H1.eps"\n')
proc_BDF2_L2H1.stdin.write("replot\n")
proc_BDF2_L2H1.stdin.write("unset output\n")
proc_BDF2_L2H1.stdin.write('quit\n') #close the gnuplot window

proc_BDF2_LinfL2 = subprocess.Popen(['gnuplot','-p'], 
				shell=True,
				stdin=subprocess.PIPE,
				)
proc_BDF2_LinfL2.stdin.write("set autoscale \n")
proc_BDF2_LinfL2.stdin.write("set title 'Erreur en temps pour la norme LinfL2 - Stokes'\n")
proc_BDF2_LinfL2.stdin.write("set xlabel 'log(pas)'\n")
proc_BDF2_LinfL2.stdin.write("set ylabel 'log(erreur)'\n")
proc_BDF2_LinfL2.stdin.write("plot 'convergence_16_BDF2_P2_LinfL2.gp' u (log($1)):(log($2)) w line lc rgb 'red' t 'BDF2'\n")
proc_BDF2_LinfL2.stdin.write("replot 2*x+2 w line lc rgb 'blue' t 'ordre 2'\n")
proc_BDF2_LinfL2.stdin.write("set term postscript enhanced color\n")
proc_BDF2_LinfL2.stdin.write('set output "convergence_16_BDF2_P2_LinfL2.eps"\n')
proc_BDF2_LinfL2.stdin.write("replot\n")
proc_BDF2_LinfL2.stdin.write("unset output\n")
proc_BDF2_LinfL2.stdin.write('quit\n') #close the gnuplot window