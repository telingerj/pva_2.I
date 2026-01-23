import time

"""
print("teď budu čekat 2s")
time.sleep(2)
print("konec")
"""

print(time.time())  # unix čas
print(time.ctime()) # unix -> běžný
cas = time.localtime()  # formátovatelný čas
print(cas.tm_hour,":",cas.tm_min)
# (year, month, day, hour, minute, second, weekday, day of the year, daylight saving)
novyCas = (2012, 5, 3, 8, 7, 24, 0, 0, 0)
time.mktime(novyCas)

#  kolik sekund jste na světě?
casNarozeni = (2003, 12, 1, 0, 0, 0, 0, 0, 0)
casNarozeniUnix = time.mktime(casNarozeni)
print(time.time() - casNarozeniUnix)
