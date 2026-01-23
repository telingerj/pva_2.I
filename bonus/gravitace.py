from vpython import *

s = sphere(pos=vector(0,0,0), radius=1, color=color.blue)
v = vector(0,0,0)
g = vector(0,-0.001,0)

while True:
    rate(60)
    s.pos += v
    v += g
    if s.pos.y < -3:
        s.pos.y = -3
        v.y *= -0.9

