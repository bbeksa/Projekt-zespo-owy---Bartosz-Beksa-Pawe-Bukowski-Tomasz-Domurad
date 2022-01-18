import os


#wzorfaktury4.png i 4v2 TYLKO na 3 produkty
def DatafromTextW1(nazwa):

    file = open(os.path.dirname(__file__) + "/../" + nazwa)

    content = file.readlines()

    numerFaktury = content[1].split(None, 1)[1]

    miasto = content[45].split(None, 2)[2]

    dataWystawienia = content[46].split(None, 2)[2]

    dataSprzedazy = content[47].split(None, 2)[2]

    sprzedawcaImie = content[49].split()[1]
    sprzedawcaNazwisko = content[49].split()[2]

    nabywcaImie = content[49].split()[3]
    nabywcaNazwisko = content[49].split()[4]

    sprzedawcaKodPocztowy = content[51].split(None, 3)[0]
    sprzedawcaMiasto = content[51].split(None, 3)[1]

    sprzedawcaUlica = content[50].split()[0]
    sprzedawcaNrUlicy = content[50].split()[1]

    nabywcaKodPocztowy = content[51].split(None, 3)[2]
    nabywcaMiasto = content[51].split(None, 3)[3]

    nabywcaUlica = content[50].split()[2]
    nabywcaNrUlicy = content[50].split()[3]

    NIP = content[52].split(None, 1)[1]

    nazwaTowaru1 = content[54].split()[1]
    ilosc1 = content[54].split()[3]
    cenaNetto1 = content[54].split()[4]
    VAT1 = content[54].split()[5]
    VAT1 = float(VAT1[:-1])/100

    nazwaTowaru2 = content[55].split()[1]
    ilosc2 = content[55].split()[3]
    cenaNetto2 = content[55].split()[4]
    VAT2 = content[55].split()[6]
    VAT2 = float(VAT2[:-1])/100

    nazwaTowaru3 = content[56].split()[1]
    ilosc3 = content[56].split()[3]
    cenaNetto3 = content[56].split()[4]
    VAT3 = content[56].split()[6]
    VAT3 = float(VAT3[:-1])/100

    slownie = content[61].split(None, 5)[5]

    formaPlatnosci = content[63].split(None, 2)[2]

    terminZaplaty = content[64].split(None, 2)[2]

    numerKonta = content[69]

    bank = content[70]

    return [numerFaktury, miasto, dataWystawienia, dataSprzedazy,
            sprzedawcaImie, sprzedawcaNazwisko, sprzedawcaKodPocztowy, sprzedawcaMiasto, sprzedawcaUlica, sprzedawcaNrUlicy,
            nabywcaImie, nabywcaNazwisko, nabywcaKodPocztowy, nabywcaMiasto, nabywcaUlica, nabywcaNrUlicy, NIP,
            nazwaTowaru1, ilosc1, cenaNetto1, VAT1,
            nazwaTowaru2, ilosc2, cenaNetto2, VAT2,
            nazwaTowaru3, ilosc3, cenaNetto3, VAT3,
            slownie, formaPlatnosci, terminZaplaty, numerKonta, bank]

