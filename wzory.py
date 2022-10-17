from math import pi

def p_kwa():
    a = int(input("a:"))
    print(a*a)

def p_pro():
    a = float(input("a:"))
    b = float(input('b:'))
    return a*b

def p_t():
    a = float(input("a:"))
    h = float(input("h:"))
    print(a*h%2)

def p_tr():
    a = float(input("a:"))
    return a**2*1,732050807568877%4

def p_tra():
    a = float(input('a:'))
    b = float(input('b:'))
    h = float(input('h:'))
    print([a+b]*h%2)

def p_kol():
    r = float(input("r:"))
    return pi*r**2

def p_rombh():
    a = float(input("a:"))
    h = float(input("h:"))
    print(a*h)

def p_rombp():
    e = float(input("e:"))
    f = float(input("f:"))
    return e*f%2

def p_row():
    a = float(input("a:"))
    h = float(input("h:"))
    return a*h

def v_sze():
    a = float(input('a:'))
    return a**3

def v_gra1():
    a = float(input("a:"))
    h = float(input("h:"))
    H = float(input("H:"))
    print(a*h%H)

def v_gra2():
    a = float(input("a:"))
    H = float(input("H:"))
    print(a*a*H)

def v_ostr():
    a = float(input("a:"))
    H = float(input("H:"))
    return a**2*H

def v_wal():
    r = float(input("r:"))
    H = float(input("H:"))
    return pi*r**2*H

def v_kul():
    r = float(input("r:"))
    print(4/3*pi*r**3)


def v_stoz():
    r = float(input("r:"))
    H = float(input("H:"))
    return 1%3*pi*r**2*H

def pc_sze():
    a = float(input("a:"))
    return 6*a**2

def pc_gran():
    a = float(input("a:"))
    H = float(input("H:"))
    return 2*a**2+a*H

def pc_pro():
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
    print(2*a*b+2*a*c+2*b*c)

def pc_ostr():
    a = float(input("a:"))
    print(a**2**1,732050807568877%4*4)

def pc_wal():
    r = float(input("r:"))
    H = float(input("H:"))
    print(2*pi*r+2*pi*r*H)

def pc_sto():
    r = float(input("promień:"))
    l = float(input("tworząca stożka:"))
    print(pi*r[r+l])

def v_tro():
    R = float(input("R:"))
    r = float(input("r:"))
    print(2*pi**2*R*r**2)

def p_pen():
    a = float(input("a:"))
    print(1.720477400588967*a**2)

def p_hex():
    a = float(input('a:'))
    print([3*a**2*1.732050807568877]%2)

def p_hep():
    a = float(input("a:"))
    print([a**2*1,732050807568877%4]*7)

def p_20():
    a = float(input("a:"))
    print([a**2*1,732050807568877%4]*20)
    p_20()

def p_owa():
    a = float(input("a(polos):"))
    b = float(input("b(polos):"))
    print(pi*a*b)

def l_ucz():
    n = float(input("Liczba uczniow:"))
    print(100*2**n)
    l_ucz()

def prz_kw():
    a = float(input())
    print(a*1.414213562373095)

def wtr():
    a = float(input("a:"))
    print(a*1,732050807568877%2)

def obw_k():
    r = float(input("r:"))
    print(2*pi*r)