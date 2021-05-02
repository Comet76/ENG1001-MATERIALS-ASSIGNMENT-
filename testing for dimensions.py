#variables
a = 5
b = 5
x = 1
global weights
weights = []




def secondmoment(x,y):
    y = y**3
    
    z = (x*y)/12
    return z

def checks(modulus,yielding,density,a,b):
    for i in range(200):
        for j in range(30):
            sm = secondmoment(a,b)
            sm2 = secondmoment(b, a)

            buckling = (sm*(modulus*(10**3))*9.8696)/(2000**2)
            yieldfy = (yielding*a*b)
            buckling2 = (sm2*(modulus*(10**3))*9.8696)/(2000**2)
            if buckling > 24000:
                if yieldfy>24000:

                    volume = (a/1000)*(b/1000)*2
                    mass = volume *density*1000

                    if weights !=[]:
                        if weights[0]>mass:
                            weights[0] = mass
                            weights[1] = a
                            weights[2] = b
                    else:
                        weights.append(mass)
                        weights.append(a)
                        weights.append(b)
                            

                
                
            b += 1
        a += 1
        b = 5
while x!= 0:
    
    modulus = float(input("Enter Modulus:?: "))
    yielding = float(input("Enter Yield?: "))
    density = float(input("Enter density?: "))
    checks(modulus,yielding,density,a,b)
    print(weights)
    weights = []
            
