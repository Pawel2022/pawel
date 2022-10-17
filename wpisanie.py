print("1 - kwadrat 2 - prostokat 3 - trojkat 4 - trojkat(rownoboczny) 5 - trapez 6 - kolo 7 - romb(z h) 8 - romb(przekatne) 9 - rownoleglobok 10 - V szescianu 11 - V graniastoslupa(pole trojkata (a*h/2)) 12 - V prostopadloscianu 13 - V ostroslupa(podstawa kwadrat) 14 - V walca  15 - V kuli 16 - V stozka 17 - Pc szescianu 18 - Pc graniastoslupa(podstawa kwadratu) 19 - Pc Prostopadloscianu  20 - Pc ostroslupa prawidłowego 21 - Pc walca 22 - Pc stozka 23 - V Toroida(donata) 24 - pole pentagonu 25 - pole hexagonu foremnego 26 - pole heptagonu foremnego 27 -  pole dwudziestokata foremnego 28 - pole owalu 29 - 'liczba uczniów' 30 - przekatna kwadratu 31 - wysokosc trojkata rownobocznego 32 - obw kola")
qq = float(input())
if qq == 1:
    from wzory import p_kwa
    p_kwa()

if qq == 2:
    from wzory import p_pro
    p_pro()
    print(p_pro())

if qq == 3:
    from wzory import p_t
    p_t()

if qq == 4:
    from wzory import p_tr
    p_tr()
    print(p_tr())

if qq == 5:
    from wzory import p_tra
    p_tra()

if qq == 6:
    from wzory import p_kol
    p_kol()
    print(p_kol())

if qq == 7:
    from wzory import p_rombh
    p_rombh()

if qq == 8:
    from wzory import p_rombp
    p_rombp()
    print(p_rombp())

if qq == 9:
    from wzory import p_row
    p_row()
    print(p_row())

if qq == 10:
    from wzory import v_sze
    v_sze()
    print(v_sze())

if qq == 11:
    from wzory import v_gra1
    v_gra1()

if qq == 12:
    from wzory import v_gra2
    v_gra2()

if qq == 13:
    from wzory import v_ostr
    v_ostr()
    print(v_ostr())

if qq == 14:
    from wzory import v_wal
    v_wal()
    print(v_wal())

if qq == 15:
    from wzory import v_kul
    v_kul()

if qq == 16:
    from wzory import v_stoz
    v_stoz()
    print(v_stoz())

if qq == 17:
    from wzory import pc_sze
    pc_sze()
    print(pc_sze())

if qq == 18:
    from wzory import pc_gran
    pc_gran()
    print(pc_gran())

if qq == 19:
    from wzory import pc_pro
    pc_pro()

if qq == 20:
    from wzory import pc_ostr
    pc_ostr()

if qq == 21:
    from wzory import pc_wal
    pc_wal()

if qq == 22:
    from wzory import pc_sto
    pc_sto()

if qq == 23:
    from wzory import v_tro
    v_tro()

if qq == 24:
    from wzory import p_pen
    p_pen()

if qq == 25:
    from wzory import p_hex
    p_hex()

if qq == 26:
    from wzory import p_hep
    p_hep()

if qq == 27:
    from wzory import p_20
    p_20()

if qq == 28:
    from wzory import p_owa
    p_owa()

if qq == 29:
    from wzory import l_ucz
    l_ucz()

if qq == 30:
    from wzory import prz_kw
    prz_kw()

if qq == 31:
    from wzory import wtr
    wtr()
    print(wtr())

if qq == 32:
    from wzory import obw_k
    obw_k()
