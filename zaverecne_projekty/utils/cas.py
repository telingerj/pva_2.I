import time

cas_zacatek = time.time()  # čas ve formátu unix - počet sekund od 1. 1. 1970

x = 0
for i in range(10000000):  # simulace náročného výpočtu
    x += i ** 20

ubehly_cas = time.time() - cas_zacatek  # aktuální čas - čas na začátku
print(ubehly_cas)
