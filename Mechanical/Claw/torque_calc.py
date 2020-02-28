import math

D = 8 #mm
f = 0.3 
g = 9.81 #kg/m2
L = 4 #mm
m = 2 #kg

realistic_cooef = 3
print ("Diameter = {}mm, Lead = {}mm, Weight = {}kg\n".format(D,L,m))

A = math.atan(L/ (D * math.pi))
B = math.atan(f)
print ("A = {} rad, B = {} rad".format(A,B))

VR = D * math.pi / L
print ("VR = {}".format(VR))

n = math.tan(A) / math.tan(A + B)
print ("n = {}".format(n))

MA = VR * n
print ("MA = {}".format(MA))
Fe = m * g / MA
print ("Fe = {}".format(Fe))

r = D / 2 
T = Fe * r/1000 #r to metres from mm

print ("T = {} Nm; T= {} gcm".format(T, T/g*1000*100))

rT = T * realistic_cooef
print ("rT = {} Nm; rT= {} gcm".format(rT, rT/g*1000*100))
