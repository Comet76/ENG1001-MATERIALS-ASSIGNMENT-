#variables
r = 3
global weights
weights = []
x = 1
#functions
def secondmoment(x):
    x = x**4
    z = (x*3.14)/4
    return z


def checks(modulus,yielding,density,r):
    for i in range(15):
        sm = secondmoment(r)
        buckling = (sm*(modulus*(10**3))*9.8696)/(2000**2)
        yieldfy = (yielding*(r*r*3.14))
        if buckling > 24000:
            if yieldfy>24000:
                print("This works. r:"+str(r))
                volume = (3.14*((r/1000)**2)*2)
                mass = volume *density*1000
                print("gives a mass of "+str(mass))
                if weights !=[]:
                    if weights[0]>mass:
                            weights[0] = mass
                            weights[1] = a
                            weights[2] = b
                else:
                    weights.append(mass)
                    weights.append(a)
                    weights.append(b)
                
        r += 1
#main
while x!= 0:
    modulus = float(input("Enter Modulus:?: "))
    yielding = float(input("Enter Yield?: "))
    density = float(input("Enter Density: "))
    sm = secondmoment(r)
    buckling = (sm*(modulus*(10**3))*9.8696)/(2000**2)
    checks(modulus,yielding,density,r)
    print(weights)
    weights = []