#wzór faktury generowanej przez program TYLKO na 2 produkty
def DatafromTextW2(nazwa):

    file = open(os.path.dirname(__file__) + "/../" + nazwa)

    content = file.readlines()

    numerFaktury = content[0].split()[2]

    miasto = content[2].split(None, 2)[2]

    dataWystawienia = content[3].split(None, 2)[2]

    dataSprzedazy = content[4].split(None, 2)[2]

    sprzedawcaImie = content[9].split()[0]
    sprzedawcaNazwisko = content[9].split()[1]

    nabywcaImie = content[9].split()[2]
    nabywcaNazwisko = content[9].split()[3]

    sprzedawcaKodPocztowy = content[12].split()[0]
    sprzedawcaMiasto = content[12].split()[1]

    sprzedawcaUlica = content[10].split()[0]
    sprzedawcaNrUlicy = content[10].split()[1]

    nabywcaKodPocztowy = content[15].split(None)[0]
    nabywcaMiasto = content[15].split(None)[1]

    nabywcaUlica = content[10].split()[2]
    nabywcaNrUlicy = content[10].split()[3]

    NIP = content[13].split(None, 1)[1]

    nazwaTowaru1 = content[30].split()[1]
    ilosc1 = content[30].split()[2]
    cenaNetto1 = content[30].split()[3]
    VAT1 = content[30].split()[4]
    VAT1 = float(VAT1[:-1])/100

    nazwaTowaru2 = content[31].split()[1]
    ilosc2 = content[31].split()[2]
    cenaNetto2 = content[31].split()[3]
    VAT2 = content[31].split()[4]
    VAT2 = float(VAT2[:-1])/100

    nazwaTowaru3 = ' '
    ilosc3 = 0
    cenaNetto3 = 0
    VAT3 = 0
    VAT3 = 0

    slownie = ' '

    formaPlatnosci = ' '

    terminZaplaty = content[39].split(None, 2)[2]

    numerKonta = ' '

    bank = ' '

    return [numerFaktury, miasto, dataWystawienia, dataSprzedazy,
            sprzedawcaImie, sprzedawcaNazwisko, sprzedawcaKodPocztowy, sprzedawcaMiasto, sprzedawcaUlica, sprzedawcaNrUlicy,
            nabywcaImie, nabywcaNazwisko, nabywcaKodPocztowy, nabywcaMiasto, nabywcaUlica, nabywcaNrUlicy, NIP,
            nazwaTowaru1, ilosc1, cenaNetto1, VAT1,
            nazwaTowaru2, ilosc2, cenaNetto2, VAT2,
            nazwaTowaru3, ilosc3, cenaNetto3, VAT3,
            slownie, formaPlatnosci, terminZaplaty, numerKonta, bank]

#wzorfaktury8.png TYLKO na 1 produkt
def DatafromTextW3(nazwa):

    file = open(os.path.dirname(__file__) + "/../" + nazwa)

    content = file.readlines()

    numerFaktury = content[0].split(None, 2)[2]

    miasto = content[14].split()[1]

    dataWystawienia = content[2].split(None, 2)[2]

    dataSprzedazy = content[3].split()[5]

    sprzedawcaImie = content[12].split(None, 4)[0]
    sprzedawcaNazwisko = content[12].split()[1] + " " + content[12].split()[2] + "." + content[12].split()[3]

    nabywcaImie = content[12].split()[4]
    nabywcaNazwisko = content[12].split()[5]

    sprzedawcaKodPocztowy = content[14].split()[0]
    sprzedawcaMiasto = content[14].split()[1]

    sprzedawcaUlica = content[13].split()[1]
    sprzedawcaNrUlicy = content[13].split()[2]

    nabywcaKodPocztowy = content[14].split(None)[2]
    nabywcaMiasto = content[14].split(None)[3]

    nabywcaUlica = content[13].split()[4]
    nabywcaNrUlicy = content[13].split()[5]

    NIP = content[15].split(None, 1)[1]

    nazwaTowaru1 = content[21].split()[1] + " " + content[21].split()[2] + " " + content[21].split()[3]
    ilosc1 = content[21].split()[6]
    cenaNetto1 = content[21].split()[7] + content[21].split()[8]
    VAT1 = content[21].split()[11]
    VAT1 = float(VAT1[:-1])/100

    nazwaTowaru2 = ' '
    ilosc2 = 0
    cenaNetto2 = 0
    VAT2 = 0
    VAT2 = 0

    nazwaTowaru3 = ' '
    ilosc3 = 0
    cenaNetto3 = 0
    VAT3 = 0
    VAT3 = 0

    slownie = ' '

    formaPlatnosci = ' '

    terminZaplaty = content[3].split()[5]

    numerKonta = ' '

    bank = ' '

    return [numerFaktury, miasto, dataWystawienia, dataSprzedazy,
            sprzedawcaImie, sprzedawcaNazwisko, sprzedawcaKodPocztowy, sprzedawcaMiasto, sprzedawcaUlica, sprzedawcaNrUlicy,
            nabywcaImie, nabywcaNazwisko, nabywcaKodPocztowy, nabywcaMiasto, nabywcaUlica, nabywcaNrUlicy, NIP,
            nazwaTowaru1, ilosc1, cenaNetto1, VAT1,
            nazwaTowaru2, ilosc2, cenaNetto2, VAT2,
            nazwaTowaru3, ilosc3, cenaNetto3, VAT3,
            slownie, formaPlatnosci, terminZaplaty, numerKonta, bank]





