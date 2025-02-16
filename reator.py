import numpy as np
import sympy as sp
import math

#variaveis
Ca0     = 8
V       = 1.36
To      = 294.7
Vj      = 0.085
alpha   = 7.08e10
E       = 69815
U       = 3065
A       = 23.22
Tjo     = 294.7
R       = 8.314
H       = 69815
cp      = 3.13
cpj     = 4.18
r       = 800
rj      = 1000

#U de equilibrio
F0      = 1.13
Fj      = 1.41

Ca, T, Tj = sp.symbols('Ca T Tj')
x= sp.symbols('x')

equation_list = list()
equation_list.append(sp.Eq((F0/V)*(Ca0 - Ca) - 
                        alpha*sp.exp(-E/(R*T)), 0));
equation_list.append(sp.Eq((F0/V)*(Tjo - T) - 
                        (H*alpha/(r*cp))*Ca*sp.exp(-E/(R*T)) -
                        (U*A/(r*cp*V))*(T - Tj), 0));
equation_list.append(sp.Eq((Fj/Vj)*(Tjo - Tj) + 
                        (U*A/(rj*cpj*Vj))*(T - Tj), 0));



print(equation_list)

