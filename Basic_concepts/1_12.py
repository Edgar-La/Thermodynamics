#Exercise 1.12
#Give Tc, Pc, Vc calculate van der Waals constantes a, b.

Tc = float(input('Tc: '))
Pc = float(input('Pc: '))
Vc = float(input('Vc: '))

b = Vc/3
R = 0.08206
a = (27/8)*Tc*R*b

print() #enter space
print('a = ' + str(a))
print('b = ' + str(b))
input() #wait