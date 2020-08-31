import matplotlib.pyplot as plt
#Plot the van der Waals P-V curves for some gas
#Compare the curves for CO2 and He with ideal gas eq.

N = 1
R = 0.08206
T = 25 + 273.15
a_CO2 = 3.59
b_CO2 = 0.0427
a_He  = 0.034
b_He  = 0.0237

V = []
P_CO2 = []
P_He = []
P_ideal = []
v = 0.05
while (v <= 0.4):
	V.append(v)
	p_CO2 = 0; p_He = 0
	p_CO2 = (N*R*T)/(v-b_CO2) - (a_CO2)/(v**2)
	p_He  = (N*R*T)/(v-b_He ) - (a_He )/(v**2)
	p_ideal = (N*R*T)/v
	P_CO2.append(p_CO2)
	P_He.append(p_He)
	P_ideal.append(p_ideal)
	v+=0.01

plt.clf()
plt.title('Exercise 1.10')
plt.xlabel('V')
plt.ylabel('P')
plt.plot(V, P_CO2, label = 'CO2')
plt.plot(V, P_He, label = 'He')
plt.plot(V, P_ideal, label = 'Ideal')
plt.legend()
plt.show()