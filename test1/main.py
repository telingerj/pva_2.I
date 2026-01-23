a = int(input())
b = int(input())
c = int(input())

prumer = (a + b + c) / 3
if prumer <= 1.5:
    print("prospěl s vyznamenáním")
if prumer >= 4.5:
    print("neprospěl")
else:
    print("prospěl")