def pozdrav():
    print("ahoj")
    print("jak se máš")

def pozdrav_jmeno(jmeno):
    print("ahoj", jmeno)

def pozdrav_dva_lidi(jmeno1, jmeno2):
    print("ahoj", jmeno1, "a", jmeno2)


def prvni_pismeno(slovo):
    return slovo[0]

def dve_hodnoty(a):
    return [a + 1, a + 2]

def druha_mocnina(x):
    return x ** 2

def absolutni_hodnota(x):
    if x >= 0:
        return x
    return x * -1


def kvadraticka_rovnice(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    if D == 0:
        return -b / (2 * a)

    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    return [x1, x2]

print(kvadraticka_rovnice(1, 0, -1))
print(kvadraticka_rovnice(1, 0, 1))
print(kvadraticka_rovnice(1, 0, 0))
print(kvadraticka_rovnice(1, 1, 0))
print(kvadraticka_rovnice(1, -8, 15))

# funkce, která vrací druhou mocninu čísla
# funkce, která vrací absolutní hodnotu čísla

# funkce, která přijímá jako parametry koeficienty
# kvadr. rovnice a vrací řešení