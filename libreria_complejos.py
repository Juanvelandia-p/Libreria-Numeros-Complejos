import math

def suma_comp(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])

def resta_comp(c1,c2):
    return (c1[0]-c2[0],c1[1]-c2[1])

def multi_comp(c1,c2):
    return ((c1[0]*c2[0])-(c1[1]*c2[1]),(c1[0]*c2[1])+(c1[1]*c2[0]))

def divi_comp(c1,c2):
    return (((c1[0]*c2[0])+(c1[1]*c2[1])/(c1[1]**2)+(c2[1]**2)),((c1[1]*c2[0])-(c1[0]*c2[1]))/(c1[1]**2)+(c2[1]**2))

def modulo_comp(c):
    return (c[0]**2+c[1]**2)**(1/2)

def conjugado_Complejo(c):
    return(c[0],-c[1])

def fase(c):
    return(math.atan2(c[1],c[0]))

def Conversion_cartesianas_a_polares(c):
    return(modulo_comp(c),fase(c))

def Conversio_polares_a_cartesianas(p):
    return(p[0]*math.cos(p[1]),p[0]*math.sin(p[1]))

c1 = (1,5)
c2 = (3,2)

print(Conversio_polares_a_cartesianas(c2))