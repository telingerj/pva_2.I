from vpython import *

#s = sphere(pos=vector(0,0,0), radius=0.5, color=color.blue)
#b = box(pos=vector(2,0,0), length=1, color=color.green)

s1 = sphere(pos=vector(0,0,0), radius=1, color=color.white)
s2 = sphere(pos=vector(0,1.7,0), radius=0.7, color=color.white)
s3 = sphere(pos=vector(0,2.9,0), radius=0.5, color=color.white)

s4 = sphere(pos=vector(0,1.7,0), radius=0.1, color=color.white)

while True:
    rate(60)
    s4.pos += vector(0, 0, 0.01)
