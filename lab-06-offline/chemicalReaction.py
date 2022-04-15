#Name: Md Sezan Mahmud Saikat
#ID: 011 173 045

A = []
B = []
C = []

n = int(5)

A.append(float(50))
B.append(float(50))
C.append(float(25))

kf = float(0.05)
kb = float(0.01)
dt = float(0.3)

ddtA = float(0.0)
ddtB = float(0.0)
ddtC = float(0.0)

for i in range(1, n+1, 1):
    ddtA = (kb*pow(C[i-1], 2))-(kf*A[i-1]*B[i-1])
    #print("---", ddtA)
    ddtB = (kb*pow(C[i-1], 2))-(kf*A[i-1]*B[i-1])
    #print("---", ddtB)
    ddtC = (3*kf*A[i-1]*pow(B[i-1], 3))-(kb*pow(C[i-1], 2))
    #print("---", ddtC)

    A.append(A[i-1]+(ddtA*dt))
    B.append(B[i-1]+(ddtB*dt))
    C.append(C[i-1]+(ddtC*dt))

t=float(0)
for j in range(n+1):
    print("At time:",t)
    print(A[j], B[j], C[j])
    print("\n")
    t=t+0.3
