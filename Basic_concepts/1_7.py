import numpy as np

a = 3.59; print('a = ' + str(a))
b = 0.0427; print('b = ' + str(b))
R = 0.08206; print('R = ' + str(R))
T = 25 + 273.15; print('T = ' + str(T))
P = 1; print('P = ' + str(P))
N = 1; print('N = ' + str(N))

V_avdg_ideal = (N*R*T)/P
#Ingresamos los coeficientes de la expresion cubica
coeff = [P, -((P*b) + (R*T)), a, -a*b]
#Con la funcion np.roots() calculamos raices
Roots = np.roots(coeff)
print('\nLas raices son: ');print(Roots)

V_avgd_vdw = input('\nIntroduce manualmente la raiz real: ')
print()
print('V_avdg_ideal: ' + str('{0:.4g}'.format(V_avdg_ideal)))
print('V_avdg_ideal: ' + str(V_avgd_vdw))

#Calcula la diferencia de error
Error = ((V_avdg_ideal- float(V_avgd_vdw))/float(V_avdg_ideal))*100
print('\nEl error es de: ' + str('{0:.3g}'.format(Error)) + '%')

input()
