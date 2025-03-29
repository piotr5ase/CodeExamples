"""
Osbługa wyjątków
try: - chce coś zrobić
    print(x)
    jak x nie istnieje to nie przewie dzialania programu, przekaze go do exception
except Exception as exc: #blad w exc sie zapisze i nie zatrzyma programu
    print(exc)
except TypeError exc #8//"b" to type error

except ZeroDivisionError as exc #8/0 to ten przypadek
        /\
        |
przewidywane błedy
nieprzewidywany błąd:
except Exception as exc:

finally:
    pass
jak już ci nadzieji zabraknie

raise TypeError powoduje wywołanie błędu danego typu. W tym wypadku TypeError
najczęściej wykorzystywane w funkcjach
np.
def dod(a,b):
    #jezeli typ jest niepoprawny
    raise TypeError

Program, story prosi o podanie 2 liczb i wykonuje dzielenie i obsługuje błędy
"""

while True:
    print('Podaj liczy do dzielenia')
    x = input()
    y = input()
    try:
        x = float(x)
        y = float(y)
        z = x / y
        print(z)
    except TypeError:
        print('Wygrałeś')
    except ZeroDivisionError:
        print('Dzielenie przez zero')
    except ValueError:
        print('To nie jest liczba')
    else:
        print('Wsystko działa')







