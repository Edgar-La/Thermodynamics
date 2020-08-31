import matplotlib.pyplot as plt

print('Exercise 1.5, chapter 1\n')
#H2
a = 0.244; #print('a = ' + str(a))
b = 0.0266; #print('b = ' + str(b))
R = 0.08206; #print('R = ' + str(R))
T = 300; #print('T = ' + str(T))
V = 10; #print('V = ' + str(V))


N = []
P_vdw = []
P_ideal = []
for n in range(1,101,1):
	N.append(n)
	p1 = 0; p2 = 0
	p1 = (n*R*T)/V
	p2 = ((R*T*n)/(V-(n*b)))-((a*n*n)/(V*V))
	P_ideal.append(p1)
	P_vdw.append(p2)

#print(N); print(P_ideal); print(P_vdw)

plt.clf()
plt.title('Exercise 1.5\nP_ideal vs N\nP_vdw vs N')
plt.xlabel('N')
plt.ylabel('P_ideal & P_vw')
plt.plot(N,P_ideal,  label="P_ideal vs N")
plt.plot(N,P_vdw,  label="P_vdw vs N")
plt.legend()
plt.show()